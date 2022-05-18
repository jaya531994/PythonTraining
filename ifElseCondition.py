
# -----------------------------------------------------
# if syntax
# ----------------------------------------------------
# if expression:
#     statements

# Ex-1

a =500
b =100

if b > a:
    print("b is greater than a")
if b < a:
    print("b is less than a")

# Ex-2
a = int(input("Enter a number"))
if a%2 ==0:
    print("number is even")

# Ex-3
a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))
if a>b and a >c :
    print("a is larger")
if b>a and b >c:
    print("b is larger")
if c>b and c >a:
    print("c is larger")

#--------------------------------
# nested if
# -------------------------------
# Ex-4 check number is even or odd
a =31
if a%2 == 0:
    if a < 10:
        print("Number is Even less then 10")
    else:
        print("Number is Even and greater then 10")


# ----------------------------------------------------
# indentation
# ----------------------------------------------------
a = int(input("Enter a number"))
if a%2 ==0:
print("number is even")

# ----------------------------------------------------
# Syntax of else condition 
# ----------------------------------------------------
# if condition:  
#     #block of statements   
# else:   
#     #another block of statements (else-block)  

# Ex –1  Program to check whether a number is even or not.
a =int(input("Enter a number"))
if a%2 == 0:
    print("Number is Even")
else:
    print("Number is odd")

# Ex-2 : Program to check whether a person is eligible to vote or not
age = int(input("Enter a number"))
if age >=18:
    print("person is eligible to vote")
else:
    print("person is not eligible to vote")


# ----------------------------------------------------
# The syntax of the elif statement is given below.
# ----------------------------------------------------
# if expression 1:   
#     # block of statements   
# elif expression 2:   
#     # block of statements   
# elif expression 3:   
#     # block of statements   
# else:   
#     # block of statements 


Ex - 
a =33
b=100
c =150
if a>b and a >c :
    print("a is larger")
elif b>a and b >c:
    print("b is larger")
elif c>b and c >a:
    print("c is larger")

# --------------------------------------------
# Shorthand If - write if condition in single
# --------------------------------------------

a,b = 50,20
if a > b: print("a is greater than b")

# --------------------------------------------
# Shorthand If else - write if condition in single
# --------------------------------------------

a = 500 
b = 330 
print("A") if a > b else print("B")

a,b = 330,330
print("A") if a > b else print("##") if a == b else print("B")

from ast import Or


And,Or

a = 50
b=20
c=30
if a > b and a>c:
    print("A is greater")

a = 50
b=20
c=70
if a > b or a > c:
    print("A is greater")


# --------------------------------------------
# Nested If else - if condition inside if
# --------------------------------------------
x = 41 
if x > 10:
    print("Above ten,")
    if x > 20: 
        print("and also above 20!") 
    else:
        print("but not above 20.")








