#!/usr/bin/python
import sys,os,time
fileName=''
if len(sys.argv)>1:
    fileName=sys.argv[1]
if fileName=='':
    print('Usage: ./makepost.py <filename>')
    exit()
output=''
output+='---\n'
output+='layout: post\n'
output+='title: %s\n'%(os.path.basename(fileName)[:-3])
formatTime=time.strftime("%Y-%m-%d %H:%M:%S +0800",time.localtime())
output+='date: '+formatTime+'\n'
postTags=raw_input("Please input the tags of this article:")
output+='tag: ['+postTags+']\n'
output+='---\n\n'
f=open(fileName)
output+=f.read()
f.close()
outFileName='_posts/'+time.strftime("%Y-%m-%d-",time.localtime())+os.path.basename(fileName)
f=open(outFileName,'w')
f.write(output)