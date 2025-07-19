# unit_converter.py

# Ask user to enter values (comma-separated)
user_input = input("Enter values in inches (comma-separated): ")  # Example: 1, 2.5, 4

# Split the input and convert each to float
try:
    inches = list(map(float, user_input.split(",")))

    # Convert inches to centimeters using lambda and map
    centimeters = list(map(lambda x: round(x * 2.54, 2), inches))

    print("Inches:     ", inches)
    print("Centimeters:", centimeters)

except ValueError:
    print("Invalid input! Please enter numeric values separated by commas.")
