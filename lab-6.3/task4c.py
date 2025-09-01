def sum(a):
    s=0
    for i in range(1,a+1):
        s+=i
    return s

a=int(input("Enter a number:"))
print(sum(a))
