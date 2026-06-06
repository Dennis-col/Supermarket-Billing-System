# =================================================================
# Course: Introduction to Programming (IPG101)
# Assignment: Supermarket Billing System
# =================================================================

def main():
    print("==================================================")
    print("    WELCOME TO SMARTBUY SUPERMARKET BILLING SYSTEM  ")
    print("==================================================")

    # Outer loop allows processing multiple customers continuously
    while True:
        # Lists (Arrays) to store product information for the current customer
        product_names = []
        quantities = []
        unit_prices = []
        item_totals = []
        
        subtotal = 0.0

        # Inner loop to collect all items purchased by this single customer
        while True:
            print("\n--- Input Product Details ---")
            
            # Input Statements
            name = input("Enter product name: ").strip()
            
            # Input handling for quantity with a basic safety check
            while True:
                try:
                    qty = int(input(f"Enter quantity for '{name}': "))
                    if qty > 0:
                        break
                    print("Quantity must be greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a whole number.")

            # Input handling for unit price
            while True:
                try:
                    price = float(input(f"Enter price per unit for '{name}' (Le): "))
                    if price > 0:
                        break
                    print("Price must be greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a valid price amount.")

            # Arithmetic Operators (Calculations)
            total_item_price = qty * price
            subtotal += total_item_price

            # Storing items into lists (Arrays)
            product_names.append(name)
            quantities.append(qty)
            unit_prices.append(price)
            item_totals.append(total_item_price)

            # Check if there are more products for this customer
            more_items = input("\nAdd another product for this customer? (yes/no): ").strip().lower()
            if more_items == 'no':
                break

        # Decision Structures (If / Else) for discount rule
        # A 10% discount is applied if the total purchase exceeds Le 500
        if subtotal > 500:
            discount = subtotal * 0.10
        else:
            discount = 0.0

        final_amount = subtotal - discount

        # Displaying a well-formatted printed receipt
        print("\n" + "="*45)
        print("            SMARTBUY SUPERMARKET            ")
        print("              FREETOWN, SIERRA LEONE        ")
        print("="*45)
        print(f"{'Product Name':<18}{'Qty':<6}{'Unit Price':<11}{'Total Price':<10}")
        print("-"*45)
        
        # Loop to display each product from our arrays
        for i in range(len(product_names)):
            print(f"{product_names[i]:<18}{quantities[i]:<6}Le {unit_prices[i]:<8.2f}Le {item_totals[i]:<8.2f}")
            
        print("-"*45)
        print(f"{'Subtotal:':<35}Le {subtotal:.2f}")
        print(f"{'Discount Applied (10%):':<35}Le {discount:.2f}")
        print("="*45)
        print(f"{'FINAL AMOUNT TO PAY:':<35}Le {final_amount:.2f}")
        print("="*45)
        print("         Thank you for shopping with us!        ")
        print("="*45 + "\n")

        # Ask if the cashier wants to process another customer sequence
        next_customer = input("Process bill for the next customer? (yes/no): ").strip().lower()
        if next_customer == 'no':
            print("\nExiting system. Have a great day!")
            break

if __name__ == "__main__":
    main()