COMMON_PASSWORDS = {
    "123456", "123456789", "password",  "qwerty", "login", 
    "abc123", "password1", "123123","admin", "welcome",    
}

def check_password_strength(password):
    length_ok = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)
 
    if not length_ok:
        return "Weak", ["Password must be at least 8 characters long."]

    criteria_met = sum([has_upper, has_lower, has_digit, has_symbol])

    suggestions = []
    if not has_upper:
        suggestions.append("Add at least one uppercase letter (A-Z).")
    if not has_lower:
        suggestions.append("Add at least one lowercase letter (a-z).")
    if not has_digit:
        suggestions.append("Add at least one number (0-9).")
    if not has_symbol:
        suggestions.append("Add at least one special character (e.g. !@#$%^&*).")

    if criteria_met <= 1:
        strength = "Weak"
    elif criteria_met in (2, 3):
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions

def print_result(password, strength, suggestions):
    print(f"\nPassword entered : {'*' * len(password)}")
    print(f"Strength result  : {strength}")

    if suggestions:
        print("Suggestions to improve it:")
        for tip in suggestions:
            print(f"  - {tip}")
    else:
        print("Great job! This password meets all the security criteria.")

def main():
    print("=" * 50)
    print("   DecodeLabs - Password Strength Checker")
    print("=" * 50)
    print("Type 'quit' at any time to exit.\n")

    while True:
        password = input("Enter a password to check: ")

        if password.lower() == "quit":
            print("\nThanks for using the Password Strength Checker. Goodbye!")
            break

        if password == "":
            print("Please enter a password (or type 'quit' to exit).")
            continue

        strength, suggestions = check_password_strength(password)
        print_result(password, strength, suggestions)
        print("-" * 50)

if __name__ == "__main__":
    main()

