#!/usr/bin/env python
import cookielib, urllib2
import re
import os
import random
import time
import ssl

username = '13912345678'
passwd = '123456'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

test = opener.open('http://bbs.sjtu.edu.cn')
data = test.read()
userip = re.search(r'name="wlanuserip" value="(.+)">', data).group(1)
acname = re.search(r'name="wlanacname" value="(.+)">', data).group(1)
acip = re.search(r'wlanacip=(.+)&wlanacname=', data).group(1)

ref='https://221.181.103.51/cmcc_edu_input.php?wlanacip=%s&wlanacname=%s&wlanuserip=%s&wlanacssid=CMCC-EDU&fromlocation=cmcc_edu_index' % (acip,acname,userip)
opener.addheader=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.52 Safari/537.17')]

temp=opener.open(ref).read()
vad=re.search(r'&code=(.*)\' alt=',temp).group(1)
hidvad=re.search(r'id=\'autohiddenvalidateid\'  value=\'(.*)\'>',temp).group(1)

print vad
print hidvad

data = 'wlanuserip=%s&wlanacname=%s&wlanacip=%s&wlanacssid=CMCC-EDU&username=%s&password=%s&loginmode=static&synccitycheck=&issaveinfo=&loginvalidate=%s&autohiddenvalidateid=%s' % (userip, acname, acip,username,passwd,vad,hidvad)

url = 'https://221.181.103.51/cmcc_edu_do_login.php'
#opener.addheaders=[('Referer',ref),('Host','221.181.103.51'),('User-Agent','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)')]
print 'opening', url, data
data = opener.open(url, data).read()
print 'result', data
