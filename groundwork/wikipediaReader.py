import requests

def getWikipediaHtml(urlString):
    response = requests.get(urlString)

    #we split the html code using "<li><a href="/wiki/" as our delimiter. This is an odd choice, but suits our purpose

    return response.text.split('href="/wiki/')

def readWikipediaPage(pageTitle):
    linkedPagesList = []
    lineList = getWikipediaHtml("https://en.wikipedia.org/wiki/" + pageTitle)
    for line in lineList:
        #each line is the start of a wikipedia page's name. The name ends with the occurance of a '"'
        linkedPagesList.append(line[:line.find('"')])
    return linkedPagesList

for item in readWikipediaPage("kilwinning"):
    print(item)