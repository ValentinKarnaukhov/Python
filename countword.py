d={}
with open("input.txt") as inf:
    for line in inf:
        line=line.strip()
        for a in line.split():
            a=a.lower()
            if a in d.keys():
                d[a]+=1
            else:
                d[a]=1
d=list(d.items())
d.sort(reverse=True,key=lambda x:x[1])
print(d[0])