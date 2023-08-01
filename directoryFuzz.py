import requests, sys, os

def progress_bar(current, total, bar_length=20):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'Progress: [{arrow}{padding}] {current}/{total}', end=ending)

def getWordlist(path):
    
    file = open(path, "r")

    wordlist = []

    for word in file.readlines():
        if '\n' in word:
            wordlist.append(word[:-1])
        else:
            wordlist.append(word)

    return wordlist

defaultPath = [os.path.dirname(os.path.realpath(__file__)) + "\wordlist\default.txt"]
url = sys.argv[1]
exclude_status = [404]
wordlist = getWordlist(defaultPath[0])

def getStatus(url, word):
    if url[-1] == "/":
        rq = requests.get(url + word)
    else:
        rq = requests.get(url + "/" + word)
    
    return rq.status_code

for idx, word in enumerate(wordlist, start=1):

    result = getStatus(url, word)

    if int(result) not in exclude_status:
        if url[-1] == '/':
            print(f'[*]  {result} : {word} -> {url}{word}')
        else:
            print(f'[*]  {result} : {word} -> {url}/{word}')
    
    progress_bar(idx, len(wordlist), bar_length=20)