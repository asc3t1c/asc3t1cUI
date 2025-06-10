import requests
from bs4 import BeautifulSoup
from colorama import Fore

def run():
    print("Running CSRF scan (heuristic)...")
    url = input("Enter target URL: ").strip()

    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        forms = soup.find_all("form")
        if not forms:
            print(Fore.YELLOW + "[!] No forms found on the page.")

        for idx, form in enumerate(forms, 1):
            inputs = form.find_all("input")
            csrf_found = False
            for input_tag in inputs:
                name = input_tag.get("name", "").lower()
                if "csrf" in name or "token" in name:
                    csrf_found = True
                    break

            if csrf_found:
                print(Fore.GREEN + f"[+] Form {idx} appears protected (CSRF token found).")
            else:
                print(Fore.RED + f"[!] Form {idx} might be vulnerable (no CSRF token detected).")

    except Exception as e:
        print(Fore.RED + f"[ERROR] Failed to scan for CSRF: {e}")

