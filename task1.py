from datetime import datetime

def get_days_from_today(date_str: str) -> int | None:
    """
    Calculate the number of days between today and the given date string.

    Args:
        date_str (str): Date in 'YYYY-MM-DD' format.

    Returns:
        int | None: Number of days difference, or None if input is invalid.
    """
    try:
        input_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError as e:
        print(f"Invalid date '{date_str}': {e}")
        return None

    today = datetime.today()
    date_difference = (today - input_date).days
    print(f"Days from today: {date_difference}")
    return date_difference

if __name__ == "__main__":
    get_days_from_today('2021-10-09')
