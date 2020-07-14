from bs4 import BeautifulSoup
import requests


a = input('Country: ')

z = a.replace(" " , '-')


url = ('https://www.worldometers.info/coronavirus/country/' + z + "/")

s = requests.get(url)
print (s)