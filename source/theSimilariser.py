import requests
from math import log

class Similariser:
    def __init__(self, term1 = "", term2 = ""):
        self.updateTerms(term1, term2)

    def updateTerms(self, term1, term2):
        self.term1 = term1
        self.term2 = term2

        self.url1 = "https://en.wikipedia.org/wiki/" + self.spaceToUnderscore(term1)
        self.url2 = "https://en.wikipedia.org/wiki/" + self.spaceToUnderscore(term2)

        self.linkSet1 = set(self.pagesLinkedFrom(self.url1))
        self.linkSet2 = set(self.pagesLinkedFrom(self.url2))

    def spaceToUnderscore(self, string):
        #replace all occurances of " " with "_" in a string
        returnString = ""
        for char in string:
            if char == " ":
                returnString += "_"
            else:
                returnString += char
        return returnString
    
    def pagesLinkedFrom(self, urlString):
        linkedPagesList = []
        response = requests.get(urlString)
        for line in response.text.split('href="/wiki/'):
            #each line is the start of a wikipedia page's name. The name ends with the occurance of a '"'
            linkedPagesList.append(line[:line.find('"')])
        #print(linkedPagesList)
        return linkedPagesList

    def calculateSimilarityCoefficient(self):
        return round(50*(log(len(self.linkSet1.intersection(self.linkSet2))) / log(len(self.linkSet1)) + log(len(self.linkSet2.intersection(self.linkSet1))) / log(len(self.linkSet2))))