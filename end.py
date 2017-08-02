b=[]
while True:
    a=input()
    if a=='end':
        break
    else:
        b.append([int(i) for i in a.split()])
c=[[0 for j in range(len(b[i]))] for i in range(len(b))]
t=len(c)
k=len(c[0])
for i in range(-1,-len(b)-1,-1):
    for j in range(-1,-len(b[i])-1,-1):
        c[i][j]=b[(i-1)%t][j%k]+b[(i+1)%t][j%k]+b[i%t][(j-1)%k]+b[i%t][(j+1)%k]
for i in range(len(b)):
    for j in range(0,len(b[i])):
        print(c[i][j],end=' ')
    print()