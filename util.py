import requests

def get_day(day):
    with open('session.txt','r') as f:
        s = f.read()   
    r = requests.get(f"https://adventofcode.com/2023/day/{day}/input",cookies={'session':s})
    return r.text.splitlines()