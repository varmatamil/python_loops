

ls = [11,12,13,14,15]

for i in range(0,len(ls)):
    ls[i] += 2
    print(i,ls[i])


ls = [10,20,30,40,50]

for j in range(0,len(ls)):
    if j % 2 == 0:
        ls[j] += 2
    else:
        ls[j] += 3
    print(j,ls[j])

ls = ["abc" , "ade", "aff" ,"agg"]

for alphabets in ls:
    print(alphabets)

ls = ["ab","adfe","acff","agg"]

for alpha in range(0,len(ls)):
    print(ls[alpha],len(ls[alpha]))

















