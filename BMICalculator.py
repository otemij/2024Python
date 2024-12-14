print("This program is a BMI calculator")

weight = float(input("Enter in your weight (kg): "))
height = float(input("Enter in your height ( metres): "))
bmi = weight/height

if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9 and bmi >= 18.5:
    print("Normal Weight")
elif bmi >= 25 and bmi <= 29.9:
    print("Overweight")
elif bmi >= 30:
    print("Obesity. Seek medical attention")
