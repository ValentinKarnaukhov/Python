a=input()
b=input()
c=input()
d=input()
dict={}
p=''
r=''
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
for i in range(len(a)):
    dict[a[i]]=b[i]
for i in c:
    p+=dict[i]
for i in d:
    r+=get_key(dict,i)
print(p)
print(r)