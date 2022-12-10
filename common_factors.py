import math 

one_factors = []
two_factors = []
common_factors = []

# Ask the user for a number
number_1 = input("Please input first number: ")
#Checks that the user input is an integer 
while not number_1.isdigit():
    #if user input is not a integer, ask for a new input
    number_1 = input("Please input an integer for the first number:")

# # repeats above code fort number_2
# number_2 = input("Please input Second number: ")
# while not number_2.isdigit():
    
#     number_2 = input("Please input an integer for the first number:")


def calc_factors(number):
    convert_to_int = int(number)
    for n in range(1, convert_to_int + 1):
        if convert_to_int%n == 0:
            one_factors.append(n)
    
    print(one_factors)

calc_factors(number_1)