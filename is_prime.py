import math 

stack = []

while True:
    input_num = input("Please input a number (or 'q' to quit):  ")

    # check if the user wants to quit
    if input_num == 'q':
        break

    # Check if the user input is an integer
    while not input_num.isdigit():
        input_num = input("Please input an integer:  ")

   
    # check if the number X is divisable by any number under the square root of X
    for n in range(1, int(math.sqrt(int(input_num))) + 1):
        if int(input_num)%n == 0:
            stack.append(n)

    # Append the actual input number to the stack as any nubmer can be divided by its self, if not done the code will produce 
    # errors in certain numbers, IE 9
    stack.append(int(input_num))

    # check the stack length, if more than two the number is not prime
    if len(stack) >=3 :

        print(input_num + " Is not a prime number.")
        print("As it can be divided by :" + str(stack))

    # if the stack length is 2 then it is a prime number
    else:
        print(input_num + " Is a prime number.")
        print("As it can only be divided by :" + str(stack))
        print(" ------ ")
        print(" ------- ")
        print(" -------- ")
        print(" --------- ")
        

    # Reset the stack for the next run
    stack = []