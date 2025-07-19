from functions import add, subtract, multiply, divide

def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Choose operation: add / subtract / multiply / divide")
        choice = input("Operation: ").lower()

        if choice == "add":
            print("Result:", add(a, b))
        elif choice == "subtract":
            print("Result:", subtract(a, b))
        elif choice == "multiply":
            print("Result:", multiply(a, b))
        elif choice == "divide":
            print("Result:", divide(a, b))
        else:
            print("Invalid operation selected.")

    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
