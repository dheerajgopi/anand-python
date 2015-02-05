import urllib

def my_wget(url):
    file_name = url.split("/")[-1]
    return urllib.urlretrieve(url, file_name)

my_wget("http://anandology.com/python-practice-book/modules.html")
