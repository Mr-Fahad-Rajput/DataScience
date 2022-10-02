import re

# open file
# with open("String.text", "r") as file:
#     data = file.read()
#     words = data.split()

#Print

text = "My name is Ja. wa d S.h afi. I a'm a phD. Student & my email is as followS: jawad SHAFi @ cuilahore.edu.pk."
x = re.search(r"\bJ.+fi", text)
y = re.search(r"\bp.+D", text)
z = re.search(r"\bj.+@.+", text)

if x is not None:
    print(x.group())
else:
    print('No Results Found')

if y is not None:
    print(y.group())
else:
    print('No Results Found')

if z is not None:
    print(z.group())
else:
    print('No Results Found')