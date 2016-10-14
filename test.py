import requests
import json
from bs4 import BeautifulSoup

url = "https://erp.iitkgp.ernet.in/StudentPerformance/view_performance.jsp?rollno=13MA20029"

content = requests.get(url)
soup = BeautifulSoup(content.text, 'lxml')

sgpa = soup.find_all("b",string = "SGPA")
cgpa = soup.find_all("b",string = " CGPA")
#print(cgpa)
for i,j in zip(sgpa,cgpa):
    i = i.find_parent("td")
    i = i.find_next_sibling("td")
    i = i.string
    j = j.find_parent("td")
    j = j.find_next_sibling("td")
    j = j.string
    print(i,j)
