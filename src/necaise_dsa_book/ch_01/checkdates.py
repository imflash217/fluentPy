## Listing 1.1
## Extracts the collection of birth dates from the user and determines
## if each individual is at least 21 years of age

from date import Date


def prompt_and_extract_date():
    """Prompts for and extracts the Gregorian date components.
    Returns:
        Date or None (after the user has finished entering the date)
    """
    print(f"Enter a date:\n")
    month = int(input(f"month (0 to quit): "))
    if month == 0:
        return None
    else:
        day = int(input("day: "))
        year = int(input("year: "))
        return Date(month, day, year)


def main():
    ## Date before which a person must have been born to be 21 or older
    born_before = Date(6, 1, 1988)

    ## Extract birth dates from the user and determine if 21 or older
    date = prompt_and_extract_date()
    while date is not None:
        if date <= born_before:
            print(f"Is at least 21 years of age: {date}")
        date = prompt_and_extract_date()


if __name__ == "__main__":
    main()
