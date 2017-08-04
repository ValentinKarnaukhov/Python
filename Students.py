d={}
countmath=0
countphis=0
countruss=0
with open("input.txt",'r') as inf:
    for line in inf:
        line=list(line.strip().split(';'))
        d[line[0]] = [int(line[1]), int(line[2]), int(line[3])]
for value in d.values():
    print((value[0]+value[1]+value[2])/3)
    countmath += value[0]
    countphis += value[1]
    countruss += value[2]
print(countmath/len(d),countphis/len(d),countruss/len(d))
