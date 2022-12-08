from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(executable_path="Downloads")
driver.get("https://www.nytimes.com/international/")

Data=driver.page_source
allData=''.join(Data)

arrhead=[]
soup=BeautifulSoup(allData,'html.parser')
for d in soup.find_all('div',id='app'):
    title=d.find_all('h3')
for u in range(len(title)):
    arrhead.append(title[u].text)
print("this is heading",arrhead)
arrpara=[]

for d in soup.find_all('div',id='app'):
    t1=d.find_all('p')
for i in range(len(t1)):
    arrpara.append(t1[i].text)
print("this is paragraph",arrpara)
arrlink=[]


for d in soup.find_all('div',id='app'):
    t2=d.find_all('a')
for i in range(len(t2)):
    arrlink.append(t2[i].get('href'))
print("this is time",arrlink)