# -*- coding:utf-8 -*-

"""
我们可以用HTTP（超文本传输协议）来访问一个网站一样，发送邮件要使用SMTP（简单邮件传输协议），
SMTP也是一个建立在TCP（传输控制协议）提供的可靠数据传输服务的基础上的应用级协议，
它规定了邮件的发送者如何跟发送邮件的服务器进行通信的细节
用法：
1.创建SMTP的操作对象并连接smtp目标服务器，可以是163、QQ等
2.根据自己的账号登录目标服务器（自己的邮箱地址和邮箱授权码）
3.调用对象中的方法，发送邮件到目标地址
"""
# Python与SMTP服务器之间的具体交互
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

# smtp简单文本邮件发送
def email_post():
    # 发送人
    sender = '9807xxxxx25@qq.com'
    # 接受人
    receivers = '942xxxxx8@qq.com'
    # 定义文件内容
    message = MIMEText('恭喜你已成为清华大学研究生')
    # 邮件添加首尾信息
    message['From'] = Header('我是陈浩东', 'utf-8')
    message['To'] = Header('多攀', 'utf-8')
    # 邮件主题：显示在邮件接受时预览界面
    message['Subject'] = Header('SMTP示例代码实验邮件', 'utf-8')
    # 发件人邮箱的STMP服务器，端口号
    smtper = SMTP('smtp.qq.com')
    # 发件人的邮箱账号，邮箱授权码
    smtper.login(sender, 'xxxxxxxxxxbjb')
    # msg.as_string()中as_string()是将msg(MIMEText或MIMEMultipart对象)变为str。
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    email_post()
