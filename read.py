with open("input.txt") as inf:
    s=inf.readline().strip()

with open("output.txt", "w") as out:
    for i in range(len(s)-1):
        res=0
        count=0
        if not s[i].isdigit():
            char=s[i]
            if i<len(s)-1:
                i+=1
            while s[i].isdigit():
                count=count*(10**res)+int(s[i])
                res+=1
                if i < len(s) - 1:
                    i += 1
                else:
                    break
            out.write(char*count)


print(s)