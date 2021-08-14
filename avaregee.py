a=input("enter name:")
b=input("enter faily:")
corse1=int (input("number of corse1:"))
corse2=int (input("number of corse2:"))
corse3=int (input("number of corse 3:"))
avarage=(corse1+corse2+corse3)/3
if avarage>=17:
    result="Great"
if avarage >=12 and avarage <17:
    result="normal"
if avarage<12:
    result="fail"
print ("student",a,b,"with avarege",avarage,"is",result)

