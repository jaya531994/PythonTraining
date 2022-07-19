#Adding Elements in set
#-------------------------------------
# Ex-1
# s1 ={"p","y","t","h","o"}
# s1.add("n")
# s1.add("p")
# print(s1)

# Ex-2
# s1 = {6,0,2}
# print(s1)
# s1.add(1)
# print(s1)

# Ex-3 Adding tuple
# s1 = {"p","y","t","h","o"}
# s2 =("i","s")
# s1.add(s2)
# print(s1)

#Adding element using update()
#------------------------------------
# s1 = {"p","y","t","h","o"}
# t1 = ("i","s")
# s1.update(t1)
# print(s1)


#Removing elements from set
#using Remove function
# s1 = {"p","y","t","h","o"}
#if elements is inside set
# s1.remove("p")
#if elements not inside set
# s1.remove("j")
# print(s1)

#using discard function
# s1.discard("j")
# s1.discard("p")
# print(s1)


#using pop function
# s1.pop()
# print(s1)

#using clear method
# s1.clear()
# print(s1)

#frozenset
#-----------------------------------
# s1 = {"p","y","t","h","o"}
# s2 = frozenset(s1)
# print(s2)

s1 = {"p","y","t","h","o"}
# print(s1)
# s2 = s1.copy()
# print(s2)
# s2 = s1.union()
# print(s2)

s2 ={"j","i","p","y"}
# s3 = s1.difference_update(s2)
# s3 = s1.intersection(s2)
s3 = s1.intersection_update(s2)
# print(s1)
print(s3)


