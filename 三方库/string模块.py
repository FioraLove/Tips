import string
import random


def demo():
    a = string.ascii_letters  # 表示获取包含大小写的所有英文字母
    b = string.ascii_lowercase  # 获取所有的小写字母
    c = string.ascii_uppercase  # 获取所有的大写英文字母
    d = string.digits
    print('获取包含大小写的所有英文字母' + a + '\n' + '获取小写的所有英文字母' + b + '\n' + '获取大写的所有英文字母' + c + '\n' + '获取所有数字' + d)
    # sample（seq,n）随机获取序列seq的n个元素
    return random.sample((a + d), 4), a + d


if __name__ == '__main__':
    a, b = demo()
    # 将列表拼接为字符串
    c = ''.join(a)
    print(c, a, b)
    print(type(a))
