def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to be applied.
    
    Returns:
    float: The final price after applying the discount if it's 20% or higher,
           otherwise returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"The final price after a {discount_percent}% discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The price remains: {original_price:.2f}")





