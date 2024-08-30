import re


def assess_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Check the length of the password
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Password is too short. Use at least 8 characters.")

    # Check for the presence of lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters to your password.")

    # Check for the presence of uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters to your password.")

    # Check for the presence of numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers to your password.")

    # Check for the presence of special characters
    if re.search(r'[@$!%*?&#]', password):
        score += 1
    else:
        feedback.append("Add special characters to your password (e.g., @, $, !, %).")

    # Assess overall strength
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback


def main():
    # Get the password from the user
    password = input("Enter your password: ").strip()

    # Assess the password strength
    strength, feedback = assess_password_strength(password)

    # Provide feedback to the user
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")


if __name__ == "__main__":
    main()
