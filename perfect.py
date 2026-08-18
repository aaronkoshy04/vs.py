#after inputing the number and choice there should be another question y/n as aloop until we give n
#if we use for loop , we would need to give range and upto that only there will be loop
while True:
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

    s=input("do u wish to continue(y/n)?:")
    if s!="y":
        print("exiting")
        break  
#from user take a number , find its divisor
count=1
a=(int(input("enter the no:")))
while count<=a:
    if a%count==0:
        print(count,end=" ")
    count+=1
#to check whether a number is perfect no or not ( perfect no is divisors sum will give the no itself)

#to check whether a number is perfect no or not ( perfect no is divisors sum will give the no itself)
total=0
i=1
a=int(input("enter the no:"))
while i<a:
    if a%i==0:
       total+=i 
    i+=1
if a==total:
    print(a,"is a perfect number")
else:
    print(a,"is not a perfect number")
#to check whether the no is a prime no
#multiplication number1,246,369,
for i in range(1,5):
    num=i
    for c in range(1,i+1):
        print(num,end=" ")
        num*=i
    print(' ')