def ADD(x1,x2):
    y= x1+x2
    return y

# This function subtracts two numbers
def SUBTRACT(x1,x2):
    y= x1-x2
    return y
# This function multiplies two numbers
def MULTIPLY(x1,x2):
    y= x1*x2
    return y

# This function divides two numbers
def DIVIDE(x1,x2):
    y=x1/x2
    return y

print("SIMPLE CALCULATOR")
print("Select the operation to be performed !.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Quit")
while True:
    # take input from the user
    operation = input("Enter the choice(1/2/3/4/5): ")

    # check if choice is one of the four options
    if operation in ('1', '2', '3', '4'):
        try:
            value1 = float(input("Enter first number: "))
            value2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if operation == '1':
            print(value1, "+", value2, "=", ADD(value1, value2))

        elif operation == '2':
            print(value1, "-", value2, "=", SUBTRACT(value1, value2))

        elif operation == '3':
            print(value1, "*", value2, "=", MULTIPLY(value1, value2))

        elif operation == '4':
            print(value1, "/", value2, "=", DIVIDE(value1, value2))
        
    elif operation == '5':
            print("Exitting from the calculator")
       
    else:
        print("Invalid Choice !")
