import csv
import json
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

csvfile = open(file1, 'r')
jsonfile = open(file2, 'w')

fieldnames = ("Player","Pos","Age","Tm","G","GS","MP","FG","FGA","FG%","3P","3PA","3P%","2P","2PA","2P%","eFG%","FT","FTA","FT%","ORB","DRB","TRB","AST","STL","BLK","TOV","PF","PS/G")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
  json.dump(row, jsonfile)
  jsonfile.write('\n')
