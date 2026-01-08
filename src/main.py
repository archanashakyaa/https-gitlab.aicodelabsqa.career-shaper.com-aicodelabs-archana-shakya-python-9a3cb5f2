def calculate_seasonal_price(product_name, date):
    products = {
        "Emerald": 125,
        "Pearl": 187,
        "Gold": 262,
        "Sapphire": 112,
        "Rose": 75,
    }

    if product_name not in products:
        print("Welcome to seasonal collections.")
        print("Not available in our collection.")
        print("Please try another product.")
        return

    if not isinstance(date, str) or len(date) != 5 or date[2] != "/":
        print("Welcome to seasonal collections.")
        print("Enter a valid date.")
        return

    month_part = date[:2]
    day_part = date[3:]
    if (not month_part.isdigit()) or (not day_part.isdigit()):
        print("Welcome to seasonal collections.")
        print("Enter a valid date.")
        return

    month = int(month_part)
    day = int(day_part)
    if month < 1 or month > 12 or day < 1 or day > 31:
        print("Welcome to seasonal collections.")
        print("Enter a valid date.")
        return

    base_price = products[product_name]
    if month in (10, 11, 12, 1, 2, 3):
        final_price = base_price * 1.5
    else:
        final_price = base_price * 1.25

    print("Welcome to seasonal collections.")
    print(f"The product price is: ${final_price}")


def main():
    line1 = input().strip()
    if "," in line1:
        product_name, date = [part.strip() for part in line1.split(",", 1)]
    else:
        product_name = line1
        date = input().strip()

    calculate_seasonal_price(product_name, date)


if __name__ == "__main__":
    main()
