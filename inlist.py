a=[int(i) for i in input().split()]
n=int(input())
if n in a:
    while n in a:
        print(a.index(n),end=' ')
        a[a.index(n)]='*'
else:
    print("Отсутствует")
