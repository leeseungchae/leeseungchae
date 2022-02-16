from email import header
from bs4 import BeautifulSoup
import requests

url="https://www.genie.co.kr/chart/top200"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
idx=1

images = soup.find_all("a",{"class":"cover"})
titles = soup.find_all("a",{"class":"title ellipsis"})

for image ,title in  zip(images,titles):
    img_url = image.find("img")["src"]
    title = title.get_text().strip()
    
    if img_url and title:
        
        img_res = requests.get("https:"+img_url)
        img_res.raise_for_status()
        

        with open("{}.jpg".format(title),"wb") as f :
            f.write(img_res.content)
            idx = idx+1
        if(idx==50):
            break
    else :
        continue

        
    
     
