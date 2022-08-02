# abc = lambda a: a+20
# print(abc(10))


# def abc(a):
#     return a + a
    
# print(abc(10))


#using filter()

# list1 = [34, 12, 64, 55, 75, 13, 63]
#using normal def function
# def abc(l1):
#     for i in l1:
#         if i % 2 != 0:
#             print("number is odd",i)

# abc(list1)

#using lambda

# list2 = list(filter(lambda i:i % 2 !=0, list1))
# print(list2)

#using map()

# numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]

# list1=list(map(lambda i : i*i,numbers_list))
# print(list1)

#list comprehension
#----------------------------------
#using normal function example
l1 = [34, 12, 64, 55, 75, 13, 63]
# list2 =[]
# for i in l1:
#     if i % 2 != 0:
#         list2.append(i)
    
# print("number is odd",list2)

#using list comprehension
#using if
# list2 = [i for i in l1 if i % 2 != 0 ]
# print(list2)

#using if-else
# list2 = [i  if i % 2 != 0 else print("not odd") for i in l1]

#Lambda function using if-else condition
#----------------------------------------------
#find the odd number from list
l1 = [34, 12, 64, 55, 75, 13, 63]

def abc(l1):
    list2 =[]
    for i in l1:
        if i % 2 != 0:
            list2.append(i)
    return list2

print(abc(l1))

#mixumum number
# abc = lambda x,y:x if (x < y) else y
# print(abc(61,52))


    






