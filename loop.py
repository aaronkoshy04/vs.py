#list
list_1=["a",1,2,3,4,5,"jgbdfu"]
for h in list_1:
    print(h)
#set
s={"asd",1,2,3}
for a in s:
    print(s)
#tuple
t=("asdfg",1,2,3,4,1.08)
for o set:
    print(o)
#dictionary
dict={"s1":"abcd","s2":"efgh","s3":"lmnop"}
for p in dict:
    print(p)
#for+if
numbers=[15,48,6,5,54,156465,457,12]
for num in numbers:
    if num%2==0:
        print("num is even")
    else:
        print("num is odd")
numbers=[15,48,6,5,54,156465,457,12]
for num in numbers:
    if num%2==0:
        print(num,"is even")#identifier not string
    else:
        print(num," is odd")
#range
print(list(range(25)))
for n in range(3,15,2):
    print(n) 
for n in range(3,15,5):
    print(n)
#table of 5
for num in range(1,11):
    print(num*5)
#table of n
n=int(input("enter the number:"))
for num in range(1,16):
    print(f"{num} x {n} = {num*n}")

#workout
num=int(input("enter the number"))
fact=1
for k in range(1,num+1):
    fact=fact*k
print("answer is", fact)
#
a,b=10,3
a,b=b,a
print(a,b)
#
print("hi",end="")
print("aaron")
#
print("hi",end=" ")#whatever comes in between end bracket comes 
print("aaron")
# 
for n in range(1,11):
     print(n,end=" ")
#
first=0
second=1
print(first,second,end=" ")
for k in range(8):
    third=first+second
    print(third,end=" ")
    first,second=second,third
#while loop
count=1
while count<=10:
    print(count)
    count+=1
#
num=int(input("enter the number:"))
count=1
fact=1
while count<=num:
    fact*=count
    count=count+1
print("factorial of " ,num, "is ",fact)
#
count=1
first=0
second=1
print(first,second,end=" ")
while count<=8:
    third=second+first
    print(third,end=" ")
    first,second=second,third
    count+=1
#upto 5 value
for n in range(1,11):
    if n==5:
        break 
    print(n,ends=" ")
#n is true then the contents in wont work otherthan 5 will work
for n in range(1,11):
    if n==5:
        continue
    print(n,end=' ')
#some numbers in a list, and in that we need to print the first 2 even numbers 
'''''
numbers=[45,24,9,12,8,3,89,78]
count=1
print(numbers{1},numbers{2},end=" ")
while count<=2:
     if numbers%2==0:
         break
     print(numbers,end=" ")
'''''
numbers=[45,24,9,12,8,3,89,78]
count=0
for n in numbers:
    if n%2==0:
        print(n,end=" ")
        count+=1
    if count==2:
        break
#inner loop
for i in range(1,10):
    for k in range(1,i+1):
        print(k,end=" ")
    print("")#if not it will come 1 12 123 1234 12345 in the same line so we simply put print without end 
num=1
for i in range(1,5):
    for k in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print("")