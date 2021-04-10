#Import packages
import tkinter as tk
import bs4 as bs
import urllib.request as url
import pandas as pd


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
headingLabel = tk.Label(root, text="Yelp", font=('Helvetica', 20))
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

def yelp(urlLink):
    source = url.urlopen(str(urlLink))  
    page_soup = bs.BeautifulSoup(source, 'html.parser')
    allDiv = page_soup.find_all("div", {"class":"arrange-unit__09f24__3IxLD arrange-unit-fill__09f24__1v_h4 border-color--default__09f24__1eOdn"})
    nameList = []
    for div in allDiv:
        nameList.append(div.text)
    
    namesData = {'Company name':nameList}
    df = pd.DataFrame(namesData)    
    df.to_csv('Yelp_data.csv', mode='a', header=False)


#Function
def getData():
    url = urlValue.get()

    if (url):
        clearErrorLabel()
        
        try:
            yelp(url)
            errorLabel("File Saved", "green")
        except:
            errorLabel("There is some error!", "red")
    else:
        errorLabel("Please Enter All the values", "red")

#Button
submitButton = tk.Button(root, text="Submit", command=getData, bg="#30475e", fg="white", padx=20, pady=15, font=('Verdana', 12))
submitButton.grid(row=4, column=0, padx=40, pady=10)

root.mainloop()

