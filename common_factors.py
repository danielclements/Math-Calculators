import math 

#Find the common multiple between two numbers, and find the highest common multiple 

one_factors = set()
two_factors = set()

# Ask the user for a number
number_1 = input("Please input first number: ")
#Checks that the user input is an integer 
while not number_1.isdigit():
    #if user input is not a integer, ask for a new input
    number_1 = input("Please input an integer for the first number:")

# repeats above code for number_2
number_2 = input("Please input Second number: ")
while not number_2.isdigit():
    number_2 = input("Please input an integer for the first number:")

#calculates the factors of a number and appends to a list depending on input source
def calc_factors(number):
    convert_to_int = int(number)
    for n in range(1, convert_to_int + 1):
        if convert_to_int%n == 0:
            if number == number_2:
                two_factors.add(n)
            else:
                one_factors.add(n) 
calc_factors(number_1)
calc_factors(number_2)

# Checks for items in each set that match, then they get sorted from lowest to highest
common_factors = one_factors.intersection(two_factors)
#Gets the highest number in the set
HCF = max(common_factors)

print("The common factors between {} and {} are: ".format(number_1, number_2) + str(common_factors))
print("the Highest Common Multiple is : " + str(HCF))