weight =float (input("input your weight in kg"))
height =float (input("input your height in m"))
BMI= weight/(height**2)
if BMI<18.5:
    print("Underweight")
elif 18.5<BMI<24.9:
    print("Normal")
elif 25<BMI<29.9:
    print("Overweight")
elif 30<BMI<34.9:
    print("Obses")
else:
    print("Extremely obses")
