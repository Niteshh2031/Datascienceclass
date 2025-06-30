list=['apple','mango','cherry','plum','banana']
print("The list:")
print(list)
#sort to permanently arrange in alphabetical  order
list.sort()
print(list)
#reverse alphabetical
list.sort(reverse=True)
print(list)
#sorted to temporaliry arrange
print("The sorted list is:")
print(sorted(list))
print("The original list is:")
print(list)
#temporarily reverse alphabetical
print("The original list is:")
print(list)
print("The reversed alphabetical list:")
print(sorted(list,reverse=True))
#reverse of list
list.append('grape')
print(list)
list.reverse()
print(list)