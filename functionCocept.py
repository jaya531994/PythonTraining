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


def ABC(a=10,b=20):
    c = a+b
    print("hello")
    return c
   

a = ABC()
print(a)