# a = 10
# print("a value is:", a)

#---------------------
#String Literals
#---------------------

# -----------------------------------------
# /n - string will terminate in the next line
#------------------------------------------
# print("Python. \n Python is the best language for programming.")


# ------------------------------------------------------
# Flush- by default it is true and flush is used for the
#buffer time
#--------------------------------------------------------

# import time
# count_seconds = 3
# for i in reversed(range(count_seconds+1)):
# 	if i > 0:
# 		print(i, end='>>>',flush=True)
# 		time.sleep(2)

# 	else:
# 		print('Start')

#--------------------------------------------------------------------------------
#Separator - used for formatting multiple statements in a single print() function
#--------------------------------------------------------------------------------
# from sys import stdin

# a=10
# b='hello'
# c='jaya'

# print("hi my age is",a,".",b,"how are you?",c,".","i am good")



# import io
# declare a dummy file
# dummy_file = io.StringIO()
# add message to the dummy file
# print('Hello Python!!', file=dummy_file)
# get the value from dummy file
# dummy_file.getvalue()


print("Python", end='')
print("Python is \n very nice")





