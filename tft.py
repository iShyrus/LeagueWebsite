import random
import requests
import json
import os
from pprint import pprint


apikey="RGAPI-ba9b3375-d6fe-42d7-87e3-18c2bdd25dd4"
name =input("Summoner Name: ")
accountInfo = requests.get("https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name/"+name+"?api_key="+apikey).json()
pprint(accountInfo)