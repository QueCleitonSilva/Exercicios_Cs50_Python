def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Requirement: All vanity plates must start with at least two letters.
    if not s[:2].isalpha():
        return False

    # Requirement: Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if not 2 <= len(s) <= 6:
        return False

    # Requirement: No periods, spaces, or punctuation marks are allowed.
    if any(char in ' .,!@#$%^&*()-_+=~`:;"\'{}[]\\/?' for char in s):
        return False

    # Check if the rest of the plate contains only letters or digits
    if not s[2:].isalnum():
        return False

    # Check if the first digit is not '0'
    if len(s) > 2 and s[2] == '0':
        return False

    # If all requirements are met, return True
    return True


main()
