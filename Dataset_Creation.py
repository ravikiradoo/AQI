from bs4 import BeautifulSoup

data=open("./DATA/HTML/{}/{}.html".format(2013,1),"rb")
soup = BeautifulSoup(data,'html.parser')
results = soup.find('table',attrs={'class':'medias mensuales numspan'}).find_all('tr')
data= []
for row in results:
    data.append([col.text for col in  row.find_all('td')])
print(data)
