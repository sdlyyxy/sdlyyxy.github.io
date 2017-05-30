#-*_coding:utf8-*-

import yaml
import os
import sys


tagSet = set()


def check(filename):
    print(filename)
    f = open(filename,encoding="utf8")
    s = ''
    time = 0
    while(True):
        tmp = f.readline()
        # print(tmp)
        if tmp[0] == '-':
            time = time + 1
        s = s + tmp
        if time == 2:
            break
    data = yaml.load_all(s)
    time = 0
    for i in data:
        if time >= 1:
            break
        time = time + 1
        for j in i['tag']:
            tagSet.add(j)
    # for i in tagSet:
        # print(i)


for root, dirs, files in os.walk('./_posts'):
    for filename in files:
        check(os.path.join(root, filename))
f=open("out.txt","w",encoding="utf8")
for i in tagSet:
    print(i,file=f)
