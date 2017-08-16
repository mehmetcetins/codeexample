from exampleClass import example

a = [26,33,35,29,19,12,22]

p = a[0]
a = example.swit(0,example.middle(a),a)


for i in range(0,len(a)):
    p = a[0]
    a = example.swit(0,example.middle(a),a)
    if a[i] != p:

        if a[i] < p:
            a = example.swit(len(a) - i - 1,  i,a)
        if a[-( i + 1 ) ] < p:
            a = example.swit(len(a) - i - 1,  i,a)
        if a[i] > p:
            a = example.swit(len(a) - i - 1,  i,a)
        if a[-( i + 1 )] > p:
            a = example.swit(len(a) - i - 1,  i,a)
p = a[0]
a = example.swit(0,example.middle(a[0:example.middle(a)]),a)


print (a)