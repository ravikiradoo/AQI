import os
import time
import requests
import sys

def download_html():
    url = ""
    for year in range(2013,2019):
        for month in range(1,13):
            if month < 10 :
                url = "https://en.tutiempo.net/climate/0{}-{}/ws-421810.html".format(month,year)
            else:
                url = "https://en.tutiempo.net/climate/{}-{}/ws-421810.html".format(month,year)
            html = requests.get(url).text.encode('utf-8')
        
            path = './DATA/HTML/{}'.format(year)
            if not os.path.exists(path):
                os.makedirs(path)
            
            with open("./DATA/HTML/{}/{}.html".format(year,month),"wb") as output:
                output.write(html)
    
    sys.stdout.flush()

if __name__ == '__main__':
    download_html()