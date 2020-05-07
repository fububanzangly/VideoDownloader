# -*- coding: utf-8 -*-
import getlist,download,time,database
dl_list = database.load(0)
for name in dl_list:
    for key in name:
        print(key + "==>"+name[key])
        getlist.name = key
        getlist.zimuzu = name[key]
        link = getlist.link
        getlist.getList(getlist.name)
        print(link)
#download.aria2(link[0])