# def ABC():
#     a =10
#     b=20
#     c = a+b
#     print(c)

# ABC()


#parameterize function

# def ABC(a,b):
#     c = a+b
#     print(c)
#     print("hello")

# ABC(10,20)


# def ABC(a=10,b=20):
#     c = a+b
#     print("hello")
#     return c
   

# a = ABC()
# print(a)

#call By refrence
# def ABC(a):
#     a=a+1
#     print("a inside",id(a))
#     return a

# a = 10
# print("a outside",id(a))
# b = ABC(a)
# # b = a
# print(b)
# print("b after return",id(b))

# def ABC(list1):
#     list1.append(30)
#     print("inside",list1,id(list1))
#     return list1

# l1 = [10,20]
# print("ouside",l1,id(l1))
# b = ABC(l1)
# print(b,id(b))

#*args 
#--------------------------------------

def XYZ(*a):
    return a

print(XYZ(10,30))

#**kargs
#----------------------------------------

def XYZ(**k):
    return k

print(XYZ(a=10,b=30))


def XYZ(**k):
    print(k)

print(XYZ(a=10,b=30))
