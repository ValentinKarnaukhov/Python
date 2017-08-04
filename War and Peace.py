def countWords(lst):
    d={}
    for i in lst:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
lst=[s.lower() for s in input().split()]
d=countWords(lst)
for key,value in d.items():
    print(key,value)