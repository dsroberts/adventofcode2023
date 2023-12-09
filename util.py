import requests

def get_day(day):
    with open('session.txt','r') as f:
        s = f.read()   
    r = requests.get(f"https://adventofcode.com/2023/day/{day}/input",cookies={'session':s})
    return r.text.splitlines()

def submit_answer(answer,day,part):
    with open('session.txt','r') as f:
        s = f.read()
    r = requests.post(f"https://adventofcode.com/2023/day/{day}/answer",data=f"level={day}&answer={answer}",cookies={'session':s},allow_redirects=False)
    if r.status_code == 302:
        return "Answer already submitted or malformed data"
    return r.text