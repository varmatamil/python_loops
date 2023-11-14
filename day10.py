
ls = {
    "names" : ["kaviya" , "appu" , "amma" , "appa"],
    "age" : [12,24,34,43]
}
'''
From the dictionary ls 
1. print all the names 
sample o/p 
['kaviya' , 'appu' , 'amma', 'appa'] 

2. print all the ages 
[12,24,34,43] 

3. print all the names 
kaviya
appu
amma
appa

4.print all the ages
12
24
34
43


6. print the names associated with their index
kaviya 0
appu 1
amma 2
appa 3


7. print the ages associated with their index
12 0
24 1
34 2
43 3


8. print the names associated with their ages
kaviya 12
appu 24
amma 34
appa 43


9. print the names those are eligible to vote alone
appu
amma
appa
'''

print(ls["names"])

print(ls["age"])

for x in ls["names"]:
    print(x)

for x in ls["age"]:
    print(x)

for x in range(0,len(ls["names"])):
    print(ls["names"][x],x)

for x in range(0,len(ls["age"])):
    print(ls["age"][x],x)

for x in range(0,len(ls["names"])):
    print(ls["names"][x],ls["age"][x])

for x in range(0,len(ls["names"])):
    if ls["age"][x] > 18:
        print(ls["names"][x])




