# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
url = "https://www.dongmanhuayuan.com/search/"
name=""
zimuzu = ""
list=[]
link = []
addrDic={}
linkUrl = []
def getList(name):
    newurl=url+name
    htmlfile = open("temp.html", 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    reg = requests.get(url=newurl, allow_redirects=False)
    soup = BeautifulSoup(reg.text, 'html5lib')
    for link in soup.select('li[class="uk-grid uk-grid-collapse"]'):
        list.append(link.select('a[class="uk-text-break"]'))
    with open("temp.html", 'w',encoding='utf-8') as f:
        for i in list:
            f.write(str(i)[1:-1]+"\n")
    f.close()
    lssoup=BeautifulSoup(htmlhandle, 'html5lib')
    index = 0
    for l in lssoup.select("a"):
        title="$"+str(index)+"$"+l.get("title")[5:-4]
        link="https://www.dongmanhuayuan.com"+l.get("href")
        addrDic[title]=link
        index = index+1
    getVideo(zimuzu)
def getVideo(zimuzu):
    for key,value in addrDic.items():
        if zimuzu in key:
            linkUrl.append(value)
        else:
            pass
    getLink(linkUrl[0])


def getLink(linkUrl):
    reg = requests.get(linkUrl, allow_redirects=False)
    soup = BeautifulSoup(reg.text, 'html5lib')
    linktmp = soup.select("input[class='uk-input uk-form-width-large']")
    for i in linktmp:
        link.append(i.get("value"))




