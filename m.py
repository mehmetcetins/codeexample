liste = []
print(414/60)
a = True
while (a):
	b = input()
	if b == "bitti":
		a = False
	else :
		sok = b
		sok = sok.split(" ")
		sok[1] = int(sok[1]) 
		liste.append(sok)
t = 0

for i in range(0,len(liste)):
	t += liste[i][1]
liste.append(t)
print(liste)