#global scope
# b =20

# def check():
    #local scope
#     a = 30 + b
#     print("inner value",a)

# def substractionVal():
#     a = 30 - b
#     print("inner value",a)


# def multiplicationVal():
#     a = 30 * b
#     print("inner value",a)


# def divisionVal():
#     a = 30 / b
#     print("inner value",a)

# check()
# substractionVal()
# multiplicationVal()
# divisionVal()


# print("outer a value",b) 

# Inner Funtion or Nested function

def ABC():
    s1 = "PYTHON IS GOOD"
    b = 10
    a = b + 30

    def XYZ():
        print(s1)
        print("a=",a)

    XYZ()
ABC()