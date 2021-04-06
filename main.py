import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?tbs=lf:1,lf_ui:2&tbm=lcl&sxsrf=ALeKk02yKYXiBftFCy96FJMs7fiVXYD0YA:1617694031088&q=IELTS+near+me&rflfq=1&num=10&sa=X&ved=2ahUKEwiSuM_wi-nvAhUWxDgGHQHBDSoQjGp6BAgXEGI&biw=1920&bih=939#rlfi=hd:;si:;mv:[[29.977438199999998,76.88911999999999],[29.967082500000004,76.8266324]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2'

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

# print(soup)

#Title of HTML page
title = soup.title

#Get all Paragraphs
paras = soup.find_all('p')

#Get all anchor tags
anchors = soup.find_all('a')
print(anchors)
all_links = set()
for link in anchors:
    if(link != '#'):
        all_links.add(link.get('href'))

titles = soup.find(class_='dbg0pd').content
print(titles)

