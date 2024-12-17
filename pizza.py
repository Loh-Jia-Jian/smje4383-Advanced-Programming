menu = {"Margherita": 25, "Pepperoni": 30, "BBQ Chicken": 35, "Veggie": 28}

def calculate_total(order_list, menu):
    total_cost = 0
    for order, amount in order_list: 
        if order in menu:
            total_cost += menu[order] * amount 
    return total_cost

  
def display_menu(menu):
    print("Pizza Menu:")
    for pizza, price in menu.items():
        print(f"- {pizza}: RM {price}")

def order_input():
    # Initialize a clean empty order list
    order_list = []

    # Take orders
    while True:
        order = input("Enter the name of the pizza you want to order (or type 'done' to finish): ").title()
        if order == 'Done':
            break
        if order in menu:
            try:
                order_amount = float(input("Enter your total pizza order amount (RM): "))
                order_list.append((order, order_amount))  # Append as a tuple
            except ValueError:
                print("Please enter a valid numeric value for the amount.")
        else:
            print("Sorry, we don't have that pizza.")

    # Check if the customer is a regular customer
    is_regular_customer = input("Are you a regular customer? (yes/no): ").lower() == 'yes'
    return order_list, is_regular_customer


def apply_discount(is_regular_customer, total):
  if total > 100:
    subtotal = total*0.85
    print(f" You get a 15% discount of RM {subtotal:.2f}!")
  else:
    subtotal = total
    print("No discount applied. Thank you for your order!")
  if is_regular_customer == True:
    subtotal = subtotal*0.9
    print(f" You get a 10% discount of RM {subtotal:.2f} as regular customer!")
  else:
    subtotal = subtotal
  return subtotal

display_menu(menu)
order_list, regular_customer = order_input()
total = calculate_total(order_list, menu)
subtotal = apply_discount(regular_customer, total)
print(f"The total price is RM{subtotal}")