#Challenge 1-2-3¶
'''
Write a sentinel controlled loop to input a color until "quit" is entered. add each color to a list 
only when the color is not already in the list print the list each time in the loop.
'''

list = []
while True:
    color = input("Enter a color: ")
    if color == 'quit':
        break
    if color in list:
        print("You already entered that color")
    else:
        list.append(color)
        print(list)
