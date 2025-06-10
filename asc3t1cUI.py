#!/usr/bin/python
# by nu11secur1ty 2025
import importlib
from colorama import Fore, init

init(autoreset=True)

def print_menu():
    print(Fore.CYAN + "=== Vulnerability Scanner ===")
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
    print("10. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter choice (1-10): ").strip()
        if choice == '10':
            print("Exiting.")
            break
        module_name = None
        if choice == '1':
            module_name = "modules.xss"
        elif choice == '2':
            module_name = "modules.sqli"
        elif choice == '3':
            module_name = "modules.path_traversal"
        elif choice == '4':
            module_name = "modules.rfi"
        elif choice == '5':
            module_name = "modules.lfi"
        elif choice == '6':
            module_name = "modules.csrf"
        elif choice == '7':
            module_name = "modules.open_redirect"
        elif choice == '8':
            module_name = "modules.command_injection"
        elif choice == '9':
            module_name = "modules.web_cache"
        else:
            print(Fore.YELLOW + "Invalid choice. Try again.")
            continue

        try:
            module = importlib.import_module(module_name)
            module.run()
        except Exception as e:
            print(Fore.RED + f"Error loading module: {e}")

if __name__ == "__main__":
    main()
