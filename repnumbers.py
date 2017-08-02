a=[int(i) for i in input().split()]
a.sort()
s=1
a.append(a[len(a)-1]+1)
for i in range(0, len(a)-1):
    if a[i]==a[i+1]:
        s += 1
    else:
        if s>1:
            print(a[i-1],end=' ')
        s=1
