def days_since_birthday(birthday):
    """Calculate total days passed since birthday, counting only whole years
    (birth year and current year are not counted)"""

    # split "DD-MM-YYYY" into parts and extract the birth year
    parts = birthday.split("-")
    birth_year = int(parts[2])

    current_year = 2026

    total_days = 0

    # loop through each complete year between birth year and current year
    for year in range(birth_year + 1, current_year):
        # leap year rules: divisible by 400, or divisible by 4 but not 100
        if year % 400 == 0:
            total_days += 366
        elif year % 100 == 0:
            total_days += 365
        elif year % 4 == 0:
            total_days += 366
        else:
            total_days += 365

    return total_days


birthday = "15-03-2000"
result = days_since_birthday(birthday)
print(f"Days since {birthday} (whole years only): {result}")
