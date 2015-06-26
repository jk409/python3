#coding=utf-8
__author__ = 'Administrator'
#python -m http.server
#
#E-mail:jk409@qq.com
import json,pymongo
fls='k.json'
def tt():
    with open(fls,'r') as f:
        print(f.readlines())

def jx_json(arg):
    res=json.load(open(fls, 'r'))
    return res[arg]

def pgo():
    cnn=pymongo.MongoClient()
    res = cnn.kkk.data.find()
    for i in res:
        print(i)


def ref():
    ls=[]
    file='./test.cfg.txt'
    with open(file) as f:
        res=f.read().split()
    print('总行数：',len(res))
    for i in res:
        i=i.split('|')
        i.pop()
        ls.append(i)
        print('生成列表',i)
    print(ls, '\n',)

def test():
    res='3.9M    tomcat.out'
    s=res.split('M')
    if eval(s[0]) >=  10:
        print('>10')
    else:
        print('<10')


if __name__ == "__main__":
    test()