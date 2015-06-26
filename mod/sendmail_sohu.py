__author__ = 'Administrator'
import requests
import time
def mail(email_list, subject, html):
    url="http://sendcloud.sohu.com/webapi/mail.send.json"
    #files={ "file1": (u"1.pdf", open(u"1.pdf", "rb")),
    #        "file2": (u"2.pdf", open(u"2.pdf", "rb"))}
    # 不同于登录SendCloud站点的帐号，您需要登录后台创建发信子帐号，使用子帐号和密码才可以进行邮件的发送。
    params = {"api_user": "flyhu2009_test_mlNXvt",
        "api_key" : "z7ulleXa5f4pugu6",
        "to" : email_list,
        "from" : "service@sendcloud.im",
        "fromname" : "告警",
        "subject" : subject,
        "html": html
        }
    r = requests.post(url, files={}, data=params)
    return eval(r.text)
if __name__ == "__main__":
    subject = "%s 电脑开机  告警"%time.strftime("%Y-%m-%d_%H:%M")
    html = "mysql 服务已离线，请检查！"
    email_list = ["flyhu2009@126.com;jk409@189.cn"]
    result = mail(email_list, subject, html)
    print(subject, result['message'])
