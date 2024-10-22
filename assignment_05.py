#Assignment 5
menu_option = ''

while menu_option != 'q':
    print ('''
           Bakery information:
           a: Learn about baking cakes
           b: Deliver bakery items
           q: Exit
           ''')
    
    menu_option = input("Enter a letter for more info about working in the bakery: ")
    if menu_option == 'a':
        print('Baking a cake requires careful timing and technique. Make sure to follow the recipe.')
    elif menu_option == 'b':
        van_driver = input('Are you comfortable delivering bakery items in our van? Enter y or n: ')
        if van_driver == 'y':
            print("Amazing! We would love to have you help deliver bakery items!")
        else:
            print("No problem! We won't ask you to drive!")