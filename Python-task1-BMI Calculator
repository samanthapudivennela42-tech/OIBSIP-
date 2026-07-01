print("=== BMI Calculator ===")

while True:
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than 0.")
            continue

        bmi = weight / (height * height)

        print(f"\nYour BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal Weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obesity")

        choice = input("\nDo you want to calculate again? (yes/no): ").lower()

        if choice != "yes":
            print("Thank you for using the BMI Calculator!")
            break

    except ValueError:
        print("Please enter valid numeric values.")
