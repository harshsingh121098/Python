import urllib.request
from urllib import request

url= "http://samplecsvs.s3.amazonaws.com/TechCrunchcontinentalUSA.csv"

def download_data(csv_url):
    response =request.urlopen(csv_url)
    csv=response.read()
    csv_str=str(csv)
    lines = csv_str.split("\\n")
    dest_url= r"this.csv"
    fx=open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()
download_data(url)

