fridge_content = {}

def add_product(key, value=0):
    if key in fridge_content:
        fridge_content[key] += value
        print(f'{value} of {key} has been added to the fridge.')
        print(fridge_content)
    else:
        fridge_content[key] = value
        print(f'{value} of {key} has been added to the fridge.')
        print(fridge_content)

def remove_product(name):
    if name in fridge_content:
        del fridge_content[name]
        print(f'Item {name} has been removed from the fridge')
        print(f'Fridge now has: {fridge_content}')
    else:
        print('Item has not been found in the fridge, maybe you have already removed it from the fridge')

def check_product(name):
    if name in fridge_content:
        print(f'{name} is in the fridge')
        print(f'There is {fridge_content[name]} of {name} in the fridge')
    else:
        print(f'Product {name} is not in the fridge')

def print_content_fridge():
    print(fridge_content)

# Bonus tasks

recipe = 0

def check_recipe():
    pass

def input_recipe():
    pass

def recipe_fail():
    pass

# Main function

def main():
    while True:
        print("Yellow Submerged Fridge")
        print("0: Exit")
        print("1: Add to the fridge")
        print("2: Remove from the fridge")
        print("3: Add a task")
        print('4: Mark task done/undone')
        print("5: Remove a task")
        choice = input("Choice: ")
        if choice == "0":
            break
        if choice == '1':
            key = input('What product would you like to add?: ')
            value = float(input('Amount of product you want to add: '))
            add_product(key, value)
        if choice == '2':
            name = input('What product would you like to remove?: ')
            remove_product(name)
main()

# check test for the fridge

add_product('milk', 1.5)
add_product('milk', 2.3)
add_product('tomato', 7.58)
add_product('eggs', 50)
check_product('milk')
remove_product('milk')
print_content_fridge()
print(recipe)
check_recipe()
input_recipe()
recipe_fail()