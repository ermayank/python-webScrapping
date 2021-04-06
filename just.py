#Imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import os

#User Inputs
url = input("Enter the query url : ")
sleep_time = int(input("Enter time (sec) to wait for complete loading : "))

#Driver Setup
print("Starting Driver\n")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
print("\nWaiting " + str(sleep_time) + "s to load page completely")
time.sleep(sleep_time)
print("\nStarting to save data !")

def strings_to_num(argument): 
    
    switcher = { 
        'dc': '+',
        'fe': '(',
        'hg': ')',
        'ba': '-',
        'acb': '0', 
        'yz': '1', 
        'wx': '2',
        'vu': '3',
        'ts': '4',
        'rq': '5',
        'po': '6',
        'nm': '7',
        'lk': '8',
        'ji': '9'
    } 
    
    return switcher.get(argument, "nothing")

storeDetails = driver.find_elements_by_class_name('store-details')


nameList = []
addressList = []
numbersList = []

for i in range(len(storeDetails)):
    
    name = storeDetails[i].find_element_by_class_name('lng_cont_name').text
    address = storeDetails[i].find_element_by_class_name('cont_fl_addr').get_attribute('innerHTML')
    contactList = storeDetails[i].find_elements_by_class_name('mobilesv')
    
    myList = []
    
    for j in range(len(contactList)):
        
        myString = contactList[j].get_attribute('class').split("-")[1]
    
        myList.append(strings_to_num(myString))

    nameList.append(name)
    addressList.append(address)
    numbersList.append("".join(myList))


    
# intialise data of lists.
data = {'Company Name':nameList,
        'Address': addressList,
        'Phone':numbersList}

# Create DataFrame
df = pd.DataFrame(data)

y = (url.split('.com'))[1].split('/')
fileName = y[1] + '_' + y[2] + '.csv'
df.to_csv(fileName, mode='a', header=False)
print("Data saved to " + fileName + "\nLocation : Same directory as this python program")