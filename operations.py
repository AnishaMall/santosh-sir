import datetime

def get_user_input(prompt, input_type):
    # ... your existing code ...
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