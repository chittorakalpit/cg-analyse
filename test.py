import requests
import json
from bs4 import BeautifulSoup

dep = input("Enter department code in 2 letters. e.g. MA/CS/GG ")
for i in range(1,20):
    j = str(i).rjust(2, '0')
    rollno = "15"+dep+"200"+j
    url = "https://erp.iitkgp.ernet.in/StudentPerformance/view_performance.jsp?rollno="+rollno
    filename = dep+'.txt'
    f=open(filename,'w')
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'lxml')

    sgpa = soup.find_all("b",string = "SGPA")
    cgpa = soup.find_all("b",string = " CGPA")
    sgpa.reverse()
    cgpa.reverse()
    f.write('cgpa sgpa \n')
#print(cgpa)
    for i,j in zip(sgpa,cgpa):
        i = i.find_parent("td")
        i = i.find_next_sibling("td")
        i = i.string
        j = j.find_parent("td")
        j = j.find_next_sibling("td")
        j = j.string
        print(i+' '+j+',')
        f.write(i+' '+j+',')
    f.write('\n') 
f.close()
print('Done!')
