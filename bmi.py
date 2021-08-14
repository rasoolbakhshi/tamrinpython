a=float(input("weight (kg)"))
b=float(input("hieght(m)"))
bmi=a/b**2
if bmi<18.5:
    report="underweight"
if  24.9>= bmi >=18.5:
    report="normal"
if 29.5>=bmi>=25:
    report="obest"
if bmi>35:
    report="extremly obest"
print(report)

