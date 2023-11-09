
ls = {
    "fruit": "apple",
    "vegetable" : "Onion",
    "animal" : "elephant",
    "bird" : "peacock"
}
'''

print out all the keys 
output
fruit
vegetable
animal
bird
'''

for x in ls:
    print(x)


'''
ls = {
    "fruit": "apple",
    "vegetable" : "Onion",
    "animal" : "elephant",
    "bird" : "peacock"
}

print out total number of keys 
output
4
'''


new_list = []

for x in ls:
    print(x)
    new_list.append(x)

print(len(new_list))

count = 0

for x in ls:
    count+=1
print(count)


ls = {
    "fruit": "apple",
    "vegetable" : "Onion",
    "animal" : "elephant",
    "bird" : "eagle"
}
'''
print out all values 
output
apple
onion
elephant
eagle
'''

for x in ls:
    print(ls[x])


ls = {
    "fruit": "apple",
    "vegetable" : "Onion",
    "animal" : "elephant",
    "bird" : "eagle"
}
'''
print out total number of values starts with the letter "e" 
output
2
'''

x = 0

for y in ls:
    if ls[y].startswith("e"):
        x+=1
print(x)


ls = {
    "fruit": "apple",
    "vegetable" : "Onion",
    "animal" : "elephant",
    "bird" : "eagle"
}
'''
print out total number of letter the value has  with the value
apple - 5
Onion - 5
elephant - 8
eagle - 5
'''

for x in ls:
    print(ls[x],len(ls[x]))



ls = {
    "fruit": "apple",
    "vegetable" : "Onion",
    "animal" : "elephant",
    "bird" : "Eagle"
}
'''
check if the first letter of the value is uppercase if yes print 
those values
output
Onion
Eagle
'''
for x in ls:
    if ls[x][0] == ls[x][0].upper():
        print(ls[x])
