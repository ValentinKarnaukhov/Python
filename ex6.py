stk=input()
res=''
counter=0
if len(stk)==1:
    print(stk+'1')
else:
    for i in range(0,len(stk)-1):
        if stk[i]==stk[i+1]:
            counter+=1
        else:
            res=res+stk[i]+str(counter+1)
            counter = 0
    res=res+stk[i+1]+str(counter+1)
    print(res)
