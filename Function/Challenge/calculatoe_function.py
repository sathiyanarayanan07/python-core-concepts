

def apply_discount(price , discount_percentage):
  

    discount_amount = (price*discount_percentage/100)
    final_price = price - discount_amount
    return final_price

total_cost = apply_discount(200,10)
print(f"The final price after discount is:${total_cost}")

