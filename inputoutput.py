
#---------------------
# Using Input()
# --------------------
a = input("Enter name")
print(a)
print(int(a)) 
print(type(a))

#---------------------
# Using raw_input()
# --------------------
a = raw_input("Enter name")
print(a)
print(int(a)) 
print(type(a))

x, y = input("Enter two values: ").split()
print(g)

x = input("Enter first name")
print(x)
y = input("Enter last name")
print(y)

# -------------------------------------------
# Taking multiple inputs
# -------------------------------------------

x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()

x, y ,z = input("Enter three values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print("Number of teacher: ", z)
print()

# -------------------------------------------
# Assigning variable using one line
# -------------------------------------------
a,b,c =10,20,30
print(a+b+c)



# -------------------------------------------
# String Formating
# -------------------------------------------
a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))
print()


# --------------------------------------------------------------------------
# taking multiple inputs at a time and type casting using list() function
# --------------------------------------------------------------------------
output - [10,20,30,40]

x = list(map(int, input("Enter multiple values: ").split()))
print(x)

x = list(map(str, input("Enter multiple values: ").split()))
print(x)

# --------------------------------------------------------------------------
# How to print without newline in Python?
# python 3 supports end =" "
# --------------------------------------------------------------------------
print("Hello jaya.",end =" ")
print("how are you.",end =" ") 
print("i am good.",end =" ")
print()
a =10
b=20
print(a,end =" ")
print(b)









