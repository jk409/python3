#coding=utf-8
__author__ = 'Administrator'
import requests
import time
url="http://sendcloud.sohu.com/webapi/mail.send.json"
params = {"api_user": "flyhu2009_test_mlNXvt",
    "api_key" : "z7ulleXa5f4pugu6",
    "to" : "jk409@qq.cn",
    "from" : "service@sendcloud.im",
    "fromname" : "告警",
    "subject" :'%s 电脑开机'%time.strftime("%Y-%m-%d_%H:%M"),
    "html": '时间：%s,<br>服务：%s,<br>状态：%s'
             '<br>=========================================='%(time.strftime("%H:%M"),'电脑','开启')
  }
r = requests.post(url, files={}, data=params)
print(r.text)
