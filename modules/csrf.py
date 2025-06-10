import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from colorama import Fore, Style

def run():
    print("Running CSRF scan (heuristic)...")
    url = input("Enter target URL: ").strip()

    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
    except Exception as e:
        print(Fore.RED + f"[ERROR] Failed to fetch URL: {e}")
        return

    soup = BeautifulSoup(res.text, "html.parser")
    forms = soup.find_all("form")
    if not forms:
        print(Fore.YELLOW + "[!] No forms found on the page.")
        return

    csrf_keywords = ["csrf", "token", "_csrf"]
    vulnerable_count = 0

    for i, form in enumerate(forms, start=1):
        action = form.get("action") or "[no action]"
        method = form.get("method", "GET").upper()
        inputs = form.find_all("input")
        input_names = [inp.get("name", "").lower() for inp in inputs]

        has_csrf = any(kw in name for name in input_names for kw in csrf_keywords)

        print(Style.BRIGHT + f"\nForm {i}:")
        print(Fore.CYAN + f"  Action: {urljoin(url, action)}")
        print(Fore.CYAN + f"  Method: {method}")
        print(Fore.CYAN + f"  Inputs: {[inp.get('name') for inp in inputs]}")

        if not has_csrf:
            print(Fore.RED + f"[!] Form {i} might be vulnerable (no CSRF token detected).")
            vulnerable_count += 1
        else:
            print(Fore.GREEN + f"[+] Form {i} appears to have CSRF protection.")

    print(Style.BRIGHT + Fore.YELLOW + f"\n[!] Scan completed. {vulnerable_count} form(s) may be vulnerable.")
    
