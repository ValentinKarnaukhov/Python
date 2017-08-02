
a=[int(i) for i in input().split()]
b=[a[len(a)-1]]
b.extend(a)
b.append(a[0])
if len(a)==1:
    print(a[0])
else:
    for i in range(1, len(b)-1):
        print(b[i-1]+b[i+1],end=' ')
