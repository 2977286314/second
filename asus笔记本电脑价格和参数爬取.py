import requests
from lxml import etree
import csv
url="https://www.asus.com.cn/store/gallery-1.html"
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

res=requests.get(url,headers=header)
res.encoding='utf-8'
html=etree.HTML(res.text)
notebooks=html.xpath("/html/body/div[2]/div[1]/div[3]/div[2]/div/div/div[3]/div[1]/ul/li")
f=open("notebooks.csv",mode="w")
write=csv.writer(f)
notebook_list=[]
for notebook in notebooks[1:]:
    name=notebook.xpath("./div[2]/h3[1]/a/p[1]/text()")[0]
    parameter="-".join(notebook.xpath("./div[2]/h3[1]/a/p[2]/text()"))
    price=notebook.xpath("./div[2]/div/ins/text()")[0].strip("￥")
    notebook_list.append([name,parameter,price])
for book in notebook_list:
    write.writerow(book)
f.close()