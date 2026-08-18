age=int(input("enter your age:")) #specify it is int otherwise it wouldn't sep from string 
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")
#multiple conditions
day=int(input("enter no:"))
if day==1:
    print("monday")
elif day==2:     
    print("tuesday")
else:
    print("invalid input")
#multiple
a=int(input("enter first no;"))
b=int(input("enter second no;"))
print("1.Addition\n2.subtraction\n3.multiplication\n4.division")
choice=int(input("enter choice"))
if choice==1:
    print(f"{a}+{b}={a+b}")
elif choice==2:
    print(f"{a}-{b}={a-b}")
elif choice==3:
    print(f"{a}/{b}={a/b}")
elif choice==4:
    print(f"{a}*{b}={a*b}")
else:
    print("invalid input")
#match
a=int(input("enter first no;"))
b=int(input("enter second no;"))
print("1.Addition\n2.subtraction\n3.multiplication\n4.division")
choice=int(input("enter choice"))
match choice:
    case 1:
         print(f"{a}+{b}={a+b}")
    case 2:
        print(f"{a}-{b}={a-b}")
    case 3:
        print(f"{a}/{b}={a/b}")
    case 4:
        print(f"{a}*{b}={a*b}")
    case __:
        print("invalid input")
num=int(input("enter the number"))
if num>0:
    if num%2==0:
         print("positive even no")
    else:
        print("positive odd no")
else:
    print("negative no")