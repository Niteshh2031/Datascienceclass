# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and r
#creating list and printing message to each list item
clubs=['Arsenal','madrid','Barcelona']
for item in clubs:
    print(f"{item}, Welcome to the champions league!")
print("\nHope you play beautiful football!")
#slcing item in a list
clubs.append('paris')
clubs.insert(0,'Milan')
clubs.append('Munich')
print(clubs)
print(clubs[:3])#item upto 3rdelement 
print(clubs[2:])#item starting from 3rd element
print(clubs[2:5])#all item between 3rd and 6th element(exclusive)
print(clubs[-2:])#retrun the last 2 elements -1 indicates last
#can work in slices with loop too
print("The first two teams are:")
for item in clubs[:2]:
    print(f"-{item}")
print("\nThe last two teams are:")
for item in clubs[-2:]:
    print(f"-{item}")
    
#list can be made using range
thousand=[(range(1000)]#includes 0 to 999
hundred=[(range(1,101)]#includes 100 the second arguments must be n+1 to include n
#list comprehension to print cube root of first 10 elements
cubes=[x**3 for x in range(1,11)]
print(cubes)

#list can be copied
original=['a','b','c']
copy=original[:]
print(original)
print(copy)
copy.append('d')
print(original)
print(copy)


