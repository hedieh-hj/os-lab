
i=1
while True:
    if i==1:
        weight=float(input("enter with Kilogram scale : "))
        height=float(input("enter with Meter scale : "))

        bmi=float((weight)/(height**2))

        if bmi<18.5:
            print("Underweight")

        if bmi>=18.5 and bmi<=24.9:
            print("Normal")

        if bmi>=25 and bmi<=29.9:
            print("Overweight")
        
        if bmi>=30 and bmi<=34.9 :
            print("Obese")

        if bmi>=35:
            print("Extremely obese")

        i=int(input("if you want try it again press 1 : "))
    else:
        print("Good bye !")
        input()
