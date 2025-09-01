def age(a):
    if(a>0 and a<=12):
        print("Child")
    elif(a>=13 and a<=19):
        print("Teen")
    elif(a>=20 and a<=59):
        print("Adult")
    elif(a>=60):
        print("Senior")
    else:
        print("Invalid age")

a=int(input("Enter the age:"))
age(a)
