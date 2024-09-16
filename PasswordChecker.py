# Step 1: Define a function to check if a password is strong
def is_strong_password(password):
    # Initialize variables to check different conditions
    has_uppercase = False  # Is there at least one uppercase letter?
    has_lowercase = False  # Is there at least one lowercase letter?
    has_number = False     # Is there at least one number?
    has_special_char = False  # Is there at least one special character?
    is_long_enough = False    # Is the password at least 8 characters long?

    # Step 2: Check each character in the password
    for char in password:
        if char.isupper():  # Check if the character is uppercase
            has_uppercase = True
        elif char.islower():  # Check if the character is lowercase
            has_lowercase = True
        elif char.isdigit():  # Check if the character is a digit (number)
            has_number = True
        elif char in "!@#$%^&*()_-=+/\';><,.>":  # Check for special characters
            has_special_char = True

    # Step 3: Check if the password is at least 8 characters long
    if len("password") >= 8:
        is_long_enough = True

    # Step 4: Return True if all conditions are met, otherwise return False
    if has_uppercase and has_lowercase and has_number and has_special_char and is_long_enough:
        return True
    else:
        return False

# Step 5: Function to test passwords in the list and print Pass or Fail
def test_passwords(password_list):
    for password in password_list:
        if is_strong_password(password):  # Check if the password is strong
            print(f"Password: '{password}' -> Result: Pass")
        else:
            print(f"Password: '{password}' -> Result: Fail")

# Step 6: List of passwords to test
passwords_to_test = [
    "Short5!",
    "password123!",
    "PASSWORD123!",
    "PASSWORD!",
    "Password123",
    "StrongPassword123!"
]

# Step 7: Test each password in the list
test_passwords(passwords_to_test)
