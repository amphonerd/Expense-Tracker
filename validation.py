from datetime import datetime, date


def get_amount():
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Please enter a number")
        return None

    if amount <= 0:
        print("Amount should be more than 0")
        return None
    return amount


def get_date():
    text = input("Date (DD-MM-YYYY) or press enter for today: ")
    if text == "":
        return date.today()

    try:
        return datetime.strptime(text, "%d-%m-%Y").date()
    except ValueError:
        print("Wrong date format")
        return None


def get_month():
    text = input("Month (YYYY-MM): ")
    try:
        d = datetime.strptime(text, "%Y-%m")
        return d.date()
    except ValueError:
        print("Wrong month format")
        return None
