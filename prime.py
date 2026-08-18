'''
#to check whether a number is a prime no or not
num=int(input("Enter the number : ")) # getting number from user
is_prime=True  # setting a variable with value True to indicate status after completing for loop
if num>1: # First condition of prime number ie number must be grater than 1
    for k in range(2,num):  # For checking each number wheather it is divisible by num
        if num%k==0: # If any number ie k gets divisible by num variable value is changed 
            is_prime=False
            print(f"{num} is not prime number")
            break # loop get terminate
    if is_prime:# Outside loop variabe value is evaluated if there is change it means num got divisible number 
        print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")
#another way of prime number
num=int(input("Enter the number : "))
if num>1:
    for k in range(2,num):
        if num%k==0:
            print(f"{num} is not prime number")
            break
    else:
        print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")
#to print a design
for k in range(1,6):
    print("* "*k)
''
    * 
   ** 
  *** 
 **** 
*****
'''
for r in range(1,6):
    for sp in range(5-r):
        print(" ",end="")
    for st in range(r):
        print("*",end="")
    print("")
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * *
'''
for r in range(1,6):
    for sp in range(5-r):
        print(" ",end="")
    for st in range(r):
        print("* ",end="")
    print("")

'''''
**** 
***  
**   
*  
'''
for r in range(1,6):
    for sp in range(5-r):
        print("*",end="")
    for st in range(r):
        print(" ",end="")
    print("")
'''
*****
 ****
  ***
   **
    *
'''
for r in range(1,6):
    for st in range(r-1):
        print(" ",end="")
    for sp in range(5-r):
        print("*",end="")
    print("")
'''
    *
   ***
  *****
 *******
*********
'''
for r in range(1,6):
    for sp in range(5-r):
        print(" ",end="")
    for st in range(r*2-1):
        print("*",end="")
    print("")


"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
for r in range(1,6):
    for sp in range(5-r):
        print(" ",end="")
    for st in range(r*2-1):
        print("*",end="")
    print("")
for r in range(4,0,-1):# count from 4 to 0th index posn in -1step-4,3,2,1
    for sp in range(5-r):
        print(" ",end="")
    for st in range(r*2-1):
        print("*",end="")
    print("")

'''hollow box
* * * * * 
*       * 
*       * 
*       * 
* * * * *
'''
for r in range(1,6):
   for j in range(1,6):
       if r==1 or j==1 or r==5 or j==5:
            print("*",end=" ")
       else:
            print(" ",end=" ")
   print("")
'''''hollow triangle
* 
* * 
*   * 
*     * 
* * * * *
'''''
for r in range(1,10):
    for j in range(1,10):
        if j==1 or r==9  or r==j:
            print("*",end=" ")
        elif j<r: 
            print(" ",end=" ")
    print("")
'''hollow pyramid
'''
for i in range(1,10):
    for j in range(9-i):
        print(" ",end=" ")
    for k in range(1,i*2):
        if k==1 or k==i*2-1 or i==9:
            print("*",end=" ")
        else:#if elif used with j<r half triangle is formed
            print(" ",end=" ")
    print("")