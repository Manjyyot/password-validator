import string

def check_password_strength(password: str) -> bool:
    # Initializing criteria flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_space = False
    
    # Immediate check for length
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    
    # Iterative checks with early returns
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True
        elif char.isspace():
            has_space = True
        
        # If all criteria are met and no space is found, return early
        if has_upper and has_lower and has_digit and has_special and not has_space:
            return True
    
    # Provide feedback if any criterion is missing
    if not has_upper:
        print("Password must contain at least one uppercase letter.")
    if not has_lower:
        print("Password must contain at least one lowercase letter.")
    if not has_digit:
        print("Password must contain at least one digit.")
    if not has_special:
        print("Password must contain at least one special character (e.g., @$!%*?&#).")
    if has_space:
        print("Password should not contain spaces.")
    
    return False

if __name__ == "__main__":
    # Input from the user
    password_input = input("Enter your password to check its strength: ")
    
    # Check password strength
    if check_password_strength(password_input):
        print("Password is strong!")
    else:
        print("Password is weak!")