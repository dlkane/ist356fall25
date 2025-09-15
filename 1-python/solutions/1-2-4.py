#Challenge 1-2-4¶
'''
Write a program to create a shopping list.

loop until "quit" is entered. input a grocery item input a quantity save the item as the key in the dictionary 
and quantity as the value if the item is in the dictionary already, add the quantity to the existing value.

'''

items = {}

while True:
    item = input("Enter an item: ")
    if item == 'quit':
        print("Quitting...")
        break
    qty = int(input("Enter a quantity: "))
    if item in items.keys():
        items[item] = items[item] + qty

        items[item] = qty
        print('ITEMS:', items)