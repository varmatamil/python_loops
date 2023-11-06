# day1
ls = ["a","b","c","d","c"]
'''print the total number of elements present in the ls
output = 5
'''

print(len(ls))

ls = ["a","b","c","d","c"]
'''print all the elements 
output = 
a
b
c
d
c 
'''
for x in ls:
    print(x)

# match the element
ls = ["a","b","c","d","c"]
# element = "c"
'''print 
output = 2 
'''

i = 0
j = "c"
for k in range(0,len(ls)):
    if ls[k] == j:
        i+=1
print(i)

# day2
'''
ls = [1,2,3,4,5]
print the last index number 
ouput = 5 
'''

ls = [1,2,3,4,5]

for i in range(len(ls),-1,-1):
    print(i)
    break

'''
ls = [1,2,3,4,5]
print the first index number 
ouput = 1 
'''

for i in ls:
    print(i)
    break

'''
ls = [11,12,13,14,15]
print the all the numbers 
ouput = 
11
12
13
14
15
'''
ls = [11,12,13,14,15]
for x in ls:
    print(x)


'''
ls = [11,12,13,14,15]
print the all index numbers 
ouput = 
0
1
2
3
4
'''

for i in range(0,len(ls)):
    print(i)

'''
ls = [11,12,13,14,15]
print the all index numbers with values
ouput = 
0 11
1 12
2 13
3 14
4 15
'''

for i in range(0,len(ls)):
    print(i,ls[i])

# day3
'''
ls = [11,12,13,14,15]
print the all index numbers with values , where each values should be 
added with number mentioned below
number = 2
ouput = 
0 13
1 14
2 15
3 16
4 17
Description : Each number from the list , the number 2 is added
to it for example if the number is 11 add 2 to it and print the new 
number as 13 
'''
ls = [11,12,13,14,15]

for i in range(0,len(ls)):
    ls[i]+=2
    print(i,ls[i])

'''
ls = [10,20,30,40,50]
print the all index numbers with values , where each values should be 
added with number mentioned below
even_index = 2
odd_index = 3
ouput = 
0 12
1 23
2 32
3 43
4 52
Description : Each number from the list ,if the index is even number
the number 2 is added
to it for example if the number is 10 add 2 to it and print the new 
number as 12 
if the index is odd add 3 it to , for example the 
index of 20 is 1 since it is an odd index add 3 and print the 
output as 23
'''

ls = [10,20,30,40,50]

for i in range(0,len(ls)):
    if i % 2 == 0:
        ls[i]+=2
    else:
        ls[i]+=3
    print(i,ls[i])



ls = ["abc" , "ade", "aff" ,"agg"]
'''
print all the values from the list
output 
abc
ade
aff
agg

'''
for x in ls:
    print(x)

'''
ls = ["ab" , "adfe", "acff" ,"agg"]
print all the values from the list with the length of each value
output 
ab 2
adfe 4
acff 4
agg 3

'''

for x in ls:
    print(x,len(x))


ls = [12,14,15,19,20]
'''
print all the numbers
output : 
12
14
15
19
20
'''

for numbers in ls:
    print(numbers)

'''
ls = [12,14,15,19,20]
print all the numbers with index
output : 
0 12
1 14
2 15
3 19
4 20
'''
for i in range(0,len(ls)):
    print(i,ls[i])

'''
ls = [12,14,15,19,20]
print all the  even numbers with index
output : 
0 12
1 14
4 20
'''

for x in range(0,len(ls)):
    if ls[x] % 2 == 0:
        print(x,ls[x])

'''
ls = [12,14,15,19,20]
create a new list ls1 = []
and store the values that are even numbers 
output : [12,14,20]
'''
new_list_ls1 = []
for x in ls:
    if x % 2 == 0:
        new_list_ls1.append(x)
print(new_list_ls1)

'''
ls = [12,14,15,19,20]
create a new list ls1 = []
and store the values that are even numbers  and print the total even numbers
output : 
[12,14,20]
3 

'''
new_list_ls1 = []
for i in ls:
    if i % 2 == 0:
        new_list_ls1.append(i)
print(len(new_list_ls1))

