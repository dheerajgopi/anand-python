import urllib
import re

def my_wget(url):
    file_name = url.split("/")[-1]
    return urllib.urlretrieve(url, file_name)

wpage = my_wget("http://anandology.com/python-practice-book/modules.html")
for lines in wpage:
    match = re.sub('<.*?>', '', lines)
    print match
