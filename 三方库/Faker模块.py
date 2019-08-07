# -*- coding:utf-8 -*-
"""
在做程序开发的时候，我们经常会用到一些测试数据，相信大多数同学是这么来造测试数据的：
test1
test01
test02
测试1
测试2
测试数据1
这是一段测试文本
这是一段很长很长很长的测试文本...
中枪的请举手。不仅要自己手动敲这些测试数据，还敲的这么假。那有啥办法呢？难不成有什么东西能自动给我造点以假乱真的数据啊？你别说，还真有！
在 Python 中有个神库，叫做 Faker，它可以自动帮我们来生成各种各样的看起来很真的”假“数据，让我们来看看吧！
"""
from time import time, sleep

# 生成几个假数据：
from faker import Faker

# 创建一个Faker()对象,支持多种语言
faker = Faker('zh_CN')

# 生成姓名
print('name:', faker.name())

# 生成虚假地址
print('address:', faker.address())

# 生成虚假文本
print('text:', faker.text())
# print(faker.providers)

# 用于生成公司相关数据，如公司名、公司前缀、公司后缀等内容
print('company:',faker.company())

# 用于生成信用卡相关数据，如过期时间、银行卡号、安全码等内容
print('Credit Card:',faker.credit_card_full(card_type='visa'))

# 用于生成时间相关数据，如年份、月份、星期、出生日期等内容
print('data-time:',faker.year())

# File，用于生成文件和文件路径相关的数据，包括文件扩展名、文件路径、MIME_TYPE、磁盘分区等内容
print('file_name:',faker.file_name())
print('file_path:',faker.file_path(depth = 1,category = None,extension =None))

# Geo:用于生成和地理位置相关的数据，包括经纬度，时区等等信息


# Internet，用于生成和互联网相关的数据，包括随机电子邮箱、域名、IP 地址、URL、用户名、后缀名等内容

# Job，用于生成和职业相关的数据
print('job:',faker.job())

# Misc，用于生成生成一些混淆数据，比如密码、sha1、sha256、md5 等加密后的内容
print('md5:',faker.md5())


