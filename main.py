from operations import find_laptop_index, get_user_input
from read import read_laptop_data
from write import update_laptop_data, generate_order_invoice, generate_customer_invoice
import os

def main():
    data_file = "laptop_data.txt"

    if not os.path.exists(data_file):
        print(f"Error: {data_file} not found.")
        return

    try:
        laptops = read_laptop_data(data_file)
    except Exception as e:
        print(f"Failed to read laptop data: {e}")
        return

    while True:
        print("\nAvailable Laptops:")
        for laptop in laptops:
            print(f"{laptop['name']} - {laptop['brand']} - ${laptop['price']} - {laptop['quantity']} in stock")

        action = input("\nChoose an action (order, sell, exit): ").lower()

        if action == 'order':
           
            distributor = input("Enter distributor name: ")
            laptop_name = input("Enter laptop name: ").lower()  # Convert to lowercase for consistency
            brand = input("Enter laptop brand: ")
            quantity = max(0, get_user_input("Enter quantity to order: ", int))  # Ensure non-negative
            net_amount = max(0, get_user_input("Enter net amount (total amount without VAT): ", float))  # Ensure non-negative

            index = find_laptop_index(laptops, laptop_name)
            if index == -1:
                laptops.append({'name': laptop_name, 'brand': brand, 'price': net_amount / quantity if quantity != 0 else 0, 'quantity': quantity})
            else:
                laptops[index]['quantity'] += quantity

            generate_order_invoice(distributor, laptop_name, brand, quantity, net_amount)
            update_laptop_data(data_file, laptops)

        elif action == 'sell':
           
            customer = input("Enter customer name: ")
            laptop_name = input("Enter laptop name: ").lower()  # Convert to lowercase for consistency
            quantity = max(0, get_user_input("Enter quantity to sell: ", int))  # Ensure non-negative

            index = find_laptop_index(laptops, laptop_name)
            if index == -1:
                print("Error: Laptop not found.")
            elif laptops[index]['quantity'] < quantity:
                print("Error: Insufficient stock.")
            else:
                laptops[index]['quantity'] -= quantity
                shipping_cost = max(0, get_user_input("Enter shipping cost: ", float))  # Ensure non-negative
                total_amount = laptops[index]['price'] * quantity

                generate_customer_invoice(customer, laptop_name, laptops[index]['brand'], quantity, shipping_cost, total_amount)
                update_laptop_data(data_file, laptops)
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please choose 'order', 'sell', or 'exit'.")

if __name__ == "__main__":
    main()
