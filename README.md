# 💀Web Login BruteForce💀

## 📜Description
This is an interactive Python script designed to perform brute force login attacks on a target web application.  
It allows users to test a list of passwords against a specific username on a given target URL.  
The script provides multiple detection methods to identify successful logins, making it flexible  
and adaptable for various target systems.  

## 🔑Features
- Accepts target URL, username, and password file path dynamically.  
- Keyword detection in response (e.g., "welcome back").  
- URL redirection detection (e.g., /dashboard).  
- Cookie/token-based success detection (e.g., auth_token).  
- HTTP status code-based success detection (e.g., 200 or 302).  

## 🚀Step-by-Step Guide in Linux Terminal !

Step 1: Update & upgrade your system  
>sudo apt update  
>sudo apt upgrade  

Step 2: Clone the repository  
>git clone https://github.com/The-Real-Virus/Web-Login-BruteForce.git  

Step 3: Go to the Tool Directory where u clone it and read requirements.txt file !  
>cd Web-Login-BruteForce      
(read requirements.txt file using cat or gedit)  

Step 4: extract the rockyou file using unrar  
>sudo apt install unrar (if it is not installed in ur kali linux)  
>unrar x rockyou.rar  

Step 5: After Completing the process now u can run script  
>python3 Script.py  

## ⚙️Troubleshooting
1) `Missing :` 'rockyou.txt' file: If the script doesn't find the rockyou.txt file, make sure it is in the same
directory or specify the full path in the script.

2) `Permission Denied:` Ensure the script is run with the necessary privileges.

3) `Module Error :` If the requests module is not installed, install it ( see requirements.txt for commands )

## 💡Steps to Determine the Needle !
1) Analyze the Login Response for Success:  
- Use tools like Postman, Burp Suite, or browser developer tools (F12) to inspect the HTTP response from the server.  
- Perform a valid login with correct credentials and observe the response.  
- Does the page redirect to a dashboard or profile page?  
- Is there a success message like "Welcome back," "Login successful," or similar?  
- Are there unique strings in the page content that indicate success (e.g., profile, logout, etc.)?  

2) Analyze the Response for Failures:  
- Perform a login with incorrect credentials and observe the error messages.  
- Compare the failed response with a successful one to identify what changes (e.g., missing or added keywords, response codes, etc.).  

3) Give the Needle when run:  
- Once you identify , Choose a detection method and write the needle ( of success login ).  

## 🤝Follow the Prompts !
*) The script will guide you through the following steps:  
- Enter the target URL (e.g., http://example.com:8080/login).  
- Enter the username to test (e.g., admin).  
- Provide the path to the password file (e.g., rockyou.txt).  
- Choose a detection method(needle):  
  1: Keyword detection in the response.  
  2: URL redirection detection.  
  3: Cookie/token detection.  
  4: HTTP status code detection.  
- If required, specify the success keyword, redirect URL, cookie name, or HTTP status code.  

## 🛠️MODIFICATION ( use own wordlist )

if u want to use ur own wordlist instead of rockyou.txt , u can modify in the script ,  

Step 1: create ur own wordlist  

Step 2: move it into the Web-Login-BruteForce Directory ( deleting rockyou is not necessory )  

Step 3: While running the script , it ask for password file then type the name of ur own created list .  

## 📂Example OutPut
	==== Interactive Login Bruteforce Script ====
	Enter the target URL (e.g., http://example.com:8080/login): http://testsite.com:8080/login
	Enter the username to test: admin
	Enter the path to the password file (e.g., rockyou.txt): passwords.txt

	[?] Detection Methods: 
	1. Search for a specific success keyword in the response (e.g., 'welcome back').
	2. Detect redirection to a specific URL (e.g., '/dashboard').
	3. Check for a specific cookie or authentication token (e.g., 'auth_token').
	4. Match a specific HTTP status code (e.g., 200 or 302).

	Choose a detection method (1/2/3/4): 1
	Enter the success keyword (e.g., 'welcome back'): welcome back

	==== Starting Bruteforce ====
	Target: http://testsite.com:8080/login
	Username: admin
	Password file: passwords.txt
	Number of passwords to test: 5

	[1/5] Attempting -> admin:password123
	[2/5] Attempting -> admin:qwerty
	[>>>] Success! Valid password 'qwerty' found for user 'admin'.

	==== Bruteforce Complete ====

# ⚠️Disclaimer !
This tool is intended for ethical and educational use only.  
Do not use it for illegal activities. The author is not responsible for any misuse.  
This script is intended for educational purposes and authorized testing only.  
Unauthorized use of this script is illegal and unethical.  
Ensure you have explicit permission before testing any system.  
- Obtain explicit permission before testing any system.  
- Adhere to all applicable laws and regulations.  
- Respect user privacy and data.  
- By using this script, you agree to take full responsibility for your actions.  
