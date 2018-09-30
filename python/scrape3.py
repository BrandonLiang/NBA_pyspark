import csv
import requests

game_id = "0041500101"

url_prefix = "http://stats.nba.com/stats/playbyplayv2?EndPeriod=10&EndRange=55800&GameID="
url_end = "&RangeType=2&Season=2015-16&SeasonType=Regular+Season&StartPeriod=1&StartRange=0"

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}

#file = open("all_game_id.csv","rb")
#reader = csv.reader(file)
#output = open("all_games.csv","wb")
#writer = csv.writer(output)
#writer.writerow(["Game ID","Home Team","Away Team"])
s = []

url = url_prefix + game_id + url_end
#print url
r = requests.get(url,headers=headers)
content = r.json()
print content
#team1 = content["resultSets"][0]["rowSet"][1][17]
#team2 = content["resultSets"][0]["rowSet"][1][24] 
#team3 = content["resultSets"][0]["rowSet"][1][31]
#s.append(team1)
#if ((team2 not in s) and team2 != None):
#	s.append(team2)
#if ((team3 not in s) and team3 != None):
#	s.append(team3)
#team1 = content["resultSets"][0]["rowSet"][2][17]
#team2 = content["resultSets"][0]["rowSet"][2][24] 
#team3 = content["resultSets"][0]["rowSet"][2][31]
#s.append(team1)
#if ((team2 not in s) and team2 != None):
#	s.append(team2)
#if ((team3 not in s) and team3 != None):
#	s.append(team3)
##print s
#home = s[0]
#if (len(s) == 1):
#	away = s[0]
#else:
#	away = s[1]
#print [number,home,away]
#writer.writerow([number,home,away])


#file.close()
#output.close()
