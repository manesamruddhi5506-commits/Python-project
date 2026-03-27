select_operation=("\n1.Addition\n2.Subtraction\n3.multiplication\n4.division")
print("select your operation:",select_operation)
operation=int(input("select operation:"))
a=int(input("enter first number: "))
b=int(input("enter second number: "))

if operation==1:
   
    print("sum of numbers is:",a+b)

elif operation==2:
   
    print("of numbers is:",a-b)

elif operation==3:
   
    print("of numbers is:",a*b)

elif operation==4:
  

    print("sum of numbers is:",a/b)

else: 
    print ("the number is invalid")