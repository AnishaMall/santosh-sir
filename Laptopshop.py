import os
import datetime

def read_laptop_data(filename):
    laptops = []
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split(',')
            if len(data) != 4:
                print(f"Invalid data: {line}")
                continue
            name, brand, price, quantity = data
            laptops.append({'name': name, 'brand': brand, 'price': max(0, float(price)), 'quantity': max(0, int(quantity))})
    return laptops

def update_laptop_data(filename, laptops):
    try:
        with open(filename, "w") as file:
            for laptop in laptops:
                line = f"{laptop['name']}, {laptop['brand']}, {laptop['price']}, {laptop['quantity']}\n"
                file.write(line)
    except Exception as e:
        print(f"Failed to update laptop data: {e}")
def generate_order_invoice(distributor, laptop_name, brand, quantity, net_amount):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    invoice_filename = f"order_invoice_{timestamp}.txt"
    vat_amount = net_amount * 0.13
    gross_amount = net_amount + vat_amount

    with open(invoice_filename, "w") as file:
        file.write("====================================\n")
        file.write("              LAPTOP SHOP           \n")
        file.write("   Kamalpokhari, Kathmandu          \n")
        file.write("   Phone No: 014412345              \n")
        file.write("====================================\n")
        file.write("             ORDER INVOICE              \n")
        file.write("====================================\n\n")
        file.write(f"Order ID: {timestamp}\n")
        file.write(f"Date & Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Distributor: {distributor}\n")
        file.write(f"\n\nProduct Details:\n")
        file.write(f"Laptop Name: {laptop_name}\n")
        file.write(f"Brand: {brand}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"\n\nPayment Details:\n")
        file.write(f"Net Amount: ${net_amount}\n")
        file.write(f"VAT Amount: ${vat_amount}\n")
        file.write(f"Gross Amount: ${gross_amount}\n")
        file.write("\n====================================\n")
        file.write("          THANK YOU FOR ORDERING!          \n")
        file.write("====================================\n")

    print(f"Order invoice generated: {invoice_filename}")


def generate_customer_invoice(customer, laptop_name, brand, quantity, shipping_cost, total_amount):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    invoice_filename = f"customer_invoice_{timestamp}.txt"

    with open(invoice_filename, "w") as file:
        file.write("====================================\n")
        file.write("              LAPTOP SHOP           \n")
        file.write("   Kamalpokhari, Kathmandu          \n")
        file.write("   Phone No: 014412345              \n")
        file.write("====================================\n")
        file.write("             CUSTOMER INVOICE              \n")
        file.write("====================================\n\n")
        file.write(f"Order ID: {timestamp}\n")
        file.write(f"Date & Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Customer: {customer}\n")
        file.write(f"\n\nProduct Details:\n")
        file.write(f"Laptop Name: {laptop_name}\n")
        file.write(f"Brand: {brand}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"\n\nPayment Details:\n")
        file.write(f"Total Amount (without shipping): ${total_amount}\n")
        file.write(f"Shipping Cost: ${shipping_cost}\n")
        file.write(f"Total Amount (with shipping): ${total_amount + shipping_cost}\n")
        file.write("\n====================================\n")
        file.write("          THANK YOU FOR SHOPPING!          \n")
        file.write("====================================\n")

    print(f"Customer invoice generated: {invoice_filename}")



def get_user_input(prompt, input_type):
    while True:
        try:
            user_input = input_type(input(prompt))
            break
        except ValueError:
            print("Invalid input, please enter the correct data type.")
    return user_input
def find_laptop_index(laptops, laptop_name):
    for index, laptop in enumerate(laptops):
        if laptop['name'].lower() == laptop_name.lower():
            return index
    return -1

# ... rest of the code remains the same ...

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

