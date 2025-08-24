# BMI Calculator in Python with Height in cm

# Get user input
weight = float(input("Enter your weight (in kilograms) : \n"))
height_cm = float(input("Enter your height (in centimeters) : \n"))

# Convert cm to meters
height_m = height_cm / 100

# Calculate BMI
bmi = weight / (height_m ** 2)

# Print BMI
print(f"\nYour BMI is: \n {bmi:.2f}")

# BMI Category
if bmi < 18.5:
    print("-> Your BMI is less than 18.5kg/m². You are Underweight.")
elif 18.5 <= bmi < 24.9:
    print("-> Your BMI is in between 18.5kg/m² and 24.9kg/m². You have a Normal weight.")
elif 25 <= bmi < 29.9:
    print("-> Your BMI is in between 25kg/m² and 29.9kg/m²2. You are Overweight.")
else:
    print("-> Your BMI is greater than 30kg/m². You are Obese.")

# Height Message
print(f"\nYour Height is: {height_cm} cm")

if height_cm < 150:
    print("-> Your height is less than 150cm.  You are Short in height.")
elif 150 <= height_cm < 180:
    print("-> Your height is in between 150cm and 180cm. You have an Average height.")
else:
    print("-> Your height in greater than 180cm.  You are Tall in height.")

