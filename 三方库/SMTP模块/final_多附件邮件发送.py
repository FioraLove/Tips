import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

"""
简单说下他们的关系，如果构造一个MIMEText对象，就表示一个文本邮件对象，
如果构造一个MIMEImage对象，就表示一个作为附件的图片对象，
要把多个对象组合起来，就用MIMEMultipart对象，他代表的是整个邮件
"""


def send_email_by_qq(to):
    # 发送人的邮件账号以及授权码
    sender_mail = '980710425@qq.com'
    sender_pass = 'uqtjxxxxxquvbbjb'

    # 设置总的邮件体对象，对象类型为mixed
    message = MIMEMultipart('mixed')
    # 邮件添加的头尾信息等
    message['From'] = '980710425@qq.com<980710425@qq.com>'
    message['To'] = 'You'
    # 邮件的主题，显示在接收邮件的预览页面
    subject = '清华大学录取通知书'
    message['subject'] = Header(subject, 'utf-8')

    # 构造文本内容
    text_info = '自强不息，厚德载物'
    """
    MIMEText对象中有三个需要我们设置的参数，一个是正文内容，一个是正文内容的类型，
    例如：”text/plain”和”text/html”，一个是正文内容的编码
    """
    text_sub = MIMEText(text_info, 'plain', 'utf-8')
    message.attach(text_sub)

    # 构造超文本
    url = "https://github.com/FioraLove"
    html_info = """
    <p>点击以下链接，你会去向一个更大的世界</p>
    <p><a href="%s">click me</a></p>
    <p>i am very galsses for you</p>
    """ % url
    html_sub = MIMEText(html_info, 'html', 'utf-8')
    # 如果不加下边这行代码的话，上边的文本是不会正常显示的，会把超文本的内容当做文本显示
    html_sub["Content-Disposition"] = 'attachment; filename="csdn.html"'
    # 把构造的内容写到邮件体中
    message.attach(html_sub)

    # 构造图片
    image_file = open(r'C:\Users\Administrator\Pictures\e7c19e5a380ad45ae1c302b9c1f7fa06.jpg', 'rb').read()
    image = MIMEImage(image_file)
    image.add_header('Content-ID', '<image1>')
    # 如果不加下边这行代码的话，会在收件方方面显示乱码的bin文件，下载之后也不能正常打开
    image["Content-Disposition"] = 'attachment; filename="good_pic.jpg"'
    message.attach(image)

    # 构造附件
    txt_file = open(r'C:\Users\Administrator\Desktop\录取通知书.txt', 'rb').read()
    txt = MIMEText(txt_file, 'base64', 'utf-8')
    txt["Content-Type"] = 'application/octet-stream'
    # 以下代码可以重命名附件为Tinghua.txt
    txt.add_header('Content-Disposition', 'attachment', filename='Tinghua.txt')
    message.attach(txt)

    # 异常机制处理
    try:
        # 发件人邮箱的STMP服务器，端口号
        sftp_obj = smtplib.SMTP('smtp.qq.com', 25)
        # 发件人的邮箱以及授权码
        sftp_obj.login(sender_mail, sender_pass)
        # # message.as_string()中as_string()是将msg(MIMEText或MIMEMultipart对象)变为str
        sftp_obj.sendmail(sender_mail, to, message.as_string())
        sftp_obj.quit()
        print('sendemail successful!')

    except Exception as e:
        print('sendemail failed next is the reason')
        print(e)


def main():
    # 可以是一个列表，支持多个邮件地址同时发送，测试改成自己的邮箱地址
    to = ['942110448@qq.com', '3434279505@qq.com', '2357001705@qq.com', '1775934381@qq.com']
    send_email_by_qq(to)


if __name__ == '__main__':
    main()
