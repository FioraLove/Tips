# -*- coding: UTF-8 -*-
import email
import base64  # 解码
import imaplib
import os
import re
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
import json
from email.header import decode_header  # 解码邮件主题


# 将发送封装成一个类，然后把功能分成各个函数，方便以后修改

# 可以用邮箱远程控制后，就剩下cookie 的动态获取了


def get_new_email():  # 用来查看信息
    # 应该返回的也是一个列表，所有的信息在列表里面，方便查看
    # 自动标记为已读，
    all_message = {}
    e_user = "****@qq.com"
    e_password = '****'  # 授权码
    host = "imap.qq.com"
    port = 993  # 995 ?
    try:
        server = imaplib.IMAP4_SSL(host=host, port=port)
        print("已经连接")
        server.login(e_user, e_password)
        print("登录成功")
    except:
        print('连接出现问题！')
        return None

    #  [b'8'] 获得邮箱的数量，老办法，字符串！
    num = str(server.select()[1]).replace('[b\'', '').replace(']', '').replace('\'', '')
    count = int(num) - 1  # 获得最新的一封信的信息
    # print(count)
    # print("邮箱数量:"+num)
    all_message['all_count'] = count

    # 整体信息获取
    typ, data = server.search(None, "Unseen")  # 获取所有未读的信息
    newlist = data[0].split()  # 找最新的一封邮件
    count = len(newlist)
    print("未读邮件数量" + str(count))
    all_message['Unseen_count'] = len(newlist)
    # print(newlist[0])
    # 标记最新的一封邮件为已读
    if count == 0:
        return None
    server.store((newlist[0]), '+FLAGS', '(\\Seen)')
    # print('标记最新邮件为已读')
    typ, data = server.fetch(newlist[count - 1], '(RFC822)')  # 获得最新信封的数据数据  count表示第几封信
    msg = email.message_from_string(data[0][1].decode('utf-8'))  #
    # 对主题进行获取 主题可能为空
    try:
        sub = msg.get('subject')  # 获取主题
        subdecode = email.header.decode_header(sub)[0][0]  # 需要进行转码
        # print("邮箱标题:", end='')
        if subdecode:
            all_message['Subject'] = subdecode.decode('UTF-8')
            # print(subdecode.decode('UTF-8'))
        else:
            all_message['Subject'] = ''
            # print('空')
    except Exception as e:
        all_message['Subject'] = str(e)
        # print(e)
    # 获取发件人的信息
    name = msg.get('from')
    name = str(email.header.decode_header(name))
    name = str(re.findall(r'\D?\d*@qq\.com', name)).replace('[', '').replace(']', '').replace('\'', '').replace('<', '')
    name = name.replace('\"', '')
    all_message["name"] = str(name)
    print("发件人：" + name)
    message = ''
    who = {}
    # 获取邮件所有内容
    try:
        for part in msg.walk():
            # 如果ture的话内容是没用的
            if not part.is_multipart():
                message = message + str(part.get_payload(decode=True).decode('utf-8'))
                # 解码出文本内容，直接输出来就可以了
        print(message)  # 查看内容
        server.close()
        who[name] = message
        all_message['message'] = message
        return all_message
    except Exception as e:
        # # 无伤大雅，，，
        # print("错误："+e)
        # print("HTML格式测试：")
        try:
            content = msg.get_payload()
            content_charset = 'UTF-8'
            content_charset = content[1].get_content_charset()
            text = content[1].as_string().split('base64')[-1]
            html_content = base64.b64decode(text).decode(content_charset)
            message = str(html_content)
            all_message['message'] = message
            return all_message
        except Exception as e:
            print('错误' + e)
            server.close()
            all_message['message'] = ''
            return None


def send_email(s_mes):
    my_sender = s_mes["From"]  # 发送人的账号
    my_pass = s_mes["password"]  # 授权码
    my_user = s_mes["To"]  # 接收人的邮箱
    s_message = s_mes['message']
    try:
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        msg = MIMEText(str(s_message), 'plain', 'utf-8')  # 发送的内容
        msg['From'] = formataddr(['', my_sender])  # 好像没什么同
        msg['To'] = formataddr(['', my_user])  #
        msg['Subject'] = s_mes['Subject']  # 发送的主题
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 服务器的地址和端口
        server.login(my_sender, my_pass)  # 登录的账号密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  #
        server.quit()  # 关闭连接
        return True
    except Exception as e:
        print(e)
        return False


def is_admin(qq):
    try:
        with open("admin.txt", "r") as f:
            admin = f.readlines()
            for i in admin:
                i = str(i).replace("\n", '')
                if str(qq) == str(i):
                    # print("true")
                    return True
            return False
    except:
        with open("admin.txt", "w+") as f:
            f.write("***@qq.com\n")
            f.write("***@qq.com")
            f.close()
    return is_admin(qq)


def send_admin():
    name = {}
    try:
        with open("qq.txt", "r+") as f:
            a = f.readline()
            a = str(a).replace("\n", "")
            b = a.split("#")
            name["From"] = b
            a = f.readline()
            a = str(a).replace("\n", "")
            b = a.split("#")
            name["password"] = b
            return name
    except:
        with open("qq.txt", "w+") as f:
            f.write("From #****@qq.com\n")
            f.write("password  #**\n")
            f.close()
    return send_admin()


if __name__ == '__main__':
    s_mes = {
        'From': '****@qq.com',
        'password': '***',
        'To': '***@qq.com',
        'Subject': '这是主题',
        'message': "关机 3600",
    }

    test = send_admin()
    s_mes["From"] = str(test["From"]).replace("['From ', '", '').replace("']", '')
    s_mes["password"] = str(test["password"]).replace("['password  ', '", '').replace("']", '')
    # print(s_mes)
    # print(test)
    # time.sleep(1.5)  # 设置延时，不然可能不会标记为已读
    while True:
        message = get_new_email()
        if message == None:  # None
            print("没有人，休息30s")
            time.sleep(30)
            continue
        if is_admin(message['name']):
            content = message['message'].replace("\n", '').split(" ")
            minling1 = str(content[0]).replace("<div>", '').replace("</div>", '')
            minling2 = str(content[1]).replace("</div>", '').replace("<div>", '')
            if str(minling1) == "关机" or str(minling1) == "shutdown":
                num = minling2
                try:
                    send_email(s_mes)
                    cmd = "shutdown -s -t " + str(num)
                    os.system("shutdown -s -t " + str(num))
                    s_mes["message"] = "发送关机指令成功:" + cmd
                    s_mes["To"] = message['name']
                    print("关机成功！")
                except:
                    s_mes["message"] = "出现错误！"
                    s_mes["To"] = message['name']
                    send_email(s_mes)
                    print('出现错误！')
            else:
                print(content)
        else:
            print("不是管理员")
        print("休息30s1")
        time.sleep(30)
    # print('结束')
