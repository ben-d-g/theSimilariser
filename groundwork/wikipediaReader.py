import requests

def getWikipediaHtml(urlString):
    response = requests.get(urlString)

    #we split the html code using "<li><a href="/wiki/" as our delimiter. This is an odd choice, but suits our purpose

    return response.text.split('href="/wiki/')

def readWikipediaPage(pageTitle):
    linkedPagesList = []
    lineList = getWikipediaHtml("https://en.wikipedia.org/wiki/" + pageTitle)
    for line in lineList:
        #print(line)
        #print("------------------------------------------")
        linkedPagesList.append(line[:line.find('"')])
        #print(line[:line.find('"')])
    linkedPagesList.sort()
    return linkedPagesList

for item in readWikipediaPage("kilwinning"):
    print(item)