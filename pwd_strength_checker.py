import string

def check_pwd_strength(password):
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    symbol = any(char in string.punctuation for char in password)
    
    if len(password) < 8:
        return "Password too short! Must be at least 8 characters."
    elif not (upper and lower and digit and symbol):
        return "Weak Password: Include upper, lower, digit, and symbol."
    else:
        return "Strong Password!"

def main():
    while True:
        pwd = input("\nEnter a password to check (or type 'exit' to quit): ")
        if pwd.lower() == "exit":
            print("Exiting password checker.")
            break
        result = check_pwd_strength(pwd)
        print(result)

main()