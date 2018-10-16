import json
import urllib
import time
import requests

key = '9hz5rkaibpmefpic7xdabqffvxmiwhjo'
url = 'http://api.filmtotaal.nl/filmsoptv.xml?apikey=9hz5rkaibpmefpic7xdabqffvxmiwhjo&dag=15-10-2018&sorteer=1'
ass = requests.get(url)
sas = json.load(url)
print(sas)