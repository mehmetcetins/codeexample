import datetime
import sys

tick_data = open("tick.txt","r+")
def check(data):
	yardim = False
	for line in data.readlines():
		if line[-4:-1] != "tmm":
			yardim = True
	if yardim :
		print("yardim alman gerek kardesim")
	data.close()

	

inp = sys.argv[1]
if (inp == "tmm"):
	tick_data.write(str(datetime.date.today()) + " tmm"+"\n")

if inp == "":
	tick_data.write(str(datetime.date.today())+"\n")

check(tick_data)
tick_data = open("tick.txt","r")

if inp == "listele":
	for line in tick_data.readlines():
		print(line)


tick_data.close()

