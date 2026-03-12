inventory = {
    "Laptop":120000,
    "Mouse":250,
    "Keyboard":500,
    "Monitor":25000

}

cart = ["Laptop","Mouse","headphone","Monitor"]

def calculate_total(shopping_cart,price_dict):
    total_sum = 0

    for item in shopping_cart:
        if item in price_dict:
            total_sum =total_sum + price_dict[item]
            print (f"Added {item}:${price_dict[item]}")
        else:
            print(f"Warning: {item} is not in stock!")

    return total_sum





final_bill = calculate_total(cart,inventory)
print(f"----- Your Final Total: ${final_bill}")


