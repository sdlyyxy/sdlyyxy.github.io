#-*_coding:utf8-*-

import yaml
import os
import sys


tagSet = set()


def check(filename):
    # print(filename)
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

def create(tagName):
    if not os.path.exists('./tag/'+tagName):
        os.makedirs('./tag/'+tagName)
    f=open('./tag/'+tagName+'/index.html','w',encoding='utf8')
    print(
        '''
--- 
layout: default 
title: 标签分类 
header: Posts By Tag 
---
        <div class="container docs-container" id="js-to-remove">
	<div class="panel docs-content">
		<div class="wrapper">
			<div class="home">

				{% for tag in site.tags %}
                {% if tag==\''''+tagName+
    '''\'%}
				<h2 id="{{ tag[0] }}-ref">{{ tag[0] }}</h2>
				<ul>
					{% assign pages_list = tag[1] %} {% include LessOrMore/pages_list %}
				</ul>
				{% endfor %}

			</div>
		</div>
	</div>
    </div>
    '''
    ,file=f)


for root, dirs, files in os.walk('./_posts'):
    for filename in files:
        check(os.path.join(root, filename))
for i in tagSet:
    # if not os.path.isfile('./tag/'+i+'/index.html'):
    create(i)
