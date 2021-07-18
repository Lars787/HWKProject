import re
import time
def readHtmlFile(file):
    htmlContent = ""
    with open(file, "r") as htmlFile:
        htmlContent = htmlFile.read().replace('\n', '')
    return htmlContent

import csv
import requests
from bs4 import BeautifulSoup


header = ['name', 'mail', 'plz']
f = open(r'C:\Users\larsv\OneDrive\Dokumente\Python Scripts\Kalsruhe\Adressen2.csv', 'w') #Öffnen des Files wo reingeschrieben werden soll #Variabel
writer = csv.writer(f)
writer.writerow(header)


for i in range(38517,45000): #Variabel
    try:
        print(i)
        req = requests.get("https://www.hwk-karlsruhe.de/betriebe/marco-rohwedder-kraftfahrzeugtechnikermeister-63,0,bdbdetail.html?id=" + str(i)) #Variabel
        beautifulSoup = BeautifulSoup(req.content, "html.parser")


    #Name des Betriebs
        name = ''
        for ue in beautifulSoup.find_all('h1'):
            print(ue.text)
            name = '' + ue.text
            name = name.strip()
        if not name:
            continue
        mail = ''
    #Mail (clean von hwk)
        for tag in beautifulSoup.select('a[class*="mail"]'):
            print(tag.text)
            mail = '' + tag.text
            break

    #PLZ (not used)
        for ps in beautifulSoup.find_all("p"):
            fastPlz = ps
            break
        postleitzahl = re.findall('\d{5}',fastPlz.text)

        data = [name, mail, postleitzahl[0]]

        writer.writerow(data)
    except:
    #Manchmal wird eine Anfrage abgeblockt. Gibt dem Program eine kurze ruhe Pause vor dem neuen Anfragen.
        print('Es gab einen Fehler + 2 Minuten Pause')
        time.sleep(120)
        i = i + 1

f.close()
#print(req.status_code)
# der HTML Conent der Seite)
#print(req.content)

