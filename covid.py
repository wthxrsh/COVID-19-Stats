from bs4 import BeautifulSoup
import requests
while True:


 a = input("Country: ")
 if a == 'usa':
     a = 'us'
 if a == "":
     print("Invalid!")
     break
 z = a.replace(" " , "-")

 r = z.replace("." , "")

 url = ("https://www.worldometers.info/coronavirus/country/" + r + "/")

 s = requests.get(url)
 soup = BeautifulSoup(s.content , 'html.parser')
#print(soup)

 cases = soup.find_all(id= 'maincounter-wrap')
 print ((cases[0]).get_text())
 print ((cases[1]).get_text())
 print ((cases[2]).get_text())

 b = input("Press 'r' to try again or press 'e' to exit: ")

 if b == 'r':
     print("Continue")
     continue
 elif b == 'e':
     print("Breaking...")
     break



