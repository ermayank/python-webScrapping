import bs4 as bs
import urllib.request as url
import pandas as pd
source = url.urlopen('https://www.yelp.com/search?find_desc=Burgers&find_loc=Melbourne+Victoria&ns=1')  
page_soup = bs.BeautifulSoup(source, 'html.parser')

allDiv = page_soup.find_all("div", {"class":"arrange-unit__09f24__3IxLD arrange-unit-fill__09f24__1v_h4 border-color--default__09f24__1eOdn"})

nameList = []
for div in allDiv:
    nameList.append(div.text)
    # print(div + "\n")

namesData = {'Company name':nameList}

df = pd.DataFrame(namesData)
df.to_csv('Yelp_data.csv', mode='a', header=False)
