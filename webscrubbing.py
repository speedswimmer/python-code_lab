#Programm ließt get-pip.py von der Webseite und erstellt eine lokale Datei!
import urllib.request
import urllib.error
import sys, os

def program_stop():
    print("Programm beendet!")
    sys.exit()

eingabe = input(str("Nach welchem Produkt soll gesucht werden? "))
crawl_URL = "https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=NEC+" + eingabe

print (crawl_URL)

try:
    webURL = urllib.request.urlopen(crawl_URL)
except urllib.error.URLError as e:
    print("Webseite kann nicht geöffnet werden -", e.reason)
    program_stop()
except urllib.error.HTTPError as e:
    print("Webserver kann die Anfrage nicht auflösen.", e.reason)
    program_stop()

webcode = webURL.getcode()
if webcode == 200:
    print("Webseite ist erreichbar:", webcode)
elif webcode == 404:
    print("URL existiert nicht!")
else:
    print("...etwas ist schief gelaufen!")
content = webURL.read().decode("utf-8")

print(type(content), len(content))

print("Webseite wurde gelesen!")

f = open("crawl_result.html", "w", encoding="utf-8")
f.write(content)
f.close()

pfad = os.getcwd()

if os.path.isfile(pfad + "\crawl_result.html") == True:
    print("Das Crawl-Resultat kann im Broswer geöffnet werden")
else:
    print("Datei existiert scheinbar nicht!")
#'os.system('start chrome "c:\Benutzer\Lenimo\PycharmProjects\ErstesProjekt\crawl.results.html"')

webURL.close()

# Crawl-Resultate werden gelesen und analysiert
s = open(pfad + "\crawl_result.html","r", encoding="utf-8")
list = s.read()
lange = len(list)

#print(list.index("offerList-itemWapper"))
s.close()
