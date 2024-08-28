def add_names():
    names = []  # Initialize an empty list to store names

    while True:
        response = input("Do you want to add a name? (yes/no): ").strip().lower()
        if response == "yes":
            name = input("Enter the name you want to add: ").strip()
            names.append(name)
        elif response == "no":
            print("The names you have added are:")
            for name in names:
                print(name)
            break  # Exit the loop
        else:
            print("Please enter 'yes' or 'no'.")

# Call the function to run the program
add_names()
