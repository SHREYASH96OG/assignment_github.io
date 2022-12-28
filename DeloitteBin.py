n = int(input())
m = int(input())
for i in range(n+1,m):
    b=bin(i)[2:]
    flag=1
    for j in range(1,len(b)):
        if(b[j-1]=="1" and b[j]=="1"):
            flag=0
            break
    if(flag):
        print(b)
