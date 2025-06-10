import requests
from colorama import Fore

def run():
    print("Running Web Cache Poisoning scan (heuristic)...")
    url = input("Enter target URL: ").strip()

    payloads = [
        "cachepoison=1",
        "cb=evil",
        "callback=evil",
        "x=1<script>alert(1)</script>",
        "utm_source=eviltest",
        "debug=1",
        "preview=true",
        "redirect=http://evil.com",
        "host=evil.com"
    ]

    poisoned = False

    for payload in payloads:
        test_url = url + ("&" if "?" in url else "?") + payload
        try:
            res = requests.get(test_url, timeout=5)
            headers = res.headers
            body = res.text.lower()

            if "x-cache" in headers and ("hit" in headers["x-cache"].lower() or "cache" in headers["x-cache"].lower()):
                print(Fore.RED + f"[!] Potential Web Cache Poisoning via payload: {payload}")
                poisoned = True
            elif "cached" in body or "via" in headers.get("via", "").lower():
                print(Fore.YELLOW + f"[?] Suspicious cache behavior with payload: {payload}")
                poisoned = True
        except Exception as e:
            print(Fore.RED + f"[ERROR] {e}")

    if not poisoned:
        print(Fore.YELLOW + "[!] No cache poisoning indicators found.")

