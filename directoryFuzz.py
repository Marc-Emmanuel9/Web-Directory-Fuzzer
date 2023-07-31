import requests
import sys

# Variable
wordlist = ["tools-dump", "secure-development-lifecycle", "blabla"]
url = sys.argv[1]
exclude_status = [404]

def getStatus(url, word):
    if url[-1] == "/":
        rq = requests.get(url + word)
    else:
        rq = requests.get(url + "/" + word)
    
    return rq.status_code

for word in wordlist:
    result = getStatus(url, word)

    if int(result) not in exclude_status:
        if url[-1] == '/':
            print(f'[*]  {result} : {word} -> {url}{word}')
        else:
            print(f'[*]  {result} : {word} -> {url}/{word}')