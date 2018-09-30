import csv
import os
import sys
from urllib import urlopen
import json
from bs4 import BeautifulSoup
import requests


url_prefix = "http://stats.nba.com/stats/playbyplayv2?EndPeriod=10&EndRange=55800&GameID="
url_end = "&RangeType=2&SeasonType=Regular+Season&StartPeriod=1&StartRange=0"
game_id = sys.argv[1]

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}


url = url_prefix+game_id+url_end
r = requests.get(url,headers=headers)
content = r.json()
s = []
try:
	team1 = content["resultSets"][0]["rowSet"][1][17]
except:
	print "Index Out of Range: " + game_id
	return
team2 = content["resultSets"][0]["rowSet"][1][24] 
team3 = content["resultSets"][0]["rowSet"][1][31]
s.append(team1)
if ((team2 not in s) and team2 != None):
	s.append(team2)
if ((team3 not in s) and team3 != None):
	s.append(team3)
try:
	team1 = content["resultSets"][0]["rowSet"][2][17]
except:
	print "Index Out of Range: " + game_id
	continue
team2 = content["resultSets"][0]["rowSet"][2][24] 
team3 = content["resultSets"][0]["rowSet"][2][31]
s.append(team1)
if ((team2 not in s) and team2 != None):
	s.append(team2)
if ((team3 not in s) and team3 != None):
	s.append(team3)
#print s
home = s[0]
if (len(s) == 1):
	away = s[0]
	print "Duplicate Home-Away:" + game_id
else:
	away = s[1]
header = content["resultSets"][0]["headers"]
content = content["resultSets"][0]["rowSet"]
result.append(header)
result = result + content
try:
	print game_id
	file = open(season+"/"+game_id+"_"+home+"_"+away+"_"+".bsv","wb")
	writer = csv.writer(file,delimiter="|")
	for row in result:
		writer.writerow(row)
	file.close()
except:
	print "Null Team Names: " + game_id 
