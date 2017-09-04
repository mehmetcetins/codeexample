import subprocess
import os

sira = open("sıra.txt","r")

sql = "mpc-hc_nvo"
siradaki = ""
for line in sira.readlines():
	if(line != "\n"):
		if line[-2] != "x":
			siradaki += line
			break

siradaki = "'" + siradaki[0:-1] + "'"
result = subprocess.check_output("find . | grep -i "+siradaki,shell=True)
result = '"'+str(result[0:-1],'utf-8')+'"'

os.system(sql+" "+result)



