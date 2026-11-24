import string
import secrets
import getpass
import re

# Common passwords that are easy to guess
COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "admin123",
    "welcome",
    "iloveyou",
    "abc123"
}


# Function to check password strength
def check_password(password):

    score = 0
    suggestions = []

    print("\n========== PASSWORD ANALYSIS ==========")

    # 1. Check password length
    if len(password) >= 16:
        print("[+] Password length: Excellent")
        score += 2
    elif len(password) >= 12:
        print("[+] Password length: Good")
        score += 1
    else:
        print("[-] Password length: Too short")
        suggestions.append("Use at least 12 characters.")

    # 2. Check uppercase letters
    if re.search(r"[A-Z]", password):
        print("[+] Uppercase letters: Present")
        score += 1
    else:
        print("[-] Uppercase letters: Missing")
        suggestions.append("Add uppercase letters (A-Z).")

    # 3. Check lowercase letters
    if re.search(r"[a-z]", password):
        print("[+] Lowercase letters: Present")
        score += 1
    else:
        print("[-] Lowercase letters: Missing")
        suggestions.append("Add lowercase letters (a-z).")

    # 4. Check numbers
    if re.search(r"[0-9]", password):
        print("[+] Numbers: Present")
        score += 1
    else:
        print("[-] Numbers: Missing")
        suggestions.append("Add numbers (0-9).")

    # 5. Check special characters
    if re.search(r"[^a-zA-Z0-9]", password):
        print("[+] Special characters: Present")
        score += 1
    else:
        print("[-] Special characters: Missing")
        suggestions.append("Add special characters (!, @, #, $, etc.).")

    # 6. Check common passwords
    if password.lower() in COMMON_PASSWORDS:
        print("[-] Common password: Detected")
        score = 0
        suggestions.append("Avoid commonly used passwords.")
    else:
        print("[+] Common password: Not detected")

    # 7. Check repeated characters
    if re.search(r"(.)\1{3,}", password):
        print("[-] Repeated characters: Detected")
        score = max(0, score - 2)
        suggestions.append("Avoid repeating the same character many times.")
    else:
        print("[+] Repeated characters: No major repetition detected")

    # 8. Check predictable patterns
    patterns = [
        "1234", "abcd", "qwerty",
        "9876", "password", "1111"
    ]

    if any(pattern in password.lower() for pattern in patterns):
        print("[-] Predictable pattern: Detected")
        score = max(0, score - 2)
        suggestions.append("Avoid predictable sequences and keyboard patterns.")
    else:
        print("[+] Predictable patterns: Not detected")

    # Final strength result
    print("\n========== FINAL RESULT ==========")

    if score >= 5:
        print("PASSWORD STRENGTH: STRONG")
    elif score >= 3:
        print("PASSWORD STRENGTH: MEDIUM")
    else:
        print("PASSWORD STRENGTH: WEAK")

    print("Security Score:", score, "/ 6")

    # Display recommendations
    if suggestions:
        print("\n========== RECOMMENDATIONS ==========")
        for suggestion in suggestions:
            print("->", suggestion)
    else:
        print("\nGood! Your password passed all these checks.")

    return score


# Function to generate strong passwords
def generate_password(length=20):

    if length < 12:
        raise ValueError("Password length must be at least 12.")

    characters = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + "!@#$%^&*()-_=+"
    )

    # Ensure at least one character from each category
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*()-_=+")
    ]

    # Fill remaining positions
    password += [
        secrets.choice(characters)
        for _ in range(length - 4)
    ]

    # Securely shuffle the characters
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


# Main program
def main():

    print("======================================")
    print("       PASSWORD STRENGTH ANALYZER")
    print("======================================")

    password = getpass.getpass("\nEnter your password: ")

    if not password:
        print("Please enter a password.")
        return

    score = check_password(password)

    print("\n========== PASSWORD GENERATOR ==========")

    choice = input(
        "\nWould you like to generate stronger passwords? (yes/no): "
    ).strip().lower()

    if choice == "yes":
        print("\nSuggested Strong Passwords:")

        for i in range(3):
            print(f"{i + 1}. {generate_password()}")

    print("\nThank you for using Password Strength Analyzer!")


# Run the program
if __name__ == "__main__":
    main()