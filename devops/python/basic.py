num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
    
print("Select operation: \n1. Add \n2. Subtract \n3. Multiply \n4. Divide")
choice = input("Enter choice(1/2/3/4): ")

if choice == '1':
    result = num1 + num2
    print("The result of addition is:", result)
elif choice == '2':
    result = num1 - num2
    print("The result of subtraction is:", result)
elif choice == '3':
    result = num1 * num2
    print("The result of multiplication is:", result)
elif choice == '4':
    if num2 == 0:
        print("Error! Division by zero.")
    else:
        result = num1 / num2
        print("The result of division is: ", result)
else:
    print("Invalid input! Please select a valid operation.")