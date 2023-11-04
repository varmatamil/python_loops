ls = [12,14,15,19,20]

for x in ls:
    print(x)

for i in range(0,len(ls)):
     print(i,ls[i])

for i in range(0,len(ls)):
     if ls[i] % 2 == 0:
         print(i,ls[i])

new_list_ls1 = []
for i in range(0,len(ls)):
    if ls[i] % 2 == 0:
        x = ls[i]
        new_list_ls1.append(x)
print(new_list_ls1)

new_list_ls1=[]
for i in range(0,len(ls)):
    if ls[i] % 2 == 0:
        x = ls[i]
        new_list_ls1.append(x)
y = len(new_list_ls1)
print(y)





