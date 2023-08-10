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