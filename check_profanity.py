import urllib.request

def read_text():
    quotes = open("/Users/danielchang/Python/movie_quotes.txt")
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    url = "http://www.wdylike.appspot.com?"
    values = {'q':text_to_check}
    data = urllib.parse.urlencode(values)
    connection = urllib.request.urlopen(url+data)
    respData = connection.read()
    respData = respData.decode("utf-8")
    if "true" in respData:
        print("Profanity Alert!!")
    elif "false" in respData:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")

read_text()
