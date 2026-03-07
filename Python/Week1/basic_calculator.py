print("Simple Python Calculator")
print("------------------------")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Floor Division")
print("6.Modulus")
print("7.Power")

choice = input("Choose operation (1/2/3/4/5/6/7): ")

if choice == '1':
    print("Result:", num1 + num2)

elif choice == '2':
    print("Result:", num1 - num2)

elif choice == '3':
    print("Result:", num1 * num2)

elif choice == '4':
    if num2 == 0:
        print("Error: Division by zero is not allowed")
    else:
        print("Result:", num1 / num2)
    
elif choice == '5':
    if num2 == 0:
        print("Error: Division by zero is not allowed")
    else:
        print("Result:", num1 // num2)

elif choice == '6':
    if num2 == 0:
        print("Error: Division by zero is not allowed")
    else:
        print("Result:", num1 % num2)
    
elif choice == '7':
    print("Result:",num1**num2)

else:
    print("Invalid operation")
