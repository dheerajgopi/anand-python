import urllib
import re

def my_wget(url):
    file_name = url.split("/")[-1]
    return urllib.urlretrieve(url, file_name)

wpage = my_wget("http://anandology.com/python-practice-book/modules.html")

match = re.sub('<.*?>', '', wpage)

print match
