
ls = [{
    "fruit": "apple",
    "vegetable" : "Onion",
    "animal" : "elephant",
    "bird" : "Eagle"
},
{
    "fruit": "orange",
    "vegetable" : "Tomato",
    "animal" : "dog",
    "bird" : "parrot"
}]
'''
1 . iterate the loop and print all the elements 
output
apple
Onion
elephant
Eagle
orange
Tomato
dog
parrot

2 . iterate the loop and print the fruits 
output 
apple
orange


3. If the keys has length more than 5 letters 
print the key and value
Guess the output ? and print it 

4.list1 =  ["a","b","c","d","e","f"]
print out how many vowels present in the list1 and how many consonants 
present in the list1.

5. find the total sum of the given list 
list2 = [10,20,30,40,343]
Guess the output 


6. find the total sum of the even index in the given list 
list3 = [10,20,30,40,343]
Guess the output ?



7. find the total sum of the even value in the given list 
list4 = [10,20,30,40,343]
Guess the output ?
'''

for x in ls:
    for y in x:
        print(x[y])

for x in ls:
    for y in x:
        if y.startswith("f"):
            print(x[y])

for x in ls:
    for y in x:
        if len(y) > 5:
            print(y,x[y])



ls =  ["a","b","c","d","e","f"]

vowels = ["a","e","i","o","u"]

for x in ls:
    if x in vowels:
        print(x)
for x in ls:
    if x  not in vowels:
        print(x)

list2 = [10,20,30,40,343]
sum_of_list = 0

for x in list2:
    sum_of_list+=x
print("total:"+str(sum_of_list))

sum_of_even_index = 0
for x in range(0,len(list2)):
    if x % 2 == 0:
        sum_of_even_index+=list2[x]
print("even_index_value:",sum_of_even_index)


sum_of_even_value= 0

for x in list2:
    if x % 2 == 0:
        sum_of_even_value+=x

print("even_value:"+str(sum_of_even_value))


c = {
    "name" : "kaviya",
    "age"  : 23
}


c["dept"] = "CS"
print(c)


ls = [10,1,20,3,4]
y = 0
for x in ls:
    if x > y:
        y = x

print(y)
