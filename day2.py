ls = [1,2,3,4,5]

print(ls[0])

print(ls[-1])

for i in range(len(ls),-1,-1):
    print(i)
    break

for i in range(0,len(ls)):
    print(ls[i])
    break


ls = [11,12,13,14,15]

for i in ls:
    print(i)

for i in range(0,len(ls)):
    print(i)

for i in range(0,len(ls)):
    print(i,ls[i])
