from xml.dom.minidom import Element


# d1 = {1:'python',2:{1:{'a':"learn","b":10},2:"python"},"a":"for"}
# d1["a"]="I"
# print(d1)
# d1[1]= 1,2,13
# print(d1)
# d1[2][1]['b'] = 30
# print(d1)

#get() - it is used to get values from the dictionary
# print(d1.get("a"))
# print(d1.get("b"))

#Adding elemts in dictionary
#update()
# d1.update({10:"I"})
# print(d1)

#keys()
# print(d1.keys())

#values
# print(d1.values())

#clear()
# print(d1.clear())

# Removing the Elementfrom the dictionary
# pop()
# print(d1.pop("a"))
# print(d1)

# popitem()
d1 = {1:'python',2:{1:{'a':"learn","b":10},2:"python"},"a":"for"}
# print(d1.popitem())
# print(d1)

#items()
print(d1.items())
# print(d1)
