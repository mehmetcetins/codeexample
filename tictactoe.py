liste = [2,2,2
		,2,2,2
		,2,2,2]

oyuncu = int(input()) - 1
liste[oyuncu] = 0

def tictactoeprint(arr):
	print("\n",arr[0],arr[1],arr[2],"\n",arr[3],arr[4],arr[5],"\n",arr[6],arr[7],arr[8])

def tictacwin(arr):
	win =0
	c = False
	lis = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[2,4,6],[0,4,8]]

	for i in lis:
		for k in i:
			if arr[k] == 0:
				win += 1
				if win == 3:
					c = True
					break
		if win != 3 :
			win = 0
	return c



a = True
while a :
	tictactoeprint(liste)
	oyuncu = int(input()) - 1
	liste[oyuncu] = 0
	if tictacwin(liste):
		a = False
		print ("kazanan var")
		tictactoeprint(liste)
