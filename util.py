import requests

def get_day(day):
    with open('session.txt','r') as f:
        s = f.read()   
    r = requests.get(f"https://adventofcode.com/2023/day/{day}/input",cookies={'session':s})
    return r.text.splitlines()

def submit_answer(answer,day,part):
    ### Doesn't work
    with open('session.txt','r') as f:
        s = f.read()
    r = requests.post(f"https://adventofcode.com/2023/day/{day}/answer",data=f"level={day}&answer={answer}",cookies={'session':s})
    return r