#!usr/bin/env python
#encoding: utf-8

import requests

def fetch(url):
    r = requests.get(url)
    res = r.text
    return r.content
    # return res.encode('utf-8')

def test():
    import os
    f = open('test.txt', 'w')

    #url = raw_input("input the url:")
    url = 'http://cn.python-requests.org/zh_CN/latest/user/quickstart.html#id2'
    f.write(fetch(url))

test()
