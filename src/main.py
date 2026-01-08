# src/main.py

def calculate_seasonal_price(product_name, date):
    """
    Calculate seasonal price based on product and date.
    
    Args:
        product_name (str): Name of the product
        date (str): Date in mm/dd format
        
    Returns:
        None: Prints price message or error message
    """
    # Product database with base prices
    products = {
        "Emerald": 125,
        "Pearl": 187,
        "Gold": 262,
        "Sapphire": 112,
        "Rose": 75
    }
    
    # Validate product name
    if product_name not in products:
        print("Welcome to seasonal collections.")
        print("Not available in our collection. Please try another product.")
        return
    
    # Parse and validate date
    try:
        parts = date.split('/')
        if len(parts) != 2:
            print("Welcome to seasonal collections.")
            print("Enter a valid date.")
            return
        
        month = int(parts[0])
        day = int(parts[1])
        
        # Validate month and day ranges
        if month < 1 or month > 12 or day < 1 or day > 31:
            print("Welcome to seasonal collections.")
            print("Enter a valid date.")
            return
            
    except (ValueError, IndexError):
        print("Welcome to seasonal collections.")
        print("Enter a valid date.")
        return
    
    # Get base price
    base_price = products[product_name]
    
    # Determine season and calculate price
    # Peak season: Oct-Mar (months 10, 11, 12, 1, 2, 3) → 50% profit (×1.5)
    # Off-season: Apr-Sep (months 4, 5, 6, 7, 8, 9) → 25% profit (×1.25)
    
    peak_months = [10, 11, 12, 1, 2, 3]
    
    if month in peak_months:
        final_price = base_price * 1.5
    else:
        final_price = base_price * 1.25
    
    print("Welcome to seasonal collections.")
    print(f"The product price is: ${final_price}")


def main():
    """Main function to demonstrate the calculator."""
    print("=== Seasonal Price Calculator ===\n")
    
    # Example usage
    test_cases = [
        ("Emerald", "01/15"),
        ("Pearl", "07/20"),
        ("Sapphire", "04/10"),
        ("Diamond", "01/15"),
        ("Rose", "13/32")
    ]
    
    for product, date in test_cases:
        print(f"Input: {product}, {date}")
        result = calculate_seasonal_price(product, date)
        print(result)
        print("-" * 50)


if __name__ == "__main__":
    main()
