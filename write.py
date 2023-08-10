import datetime

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
