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

        # Map user choice to module name (folder.module)
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
        }

        module_name = modules_map.get(choice)
        if not module_name:
            print(Fore.YELLOW + "Invalid choice. Try again.")
            continue

        try:
            # Import the selected module dynamically
            module = importlib.import_module(module_name)
            # Call the run() function inside the module
            module.run()
        except Exception as e:
            print(Fore.RED + f"Error loading module: {e}")

if __name__ == "__main__":
    main()
