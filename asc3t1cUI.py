#!/usr/bin/python
# by nu11secur1ty 2025

import importlib
import sys
from colorama import Fore, init

init(autoreset=True)

def print_menu():
    print(Fore.CYAN + "=== asc3t1cUI, the Vulnerability Scanner and Injector ===")
    print(Fore.CYAN + "=== WARNING: This is a CUSTOM SCANNER! You MUST know what you're scanning! ===")
    print("Select vulnerability to test:")
    print("1. XSS")
    print("2. SQL Injection")
    print("3. Path Traversal")
    print("4. RFI")
    print("5. LFI")
    print("6. CSRF")
    print("7. Open Redirect")
    print("8. Command Injection")
    print("9. Web Cache")
    print("10 asce3t1c-SQLi")
    print("11. Exit")

def main():
    while True:
        print_menu()
        try:
            choice = input("Enter choice (1-11): ").strip()
        except KeyboardInterrupt:
            print("\n" + Fore.YELLOW + "User interrupted (Ctrl+C). Exiting.")
            sys.exit(0)

        if choice == '':
            print(Fore.YELLOW + "No input detected. Exiting.")
            break

        if choice == '11':
            print("Exiting.")
            break

        modules_map = {
				'1': "modules.xss",
				'2': "modules.sqli",
				'3': "modules.path_traversal",
				'4': "modules.rfi",
				'5': "modules.lfi",
				'6': "modules.csrf",
				'7': "modules.open_redirect",
				'8': "modules.command_injection",
				'9': "modules.web_cache",
				'10': "modules.sqlmap_external",
}

        module_name = modules_map.get(choice)
        if not module_name:
            print(Fore.YELLOW + "Invalid choice. Try again.")
            continue

        try:
            module = importlib.import_module(module_name)
            module.run()
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\nScan interrupted by user (Ctrl+C). Returning to main menu...\n")
            continue
        except Exception as e:
            print(Fore.RED + f"Error loading module: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nExiting due to user interrupt (Ctrl+C).")
        sys.exit(0)
