# -*- coding: utf-8 -*-
import pickle
try:
    f = open('db.db','rb')
    data = pickle.loads(f.read())
    f.close()
except :
    f = open('db.db','wb')
    data=[[]for i in range(7)]
    f.write(pickle.dumps(data))
    f.close()


def dump(name,zimuzu,day):
    dic = {}
    f = open('db.db','wb')
    dic[name] = zimuzu
    if dic not in data[int(day)]:
        data[int(day)].append(dic)
    f.write(pickle.dumps(data))
    f.close()

def load(day):
    f = open('db.db', 'rb')
    if day!=None:
        f.close()
        return data[int(day)]
    else:
        f.close()
        return data
