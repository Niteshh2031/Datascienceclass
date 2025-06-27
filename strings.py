#printing simple message of strings using variable
name="Ram"
print(f"Hello, {name}, How are you doing?")
#the code could be made alternatively as
name="Hari"
message="How are you doing"
print(f"Hello,{name},{message}?")
#name case using string methods
name="Lionel Messi"
print(name.title())
print(name.upper())
print(name.lower())
#use of single quote and double quote
print('Albert einstein once said, "A man who never made mistake never tried anything new!"')
#alternatively
name="Albert Einstein"
saying="A man who never made mistake never tried anything new!"
print(f'{name} once said, "{saying}"')
#whitespacing in python 
first_name="  Rajneesh "
last_name=" Osho "
full_name=f"{first_name} {last_name}"
print(f"Details of the person:\n\tFirst name:\t{first_name}\n\tLast name:\t{last_name}")
#removing whitespacing
name=f"{first_name.strip()} {last_name.strip()}"
print(full_name)
print(name)