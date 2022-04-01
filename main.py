from numpy import *
import funcy

from week0 import cloud, ChristmasTree, numpad, swap
from week1 import dictionaries, factorials, fibonacci, fibonacci2
from week2 import Factorial_with_call, Palindrome, CubeRoot, FourthRoot


ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"
def colorTest():
  print("ID  Color")
  for n in range(900):
    COLOR = u"\u001B["+str(n)+"m\u001B[2D"
    print(str(n)+" - "+COLOR)
"""
======================================================================
                        EFFICIENT MENU
======================================================================

"""

# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders



# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    # ["Stringy", "stringy.py"],
    # ["Listy", "listy.py"],
    # ["Loopy", loopy.main],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
math_sub_menu = [
    ["Factorials", factorials.tester2],
    ["Fibonacci", fibonacci.driver],
    ["Fibonacci 2 - by Connor", fibonacci2.tester],
    ["Swap", swap.driver],
    ["Factorials using __call__", Factorial_with_call.driver],
    ["Cube Root using Imperative and OOP", CubeRoot.driver],
    ["Fourt Root - by Connor", FourthRoot.tester],
]

patterns_sub_menu = [
    ["Christmas Tree", ChristmasTree.driver],
    ["Clouds", cloud.driver],
    ["Numpad", numpad.driver],
]

data_sub_menu = [
    ["Dictionaries", dictionaries.tester1],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", math_submenu])
    menu_list.append(["Patterns", patterns_submenu])
    menu_list.append(["Data", data_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def math_submenu():
    title = "Math Submenu" + banner
    buildMenu(title, math_sub_menu)

def patterns_submenu():
    title = "Patterns Submenu" + banner
    buildMenu(title, patterns_sub_menu)
  
def data_submenu():
    title = "Data Submenu" + banner
    buildMenu(title, data_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice ==[ ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()

    
# """
# ======================================================================
#                              MENU 1
# ======================================================================
# """

# # Menu options as a dictionary
# menu1_options = {
#     1: 'Color Test',
#     2: 'Trimester 2 Deliverables',
#     3: 'Lists and Loops',
#     4: 'Patterns',
#     5: 'Exit',
# }

# # Print menu options from dictionary key/value pair
# def print_menu1():
#     print(" " * 9999)
#     for optionID in menu1_options.keys():
#         print(optionID, '--', menu1_options[optionID] )
#     runOptions()


# # call functions based on input choice
# def runOptions():
#     # infinite loop to accept/process user menu choice
#     while True:
#         try:
#             option = int(input('Enter your choice 1-4: '))
#             if option == 1:
#               colorTest()
#             elif option == 2:
#                 print_menu3()
#             elif option == 3:
#                 print_menu4()
#             elif option == 4:
#                 print_menu2()
#             # Exit menu    
#             elif option == 5:  
#                 print('GNIGHT GIRL... ILL SEEYA TOMORROW')
#                 exit() # exit out of the (infinite) while loop
#             else:
#                 print('Invalid option, just like ur identity tbh. Please enter a number between 1 and 5.')
#         except ValueError:
#             print('QUIT HORSIN AROUND. Please enter an integer input.')





# """
# ======================================================================
#                          MENU 2
# ======================================================================
# """
# # Menu options as a dictionary
# menu2_options = {
#     1: 'Christmas Tree',
#     2: 'Clouds',
#     3: 'Back',
#     4: 'Exit',
# }

# # Print menu options from dictionary key/value pair
# def print_menu2():
#     print(" " * 9999)
#     print(ANSI_CLEAR_SCREEN)
#     for optionID in menu2_options.keys():
#         print(optionID, '--', menu2_options[optionID] )
#     runOptions2()

# # call functions based on input choice
# def runOptions2():
#     # infinite loop to accept/process user menu choice
#     while True:
#         try:
#             option = int(input('Enter your choice 1-4: '))
#             if option == 1:
#                 ChristmasTree.christmasTree()
#             elif option == 2:
#                 cloud()
#             elif option == 3:
#                 print_menu1()
#             # Exit menu    
#             elif option == 4:  
#                 print('Goodbye!')
#                 exit() # exit out of the (infinite) while loop
#             else:
#                 print('Invalid option. Please enter a number between 1 and 4.')
#         except ValueError:
#             print('Invalid input. Please enter an integer input.')
          
# """
# ======================================================================
#                          MENU 3
# ======================================================================
# """
# # Menu options as a dictionary
# menu3_options = {
#     1: 'Swap',
#     2: 'Numpad',
#     3: 'Back',
#     4: 'Exit',
# }

# # Print menu options from dictionary key/value pair
# def print_menu3():
#     print(" " * 9999)
#     print(ANSI_CLEAR_SCREEN)
#     print(" < TRI 2 DELIVERABLES >")
#     for optionID in menu3_options.keys():
#         print(optionID, '--', menu3_options[optionID] )
#     runOptions3()


    


  
# # call functions based on input choice
# def runOptions3():
#     # infinite loop to accept/process user menu choice
#     while True:
#         try:
#             option = int(input('Enter your choice 1-4: '))
#             if option == 1:
#                 try:
#                   a=int(input("Value 1: "))
#                   b=int(input("Value 2: "))
#                 except:
#                   print("Invalid input; please input a number")
#                 print(swap.swap(a, b))
#             elif option == 2:
#                 numpad.numpad()
#             elif option == 3:
#                 print_menu1()
#             # Exit menu    
#             elif option == 4:  
#                 print('GNIGHT GIRL... ILL SEEYA TOMORROW')
#                 exit() # exit out of the (infinite) while loop
#             else:
#                 print('Invalid option. Please enter a number between 1 and 4.')
#         except ValueError:
#             print('Invalid input. Please enter an integer input.')

# """
# ======================================================================
#                          MENU 4
# ======================================================================
# """
# # Menu options as a dictionary
# menu4_options = {
#     1: 'Databases',
#     2: 'Fibonacci Sequence',
#     3: 'Factorials',
#     4: 'Back',
#     5: 'Exit',
# }

# # Print menu options from dictionary key/value pair
# def print_menu4():
#     print(" " * 9999)
#     print(ANSI_CLEAR_SCREEN)
#     print(" < Lists and Dictionaries >")
#     for optionID in menu4_options.keys():
#         print(optionID, '--', menu4_options[optionID] )
#     runOptions4()


  
# # call functions based on input choice
# def runOptions4():
#     # infinite loop to accept/process user menu choice
#     while True:
#         try:
#             option = int(input('Enter your choice 1-4: '))
#             if option == 1:
#                 dictionaries.tester1()
#             elif option == 2:
#                 a = int(input("Iterations: "))
#                 fibonacci.Fibonacci_Sequence(a, 0)
#             elif option == 3:
#                 factorials.tester2()
#             elif option == 4:
#                 print_menu1()
#             # Exit menu    
#             elif option == 5:  
#                 print('GNIGHT GIRL... ILL SEEYA TOMORROW')
#                 exit() # exit out of the (infinite) while loop
#             else:
#                 print('Invalid option. Please enter a number between 1 and 4.')
#         except ValueError:
#             print('Invalid input. Please enter an integer input.')
