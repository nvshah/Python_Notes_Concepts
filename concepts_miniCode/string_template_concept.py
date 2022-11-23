import string 

greeting = "hey $name, welcome to $place"
template = string.Template(greeting)

s = template.substitute({'name': 'Naruto', 'place': 'Leaf Village'})

print(s)

