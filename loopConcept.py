# print("1")
# print("2")
# print("3")


# Ex-1
# --------------------------------
# from re import T
# from tkinter import Y


# str1 = "Python"
# o/p- 
# p
# Y
# T
# h
# print(str1[0])
# print(str1[1])
# print(str1[2])

# for i in str1:
#     print(i)


# Ex2: Program to print the table of the given number.
# --------------------------------------------------------

# list = [1,2,3,4,5,6,7,8,9,10,'a']
# n = 5
# for i in list:
#     c =n*i
#     print(n, "*", i,"=", c)


# Ex3: Program to print the sum of the given list.
# -----------------------------------------------------

# list1 = [10,30,23,43,65,12] 
# print(len(list1))
# sum_val = 0

# for i in list1:
#     sum_val = sum_val + i
    # print(sum_val)
    # print("hello")

# print(sum_val)


# Ex-4: Program to print numbers in sequence using range().
# for i in range(1,11):
#     print(i)


# Ex2: Program to print the table of the given number using range().
# --------------------------------------------------------
# n = 5
# for i in range(1,11):
#     c =n*i
#     print(n, "*", i,"=", c)


# Ex-4: Program to print even numbers in sequence using range().
# for i in range(2,11,2):
#     print(i)


#Nested Loop
# o/p 
# *
# **
# ***
# ****

num = int(input("Enter a number"))
for i in range(0,num+1):
    for j in range(i):
        print("*", end="")
    print()










