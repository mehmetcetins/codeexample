from exampleClass import example

a = [5,4,11,3,14,10,6,12,20,15,9,1]

aleft = []
aright = []
for i in range(0,int(len(a)/2)):
    aleft.append(a[i])
for i in range(int(len(a)/2),len(a)):
    aright.append(a[i])

aleft = sorted(aleft)
aright = sorted(aright)

x = y = 0
result = []

while x < len(aleft) and y < len(aright):
    if aleft[x] < aright[y]:
        result.append(aleft[x])
        x+=1
    else : 
        result.append(aright[y])
        y+=1
if (y < len(aright)):
    for i in range(y,len(aright)):
        result.append(aright[y])

print(result , len(result))