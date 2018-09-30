import csv
import os
import sys
from urllib import urlopen
import json
from bs4 import BeautifulSoup
import requests


url_prefix = "http://stats.nba.com/stats/playbyplayv2?EndPeriod=10&EndRange=55800&GameID="
url_end = "&RangeType=2&SeasonType=Regular+Season&StartPeriod=1&StartRange=0"
game_id = str(sys.argv[1])

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}


url = url_prefix+game_id+url_end
r = requests.get(url,headers=headers)
content = r.json()
print len(content["resultSet"][0]["rowSet"])
