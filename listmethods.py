# l1 = ['a','b','c','d','e','f',1,2,3,4]
# l1[9] = 12


# print(l1[9])

# Adding elements in the list
# 1.append() - this method will add one element in the last index of list.
# 2.index(a,b) - this method takes first parameter as a index value and second parameter as a value.
# 3.extend() - thi method will add multiple elemets at a time in the last index of list.

#append()
#--------------------------------------------------------------
# l1.append(30)
# print(l1)
# l1.append(30)
# print(l1)

#index()
#--------------------------------------------------------------
# l1.insert(2,40)
# print(l1)
# l1.insert(3,50)
# print(l1)

#extend()
#--------------------------------------------------------------

# l1.extend(['x','y','z'])
# print(l1)
# l1.extend(('x','y','z'))
# print(l1)
# l1.extend({'x','y','z'})
# print(l1)
# l1.extend("xyz")
# print(l1)
# d ={"xyz":101,"abc":201}
# l1.extend(d.values())
# print(l1)

#sum(),count(),index(),min(),max()
#--------------------------------------
#sum()
#-------------------------
# l1 = [10,20,30,40,50]
# print(sum(l1))
#output - 150

# l1 = [10,20,30,40,50,'x','y']
# print(sum(l1))
#output - throws TypeError

# l1 =102
# s1="jaya"
# print(l1+s1)

#count
#-----------------------
# l1 = [10,20,30,40,50,10,10,30,'a']
# print(l1.count(10))

# print(len(l1))

#index()
#--------------------------------------------------------------
# print(l1.index('a'))
# print(min(l1))

#max
#--------------------------------------------------------------
# from filecmp import cmp


# l1 = [10,20,30,40,50,10,10,30]
# l2 = set(l1)
# print(l2)
# l2 = max(l1)
# print(l2)

#min
#--------------------------------------------------------------
# l1 = 50
# l2 = 10
# print(min(l1))

#compare
#--------------------------------------------------------------
# print(cmp(l1,l2))

#index
#------------------------
l1 = [10,20,30,40,50,10,10,30,50]
# print(l1.index(50))

# pop - used to delete elements from the list based on index
#--------------------------------------------------------------
# print(l1.pop()) - by default it will delete last element from the list
# print(l1.pop(1)) - This will delete index based element from the list
# print(l1)

#remove - used to delete elements from the list based on elements
#-------------------------------------------------------------------
# print(l1.remove(20)) 
# print(l1)

#Reverse - this method will reverse a given list
# print(l1.reverse())
# print(l1)

#sort - 
# l1 = ['a','abc','ac','ab']
l1.sort() 
# - By Default it will sort in ascending order
l1.sort(reverse=True)
#  - If you want to sort in descending order we have pass reverse = True
print(l1)












