# -*- coding: utf-8 -*-
import pickle
try:
    f = open('db.db','rb')
    data = pickle.loads(f.read())
except :
    data=[[]for i in range(7)]

dic={}
def dump(name,zimuzu,day):
    f = open('db.db','wb')
    dic[name] = zimuzu
    if dic not in data[int(day)]:
        data[int(day)].append(dic)
    f.write(pickle.dumps(data))
    f.close()

def load(day):
    if day!=None:
        return data[int(day)]
    else:
        return data
