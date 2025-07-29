import random

def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list[int]:
    """
    Generates a sorted list of unique random numbers within the specified range.

    Args:
        min_value (int): Minimum possible number (not less than 1).
        max_value (int): Maximum possible number (not greater than 1000).
        quantity (int): Number of unique values to generate.

    Returns:
        list[int]: Sorted list of unique random numbers, or an empty list if parameters are invalid.
    """

    # Parameters validation
    if not all(isinstance(x, int) for x in [min_value, max_value, quantity]):
        print("Error: 'min_value', 'max_value' and 'quantity' must be integers")
        return []

    if min_value < 1 or max_value > 1000 or min_value >= max_value:
        print("Error: 'min_value' ≥ 1, 'max_value' ≤ 1000, and 'min_value' < 'max_value'")
        return []

    if not (0 < quantity <= (max_value - min_value + 1)):
        print("Error: 'quantity' must be > 0 and not exceed the number of available unique values.")
        return []
    
    numbers = random.sample(range(min_value, max_value + 1), quantity)
    return sorted(numbers)
    

if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Your lottery numbers:", lottery_numbers)