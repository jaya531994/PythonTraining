from zlib import Z_PARTIAL_FLUSH


l1 = [10,20,30,'a']
# print(l1[2])

#interview question
#Can we update elements of string?

# var1 ="Hello World"
# # var1[0] = 'P'
# print(var1[:6] + 'python')


# str1 = "Therefore, ' ' this raises an exception that the immutable objects do not change their value but the value of constituents changes their value."
# print(str1)

# print("r \n  print \n and print R'\n' print \n")

#String Formating
# name = 'jaya'
# weight = 21
# print("My name is %s and weight is %d kg!" % (name, weight))

#Using Format method
#------------------------------------------------
# Ex -
# age = 36
# name = "jaya"
# feel = "good"
# str1 = "my name is {} and age {} and i am {}"
# print(str1.format(name,age,feel))

# Ex- using index
# age = 36
# name = "jaya"
# feel = "good"
# str1 = "my name is {1} and age {0} and i am {2}"
# # print(str1)
# print(str1.format(age,name,feel))



# str1 = "jaya"
# str2 = "dwivedi"
# str3 = str1 - str2
# print(str3)

#8bit = 1 byte
# import sys
# str1 = u'Hello, world!'
# print(sys.getsizeof(str1))
# str2 = "Hello, world!@#%$"
# print(str2)

#---------------------------------
#String Methods
#---------------------------------
# txt = "my age is 36"
# print(txt.capitalize())
# txt = "Hello, And Welcome To My World!"
# print(txt.casefold())
# print(txt.lower())
# txt = "Hello"
# print(txt.center(30))

# txt = "I love apples, apple are my favorite fruit"
#by default it will 
# print(txt.count("apple"))
# print(len(txt))
# print(txt.encode())
# print(txt.endswith("fruit"))
txt = "H\te\tl\tl\to"
print(txt.expandtabs(2))
