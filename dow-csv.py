from urllib.request import urlretrieve
for x in range(5):
    url = 'http://localhost:8888/?format=csv&q=[twitter:maroc]&pageno='+str(x) 
    dst = 'omacsvfile'+str(x)+'.csv'
    urlretrieve(url, dst)
