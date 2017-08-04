import requests
f=open("input.txt")
r=requests.get(f.readline().strip())
print(r.text.strip().split()[0])
while True:
    r=requests.get("https://stepic.org/media/attachments/course67/3.6.3/"+r.text.strip().split()[0])
    print(r.text.strip())
    if r.text.strip().split()[0]=="We":
        break
print(r.text.splitlines())
f.close()

