import requests

def getHtml(urlString):
    """
    input: urlString (string) - the url of page for which we want the html code
    output: string - html code
    """
    response = requests.get(urlString)

    return response.text

print(getHtml("https://www.berkshirehathaway.com/"))
