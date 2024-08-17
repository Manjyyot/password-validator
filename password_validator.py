import string

def check_password_strength(password: str) -> bool:
    # Validation flags
    contains_upper = False
    contains_lower = False
    contains_number = False
    contains_special = False
    contains_space = False
    
    # Password length validation
    if len(password) < 8:
        print("The password must be 8 characters or longer.")
        return False
    
    # validate if entered password satisfies criteria
    for character in password:
        if character.isupper():
            contains_upper = True
        elif character.islower():
            contains_lower = True
        elif character.isdigit():
            contains_number = True
        elif character in string.punctuation:
            contains_special = True
        elif character.isspace():
            contains_space = True
        
        # Ensure all conditions are satisfied
        if contains_upper and contains_lower and contains_number and contains_special and not contains_space:
            return True
    
    # Provide specific feedback for missing criteria
    if not contains_upper:
        print("Include at least one uppercase letter.")
    if not contains_lower:
        print("Include at least one lowercase letter.")
    if not contains_number:
        print("Include at least one digit.")
    if not contains_special:
        print("Include at least one special character.")
    if contains_space:
        print("Avoid using spaces in your password.")
    
    return False

if __name__ == "__main__":
    # Continue until a valid password is provided
    while True:
        user_input = input("Enter a password to validate its strength: ")
        
        # Validate the password strength
        if check_password_strength(user_input):
            print("Your password is strong!")
            break  
        else:
            print("Password is too weak. Please try again.\n")
