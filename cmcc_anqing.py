#!/usr/bin/env python
import cookielib, urllib2
import re
import os
import random
import time

username = '15211436758'
passwd = 'r7xfep'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

test = opener.open('http://baidu.com')
data = test.read()
userip = re.search(r'name="wlanuserip" value="(.+)">', data).group(1)
acname = re.search(r'name="wlanacname" value="(.+)">', data).group(1)
acip = re.search(r'wlanacip.*value=\"(.+)\" type', data).group(1)


data = 'wlanuserip=%s&wlanacname=%s&wlanacip=%s&wlanacssid=CMCC&staticusername=%s&staticpassword=%s&loginmode=static&staticsaveuserinfo=yes' % (userip, acname, acip,username,passwd)
#url = os.path.join(os.path.dirname(test.url), data)
url = 'https://221.176.1.140/wlan/login.do'
print 'opening', url, data
data = opener.open(url, data).read()
print 'result', data
