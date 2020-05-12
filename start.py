# -*- coding: utf-8 -*-
import website.dongmanhuayuan,download_plugins.aria2,time,database
dl_list = database.load(0)
for name in dl_list:
    for key in name:
        print(key + "==>"+name[key])
        website.dongmanhuayuan.name = key
        website.dongmanhuayuan.zimuzu = name[key]
        link = website.dongmanhuayuan.link
        website.dongmanhuayuan.getList(website.dongmanhuayuan.name)
        print(link)
#download_plugins.aria2.download(link[0])