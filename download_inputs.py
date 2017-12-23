import requests

year = str(2016)

for day in range(1, 26):

    url = ''.join(['http://adventofcode.com/',year,'/day/',str(day),'/input'])

    cookie = {'session':'53616c7465645f5f3e26a2c9638628258749deecbf3ce79b1a2f15c0b6b20d7f1a4bade19854db90de7e414419ff91cb'}

    r = requests.get(url,cookies=cookie)

    path = ''.join(['./',year,'/','day',str(day),'/input.txt'])
    
    with open(path,'wb') as p:
        p.write(r.content)
