import math
a = float (input())
b=float(input("second number:"))
op= input()
if op =="+":
    result =a+b
if op =="-":
    result = a-b
if op=="*":
     result=a*b
if op=="/" :
    if b!=0:
        result=a/b
    if b == 0:
        result="error"
if op=="sqrt(a)":
    if a>=0:
        result = math.sqrt (a)
    else : 
        result= "error"
if op=="sin(a)":
    result =math.sin (a) 
if op=="cot(a)":
    if math.sin(a)!=0:
        result=math.cot(a)
    else :
        result="error"
if op=="tan(a)":
    if math.cos(a)!=0:
        result=math.tan(a)
if op=="factorial(a)":
    if a>0 :
        result=math.factorial(a)
    if a==0:
        result=1
    if a<0:
        result="error"


    

print(result)
    