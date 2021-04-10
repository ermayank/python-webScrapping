from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
import pandas as pd
import time
import os

driver.get("https://dir.indiamart.com/search.mp?ss=ceiling+tiles&src=as-popular%3Akwd%3Dceilingtiles%3Apos%3D1%3Acat%3D-2%3Amcat%3D-2")

storeDetails = driver.find_elements_by_class_name('clg')
names = driver.find_elements_by_class_name('lcname')
contactList = driver.find_elements_by_class_name('pns_h')

nameList = []
addressList = []
numbersList = []

for i in range(len(names)):
    
    name = names[i].text
    address = storeDetails[i].text
    contact = contactList[i].get_attribute("innerHTML")
    
    nameList.append(name)
    addressList.append(address)
    numbersList.append(contact)


    
# intialise data of lists.
data = {'Company Name':nameList,
        'Address': addressList,
        'Phone':numbersList}

# Create DataFrame
df = pd.DataFrame(data)

df.to_csv('demo.csv', mode='a', header=False)