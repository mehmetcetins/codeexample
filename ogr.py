import requests
from bs4 import BeautifulSoup
import time

def login():
    with requests.Session() as s:
        ogr = s.get("https://ogr.nku.edu.tr")
        soup = BeautifulSoup(ogr.text,'html.parser')
        dogkod = soup.find(id="dogrulama").parent.find("div").string

        payload = {"form1":"",'girisyap':'G İ R İ Ş','dogrulama':str(dogkod) ,'email': '1170606033', 'sifre': '98mehmet',"unut":''}
        cookies = dict(ogr.cookies)
        print(dogkod)
        r = s.post('https://ogr.nku.edu.tr', data= payload)
        r = s.post('https://ogr.nku.edu.tr/ogrencidonemnotdurumu.php')
        r.encoding="utf-8"
    return r.text


def ogr(htmlc):
    soup = BeautifulSoup(htmlc,'html.parser')
    notlar = []
    for i in range(7):
        if soup.find(id="dataTablosu").find_all("td")[i*11 + 4].string != None:
            notlar.append([soup.find(id="dataTablosu").find_all("td")[i*11 + 2].string,soup.find(id="dataTablosu").find_all("td")[i*11 + 4].string])
    return notlar



def pshnot(nts,cch):
    c=""
    if nts == 0:
        for k in cch:
            c+=k[0] + " : " +k[1]+" "
    else :
        for i in nts:
            varmi = False
            for k in cch:
                if i[0] != k[0] :
                    varmi = True
            if varmi:
                c+=i[0] + " : " +i[1]+" "
     
    payload = { "app_key": "ppSP1ZVlsEKuP9vRwdSa",
    "app_secret": "yqsxeDDlYKTYamWrueDCCVlRP1DCoio5lwjCDKoSHAc0IXe7aBevHorkblaJU75o",
    "target_type": "app",
    "content": c 
    }
    r = requests.post("https://api.pushed.co/1/push", data=payload)
    print(r.text)

cache = ogr(login())
pshnot(0,cache)
time.sleep(600)


while True:
    a = ogr(login())
    if len(cache) != len(a):
        psh(a,cache)
    time.sleep(600)    
    

