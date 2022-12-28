s = input()
a = ""
for i in s: 
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        a+="0"
    else:
        a+="1"

print(int(a,2))
