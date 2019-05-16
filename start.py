# -*- coding: utf-8 -*-
import getlist,download,time,database
getlist.name="进击的巨人"
getlist.zimuzu = "星空字幕组"
link = getlist.link
day = 0
getlist.getList(getlist.name)
#print(link)
print(day)
dl_list = database.load(day)
print(dl_list)
#download.aria2(link[0])