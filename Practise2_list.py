#creating a list
places=['paris','barcelona','sydney','rome','munich','london','Adelaide']
print(places)
#adding item in list
places[0]='lisbon'
print(places)
#inserting item 
places.insert(0,'paris')
print(places)
#appending item at last place
places.append('maracana')
print(places)
#deleting item permanently
del places[0]

print(places)
del places[0]
print(places)
del places[0]
print(places)
#pop method to pop any index item 
item=places.pop()
print(places)
print(f"The popped item is {item.title()}")
item=places.pop(0)
print(f"The popped item is {item.title()}")
#removing item from name rather index
places.remove('Adelaide')
print(places)