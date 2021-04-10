from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import tkinter as tk
driver = webdriver.Chrome(ChromeDriverManager().install())
import pandas as pd
import time
import os


#Setup Tkinter window
root = tk.Tk()
root.title("CALINFO")

w=1000
h=800

#Screen Width and Height
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

#X and Y coordinates for root Tkinter window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w,h,x,y))

#Heading
headingLabel = tk.Label(root, text="Google My Buisness", font=('Helvetica', 20))
headingLabel.grid(row=0, column=0, padx=30, pady=10)
#Input Url label + textbox
inputLabel = tk.Label(root, text="Enter the query url", font=(15))
inputLabel.grid(row=1, column=0, padx=10, pady=10)

urlValue = tk.Entry(root, width=50, borderwidth=3)
urlValue.grid(row=1, column=1, pady=10)


msgLabel = tk.Label(root, text="Message : ", font=(15))
msgLabel.grid(row=3, column=0, pady=20, padx=10)

#Dynamic message function
def errorLabel(msg, rang):
    global eLabel
    eLabel = tk.Label(root, text=msg, fg=rang, font=18)
    eLabel.grid(row=3, column=1, pady=20, padx=10)

#Clear the label
def clearErrorLabel():
    eLabel = tk.Label(root, text="", font=18)
    eLabel.destroy()

def googleData(url):
    driver.get(str(url))

    nameList = []

    storeNames = driver.find_elements_by_class_name('rllt__link')
    for j in range(len(storeNames)):
        name = storeNames[j].text
        nameList.append(name)

    namesData = {'Company name':nameList}

    # Create DataFrame
    df = pd.DataFrame(namesData)
    df.to_csv('Google_data.csv', mode='a', header=False)

def getData():
    url = urlValue.get()

    if (url):
        clearErrorLabel()
        
        try:
            googleData(url)
            errorLabel("File Saved", "green")
        except:
            errorLabel("There is some error!", "red")
    else:
        errorLabel("Please Enter All the values", "red")

#Button
submitButton = tk.Button(root, text="Submit", command=getData, bg="#30475e", fg="white", padx=20, pady=15, font=('Verdana', 12))
submitButton.grid(row=4, column=0, padx=40, pady=10)

root.mainloop()

