from bs4 import BeautifulSoup
import requests
from pprint import pprint

depart = "Shinjuku+Station"
arrive = "Daitabashi+Station"

# mapsUrl = f"https://www.google.com/maps/dir/Daitabashi+Station,+2-ch%C5%8Dme-18+%C5%8Chara,+Setagaya+City,+T%C5%8Dky%C5%8D-to+156-0041/Shinjuku+Station,+3+Chome-38-1+Shinjuku,+Shinjuku+City,+Tokyo+160-0022/@35.6803947,139.6621684,14z/data="
mapsUrl = f"https://www.google.com/maps/dir/{depart}/{arrive}"

req = requests.get(mapsUrl)
pprint(req.content)

# soup = BeautifulSoup(req, "html.parser")
# print(soup.prettify())



