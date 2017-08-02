n=int(input())
s=0
for i in range(n+1):
    for j in range(i):
        s=s+1
        if s>n:
            break
        print(i,end=' ')