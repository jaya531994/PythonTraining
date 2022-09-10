# a = ["python",'a','b']

# for i in range( 4 ):
#         print("The index and element from the array is", i, a[i] )
# try:
# #looping through the elements of the array a, choosing a range that goes beyond the length of the array
#     for i in range(4):
#         print("The index and element from the array is", i, a[i] )
#     #if an error occurs in the try block, then except block will be executed by the Python interpreter
# except:
#     print("Index out of range")
# finally:
#     print("Program executed and no error found")


# num = [3, 4, 5, 7]
# print(len(num))
# if len(num) > 3:
#     raise Exception( f"Length of the given list must be less than or equal to 3 but is {len(num)}" )

# div = 4 // 0
# print(div)

try:
    div = 4 // 2
    print(div)
# this block will handle the exception raised
except ZeroDivisionError:
    print( "Atepting to divide by zero" )
# this will always be executed no matter exception is raised or not
except:
    print("Found syntex error")
else:
    print("else block execute")
finally:
    print( 'This is code of finally clause' )


# class EmptyError():
#     a = 10
#     def abc(self):
#         print("hello")


# obj = EmptyError()
# obj.abc()





