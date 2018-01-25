import requests, sys

year = sys.argv[1]

for day in range(1, 26):

    url = ''.join(['http://adventofcode.com/',year,'/day/',str(day),'/input'])

    cookie = {'session':''}

    r = requests.get(url,cookies=cookie)

    path = ''.join(['./',year,'/','day',str(day),'/input.txt'])
    
    with open(path,'wb') as p:
        p.write(r.content)
