#-*_coding:utf8-*-
#!/usr/bin/python
import sys
import os
import time
import platform
import glob

fileName = ''
if len(sys.argv) > 1:
    fileName = sys.argv[1]
if fileName == '':
    file_list = glob.glob('*.md')
    if len(file_list)!=2:
        print('Usage: ./makepost.py <filename>')
        exit()
    if file_list[0]=="README.md":
        fileName=file_list[1]
    else:
        fileName=file_list[0]
output = ''
output += '---\n'
output += 'layout: post\n'
output += 'title: %s\n' % (os.path.basename(fileName)[:-3])
formatTime = time.strftime("%Y-%m-%d %H:%M:%S +0800", time.localtime())
output += 'date: ' + formatTime + '\n'
ver = platform.python_version()
print(fileName)
if ver[0] == '2':
    postTags = raw_input("Please input the tags of this article:")
else:
    postTags = input("Please input the tags of this article:")
if postTags=="":
    postTags="杂"
output += 'tag: [' + postTags + ']\n'
output += '---\n\n'
f = open(fileName, encoding="utf8")
output += f.read()
f.close()
outFileName = '_posts/' + \
    time.strftime("%Y-%m-%d-", time.localtime()) + os.path.basename(fileName)
f = open(outFileName, 'w', encoding='utf8')
f.write(output)
os.remove(fileName)
