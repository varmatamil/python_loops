

ls = ["apple", "mango" ,"orange","bananna" , "avacado"]
'''
print all the fruits name with index 
output
0 apple
1 mango
2 orange
3 bananna
4 avacado
'''

for i in range(0,len(ls)):
    print(i,ls[i])


'''
ls = ["apple", "mango" ,"orange","bananna" , "avacado"]
print all the fruits name that starts with the letter a
output
apple 
avacado
'''

for i in ls:
    if i.startswith("a"):
        print(i)

'''
ls = ["apple", "mango" ,"orange","bananna" , "avacado"]
print all the fruits name that doesn't starts with the letter a
output
mango 
orange
bananna
'''

for i in ls:
    if i.startswith("a") == False:
        print(i)

ls = ["apple", "mango" ,"orange","bananna" , "avacado"]
'''
print all the fruits name that has a total length more than 5
For example the total letters in apple is 5 so skip it 
in bananna its 7 so add that etc.. 
output 
orange
bananna
avacado
'''

for i in ls:
    if len(i) > 5:
        print(i)


ls = {
    "fruit": "apple",
    "vegetable" : "Onion",
    "animal" : "elephant",
    "bird" : "peacock"
}
'''

print all the keys 
output : 
fruit
vegetable
animal
bird

print all the values
apple
Onion
elephant
peacock


print keys with values
fruit apple
vegetable Onion
animal elephant
bird  peacock

Here keys are left to the ":" and values are right to ":"

'''
for x in ls:
    print(x)

for x in ls:
    print(ls[x])


for x in ls:
    print(x,ls[x])
