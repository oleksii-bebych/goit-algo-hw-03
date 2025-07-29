import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalizes the phone number to international format for SMS broadcasting.

    Removes all symbols except digits and '+' at the beginning. If the international
    code is absent, adds Ukraine code '+38'. Validates that the final number is in
    the correct '+380XXXXXXXXX' format.

    Args:
        phone_number (str): Phone number in arbitrary format.

    Returns:
        str: Normalized phone number in format '+380XXXXXXXXX' or empty string if invalid.
    """
    phone_number = phone_number.strip()

    # If number starts with '+', retain it and clean the rest
    if phone_number.startswith('+'):
        digits = '+' + re.sub(r'\D', '', phone_number[1:])
    else:
        digits_only = re.sub(r'\D', '', phone_number)
        if digits_only.startswith('380'):
            digits = '+' + digits_only
        elif digits_only.startswith('0'):
            digits = '+38' + digits_only
        else:
            digits = '+380' + digits_only

    # Validate that the final number matches '+380XXXXXXXXX'
    if re.fullmatch(r'\+380\d{9}', digits):
        return digits
    else:
        print(f"Warning: Invalid phone number format: {digits}")
        return ''


if __name__ == "__main__":
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Normalized phone number for SMS broadcasting:", sanitized_numbers)