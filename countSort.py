

a = [5,7,5,6,7,8,9]
b = [0,0,0,0,0,0,0,0,0,0]

for i in range(0,11):
    for k in a :
        if i == k :
            b[i]+=1
a = []
for i in range(0,len(b)):
    if b[i] != 0:
        for k in range(0,b[i]):
           a.append(i) 

print(a)