import random
import urllib.request

def download(url):
    name= random.randrange(1,1000)
    full_name=str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)

download("https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT2YUtQXQkwC_fR2yBMgC2sCtIDsS5wLgU0aUbTlZ3hROLiNZsS")