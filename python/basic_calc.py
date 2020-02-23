def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    # remove .0 if answer is same.
    if x/y == int(x/y):
        return int(x/y)
    else:
        return x/y

def power(x,y):
    return x**y

#################################################

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
func = input("Select from an option above: ")

if func == ("1" or "add"):
    print(num1, "+", num2, "=", add(num1,num2))

elif func == ("2" or "subtract"):
    print(num1, "-", num2, "=", subtract(num1,num2))

elif func == ("3" or "multiply"):
    print(num1, "*", num2, "=", multiply(num1,num2))

elif func == ("4" or "divide"):
    print(num1, "/", num2, "=", divide(num1,num2))

elif func == ("5" or f"power"):
    print(num1, "**", num2, "=", power(num1,num2))

else:
    print("Invalid input from user.")
