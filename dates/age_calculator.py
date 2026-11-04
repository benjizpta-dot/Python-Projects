from datetime import datetime
from dateutil.relativedelta import relativedelta


def main():
    today = datetime.now().date()
    try:
        date_of_birth = datetime.strptime(
            input("Enter your date of birth (mm-dd-yyyy): "), "%m-%d-%Y"
        ).date()
    except ValueError:
        print("Please enter a valid date in mm-dd-yyyy format.")
        return
    if date_of_birth > today:
        print("Date of birth cannot be in the future.")
        return
    age = relativedelta(today, date_of_birth)
    print(f"You are {age.years} years, {age.months} months, and {age.days} days old")
    print(f"This year is: {today.year}")
    print(f"Your birth year is: {date_of_birth.year}")
    print(f"Your birth month is: {date_of_birth.month}")
    print(f"This month is: {today.month}")


if __name__ == "__main__":
    main()
