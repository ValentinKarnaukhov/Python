n=int(input())
d={}
for i in range(n):
    a=int(input())
    if a in d:
        print(d[a])
    else:
        d[a]=f(a)
        print(d[a])