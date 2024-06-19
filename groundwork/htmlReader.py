import requests

def getHtml(urlString):
    """
    input: urlString (string) - the url of page for which we want the html code
    output: string - html code
    """
    response = requests.get(urlString)

    #comment/uncomment the following as required
    #return response.text #this returns html as a single string
    return response.text.split("\n") #this returns html as a list of strings. Each string in the list is a single line of html

print(getHtml("https://www.berkshirehathaway.com/"))
