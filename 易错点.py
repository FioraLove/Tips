import requests
from lxml import etree


# 1.下载图片（二进制写入）
def download_image():
    url = 'https://img4.duitang.com/uploads/item/201403/23/20140323210720_TwfLF.thumb.700_0.jpeg'

    response = requests.get(url, timeout=4.2)
    data = response.content
    with open('image.png', 'wb') as f:
        f.write(data)


# 2.下载视频（二进制写入）
def download_video():
    response = requests.get(
        'https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo-transcode/1767502_56ec685f9c7ec542eeaf6eac93a65dc7_6fe25cd1347c_3.mp4',
        stream=True)
    # stream参数:一点一点的取,比如下载视频时,如果视频100G,用response.content然后一下子写到文件中是不合理的
    with open('b.mp4', 'wb') as f:
        for line in response.iter_content():
            f.write(line)


def selenium_learning():
    from selenium import webdriver
    import time
    # 创建一个浏览器对象
    browser = webdriver.Chrome()
    # .get函数：打开URL网址
    browser.get('https://www.baidu.com')
    # .execute_script为js脚本，window.open()表示再打开一个新窗口
    browser.execute_script('window.open()')
    # switch_to_window表示切换浏览器窗口
    # browser.window_handles[1]表示切换到窗口2
    browser.switch_to_window(browser.window_handles[1])
    browser.get('https://www.taobao.com')
    time.sleep(1)
    # browser.window_handles[0]表示切换到窗口1
    browser.switch_to_window((browser.window_handles[0]))
    browser.get('https://python.org')


def xapth_lxml():
    etree1 = etree.HTML(html)
    parse = etree1.xpath('.//div[@class="tang"]/ul/li/text()')
    print(parse)


def hanoi(n, a, b, c):
    # 算法的时间复杂度：Ο(1)＜Ο(log2n)＜Ο(n)＜Ο(nlog2n)＜Ο(n2)＜O((n^2)logn)< Ο(n^3）＜…＜Ο(2^n)＜Ο(n!)
    """
    汉诺塔问题
    将n-1个盘子看做一个整体，把最后一个盘子看做一个整体。
　　 将n-1个盘子从A经C移动到B：
　　 把第n个盘子从A移动到C：
　　 把n-1个小圆盘从B经过A移动到C：
    :param n: 问题规模
    :param a: 从哪个柱子
    :param b: 经哪个柱子
    :param c: 到哪个柱子
    :return:
    """
    if n > 0:
        hanoi(n - 1, a, c, b)  # 将n-1个盘子从a经过c移动到b
        print("moving from %s to %s" % (a, c))  # 将剩余的最后一个盘子从a移动到c
        hanoi(n - 1, b, a, c)  # 将n-1个盘子从b经过a移动到c


# 冒泡排序
def bubble_sort():
    li = [1806, 212, 4314, 1611, 8355]
    for i in range(len(li) - 1):  # 总共是n-1趟
        exchange = False
        for j in range(len(li) - i - 1):  # 每一趟都有箭头，从0开始到n-i-1
            if li[j] > li[j + 1]:  # 比对箭头指向和箭头后面的那个数的值
                # 当箭头所指数大于后面的数时交换位置, 升序排列；条件相反则为降序排列
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True  # 如果发生了交换就置为true
        print(li)
        if not exchange:
            # 如果exchange还是False，说明没有发生交换，结束代码
            return


# 选择排序
def select_sort_simple():
    li = [3, 2, 4, 1, 5, 6, 8, 7, 9]
    # 和冒泡排序类似，在n-1趟完成后，无序区只剩一个数，这个数一定是最大的
    for i in range(len(li) - 1):  # i是第几趟
        min_loc = i  # 最小值的位置
        for j in range(i + 1, len(li)):  # 遍历无序区，从i开始是自己跟自己比，因此从i+1开始
            if li[j] < li[min_loc]:  # 如果遍历的这个数小于现在min_loc位置上的数
                min_loc = j  # 修改min_loc的index，循环完后，min_loc一定是无序区最小数的下标
        li[i], li[min_loc] = li[min_loc], li[i]  # 将i和min_loc对应的值进行位置交换
        print(li)  # 打印每趟执行完的排序，分析过程


# 插入排序
def insert_sort():
    li = [3, 2, 4, 1, 5, 6, 9, 6, 8]
    for i in range(1, len(li)):  # i表示摸到牌的下标
        tmp = li[i]  # 摸到的牌
        j = i - 1  # j指得是手里牌的下标
        while li[j] > tmp and j >= 0:  # 循环条件
            """
            循环终止条件：如果手里最后一张牌 <= 摸到的牌  or j == -1
                比如手里有牌457，新摸到一张6(index=3)，当比对5与6时，5<6,满足了循环终止条件，插到列表j+1处，即index=2处.
                比如手里的牌是4567,新摸到一张3(index=4)，一个个比对均比3大，到4与3比较时，由于比4小，再次循环j=-1，满足终止条件插到列表j+1处，即最前面
            """
            li[j + 1] = li[j]  # 通过循环条件，将手里的牌左移
            j -= 1  # 手里的牌对比箭头左移
        li[j + 1] = tmp  # 将摸到的牌插入有序区
        print(li)  # 打印每一趟排序过程


class Node(object):

    def __init__(self, data=None, left=None, right=None):  # data代表根节点，left代表左节点，right代表右节点
        self._data = data
        self._left = left
        self._right = right


# 先序遍历  遍历过程 根左右
def pro_order(tree):
    if tree == None:
        return False
    print(tree._data, end=' ')
    pro_order(tree._left)
    pro_order(tree._right)


# 后序遍历 遍历过程：左 右 根
def pos_order(tree):
    if tree == None:
        return False
    # print(tree.get_data())
    pos_order(tree._left)
    pos_order(tree._right)
    print(tree._data, end=' ')


# 中序遍历 遍历过程： 左 根 右
def mid_order(tree):
    if tree == None:
        return False
    # print(tree.get_data())
    mid_order(tree._left)
    print(tree._data, end=' ')
    mid_order(tree._right)


# 层次遍历 遍历过程：从上至下，从左至右(用一个队列保存被访问的当前节点的左右孩子以实现层序遍历。)
def row_order(tree):
    # print(tree._data)
    queue = []
    queue.append(tree)
    while True:
        if queue == []:
            break
        print(queue[0]._data, end=' ')
        first_tree = queue[0]
        if first_tree._left != None:
            queue.append(first_tree._left)
        if first_tree._right != None:
            queue.append(first_tree._right)
        queue.remove(first_tree)

# import pywifi
# from pywifi import const
# import time
# def wifi1():
#     wifi=pywifi.PyWiFi()#获取网卡
#     ifaces=wifi.interfaces()[0]
#     print(ifaces.name())#获取网卡名字
#     print(ifaces.status())#获取网卡状态（0是未连接，1是已连接）
#     if ifaces.status()==const.IFACE_DISCONNECTED:
#         print("未连接！！")
#     else:
#         print("已连接！")
#     ifaces.scan()#扫面附近的网络
#     time.sleep(2)
#     res=ifaces.scan_results()
#     for date in res:
#         a=date.ssid#读取网络的名称，如果是中文的话，会乱码，待解决中
#         print(str(a),type(a))



# 栈的使用
class Stack(object):
    def __init__(self):
        # 列表和字典都可以视为栈，以列表为作为开栈口
        # 因为在表尾添加或删除元素的时间复杂度为O(1)
        self._list =[]

    def push(self,item):
        # 添加一个元素item到栈顶
        self._list.append(item)

    def pop(self):
        # 弹出栈顶元素
        return self._list.pop()  # pop()函数用于移除列表中的一个元素(默认最后一个元素)

    def get_top(self):
        # 返回一个栈顶元素
        if self._list:
            return self._list[-1]
        else:
            return None

    def is_empty(self):
        # 判断栈是否为空
        return self._list == []

    def size(self):
        # 返回栈的元素个数
        return len(self._list)

# 括号匹配问题
def kuohao_match(exp):
    # 以列表为栈
    stack = []
    # 目标条件匹配
    items = {'(': ')', '{': '}', '[': ']'}
    # 遍历目标字符串
    for item in exp:
        # 遍历item是否含有这三种字符
        if item in {'(', '{', '['}:
            stack.append(item)
        else:
            if len(stack) == 0:
                return False
            # 返回栈顶元素,pop() 函数用于移除列表中的一个元素(默认最后一个元素)
            top = stack.pop()
            if items[top] != item:
                return False
    if len(stack) > 0:
        return False
    else:
        return True

class Queue(object):
    # 队列（先进先出）
    def __init__(self):
        self._list = []  # 初始化构造函数，空的列表私有化保存元素

    def enqueue(self, item):
        # 往队列中增加一个item元素
        self._list.append(item)

    def dequeue(self):
        # 列表头部删除一个元素
        return self._list.pop(0)

    def is_empty(self):
        # 判断一个队列是否为空
        return self._list == []

    def size(self):
        # 返回队列的大小
        return len(self._list)

# 双端队列
def deque():
    from collections import deque

    """
    deque([iterable[, maxlen]])  
        参数：列表、最大队列
        
    创建队列：queue = deque(li)
    进队：append
    出队：popleft
    双向队列队首进队：appendleft
    双向队列队尾进队：pop
    """
    # q = deque()  # 创建队列
    q = deque([1, 2, 3], 5)
    q.append(1)  # 队尾进队
    print(q.popleft())  # 1    队首出队

    # 用于双向队列
    q.appendleft(1)  # 队首进队
    q.pop()  # 队尾出队



if __name__ == '__main__':

    # download_image()
    # download_video()
    # selenium_learning()
    # xapth_lxml()
    # 汉诺塔模型
    # n = int(input('汉诺塔层数:'))
    # hanoi(n, 'A', 'B', 'C')
    # bubble_sort()
    # select_sort_simple()
    # insert_sort()
    # tree = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G')))  # 注意描述一棵树的节点的规范
    # print('-------先序遍历---------')
    # pro_order(tree)
    #
    # print('\n\n-------中序遍历---------')
    # mid_order(tree)
    # print('\n\n-------后序遍历---------')
    # pos_order(tree)
    # print('\n\n--------层次遍历--------')
    # row_order(tree)
    # s = Stack()
    # s.push(1)
    # s.push(2)
    # s.push(3)
    # print('<------------>')
    # print(s.size())
    # print('<------------>')
    # print(s.pop())
    # print('<------------>')
    # print(s.pop())
    # print('<------------>')
    # print(s.size())
    # print('<------------>')
    # print(s.is_empty())
    # print('<------------>')
    # print(kuohao_match('(){}[{[[](])}]'))
    #
    # print('----^^^^^-----')
    # ws = Queue()
    # ws.enqueue(1)
    # ws.enqueue(2)
    # print(ws.size())
    # print(ws.dequeue())
    # print(ws.dequeue())
    # print(ws.size())
    # print(ws.is_empty())
    # deque()
    pass
