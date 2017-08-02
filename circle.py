n=int(input())
arr = [[None]* n for j in range(n)]
x,y=0,0
dx,dy=1,0
for i in range(1,n**2+1):
    arr[x][y]=i
    nx,ny=x+dx,y+dy
    if 0<=ny<n and 0<=nx<n and arr[nx][ny]==None:
        x,y=nx,ny
    else:
        dx,dy=-dy,dx
        x,y=x+dx,y+dy
for i in range(n):
    for j in range(n):
        print(arr[j][i],end=' ')
    print()