
### ```软硬件的Bug报错```
<img src="http://pic1.win4000.com/wallpaper/2019-09-29/5d9049c9b3c1d.jpg" width=70%/><br>
#### 1.[安装Docker后VMware和VirtualBox无法启动 VT-x is not available??](https://blog.csdn.net/huryer/article/details/91126391)<br>
><span style="color: green"> 要在windows上使用docker-desktop，需要打开Hyper-V；如果要运行VMware 或Oracle VM VirtualBox，需要禁用Hyper-V;鱼和熊掌不可兼得 </span>

#### 2.[解决Windows10中Virtualbox安装虚拟机没有64位选项(N种情形盘点)](https://www.4spaces.org/windows-10-virtualbox-no-64bit/)

#### 3.[]()



    


# Tips
详细记录一些常见易混知识点，涵盖python，Django，js，SQL，web，spider....

### 1.TCP与UDP

  TCP的三次握手，四次挥手：
      所谓三次握手(Three-way Handshake)，是指建立一个TCP连接时，需要客户端和服务器总共发送3个包。

    首先Client端发送连接请求报文，Server段接受连接后回复ACK报文，并为这次连接分配资源。Client端接收到ACK报文后也向Server段发生ACK报文，并分配资源，这样TCP连接就建立了。

    TCP的连接的拆除需要发送四个包，因此称为四次挥手(four-way handshake)。客户端或服务器均可主动发起挥手动作（中断连接），在socket编程中，任何一方执行close()操作即可产生挥手操作。

     挥手过程：假设Client端发起中断连接请求，也就是发送FIN报文。Server端接到FIN报文后，意思是说"我Client端没有数据要发给你了"，但是如果你还有数据没有发送完成，
    则不必急着关闭Socket，可以继续发送数据。所以你先发送ACK，"告诉Client端，你的请求我收到了，但是我还没准备好，请继续你等我的消息"。
    这个时候Client端就进入FIN_WAIT状态，继续等待Server端的FIN报文。当Server端确定数据已发送完成，则向Client端发送FIN报文，"告诉Client端，好了，我这边数据发完了，准备好关闭连接了"。
    Client端收到FIN报文后，"就知道可以关闭连接了，但是他还是不相信网络，怕Server端不知道要关闭，所以发送ACK后进入TIME_WAIT状态，如果Server端没有收到ACK则可以重传。
    “Server端收到ACK后，"就知道可以断开连接了"。
    Client端等待了2MSL后依然没有收到回复，则证明Server端已正常关闭，那好，我Client端也可以关闭连接了。

### 2.python占位符%s,%d,%r,%f
    -%s 代表字符串占位符
    -%d 代表数字占位符
    -%f 默认保留6为小数位
    
# Python3 cookbook 

    # -*- coding:utf-8 -*-
## 1.将序列或元组分解为单独变量
    a = (4, 5)
    x, y = a
    print(x, y)
    b = 3
    c = 4
    # 拓：仅元组支持这样的的交换操作，直接传统上忽略第三方变量
    b, c = c, b
    print(b, c)

## 2.从任意长度的可迭代对象中分解元素(*表达式分解未知或任意长度的可迭代对象)
    record = ('Dove', 'dave@qq.com', '187-1369', '158-6711')
    name, email, *tel = record
    print(tel)
    print(email)
    print(name)

    # 拓：元组的遍历
    for i in record:
        print(i)

## 3.collects库使用
    from collections import Counter

    s = 'abcbcaccbbad'

    l = ['a', 'b', 'c', 'c', 'a', 'b', 'b']

    d = {'2': 3, '3': 2, '17': 2}
### 3.1 Counter使用：将元素进行数量统计、计数后返回一个字典,键值为元素：值为元素个数
    print(Counter(s))
    print(Counter(l))
    print(Counter(d))

### 3.2 most_common(int)方法 按照元素出现的次数进行从高到低的排序,返回前int个元素的字典
    m = Counter(s)
    print(m.most_common())
    print(m.most_common(3))

### 3.3 elements方法 返回经过计数器Counter后的元素,返回的是一个迭代器
    print('---------')
    print('-'.join(sorted(m.elements())))

### 4.deque双端队列
    from collections import deque

    """
    双端队列，它最大的好处就是实现了从队列头部快速增加和取出对象: .popleft(), .appendleft() 。
    作为一个双端队列，deque还提供了一些其他的好用方法，比如 rotate
    """
    str = 'abc123cd'
    dq = deque(str)
    print(dq)

### 4.1 向双端队列deque的队列左边添加元素
    dq.appendleft('left')
    dq.appendleft('ojbk')
### 4.2 向双端队列右边添加元素
    dq.append('hello')
    dq.append('python')
    dq.append(0)
    print(dq)
    print(type(dq))

    raw = [1, 2, 3]
    d = deque(raw)
### 4.3 左扩展
    d.extendleft([4, 5, 6])
    print(d)
### 4.4 右扩展
    d.extend([7, 8, 9])
    print(d)  # deque([6, 5, 4, 1, 2, 3, 7, 8, 9])

### 4.5 右弹出
    r_pop = d.pop()
    print(r_pop)  # 9
    print(d)  # deque([6, 5, 4, 1, 2, 3, 7, 8])

### 4.6 左弹出
    l_pop = d.popleft()
    print(l_pop)  # 6
    print(d)  # deque([5, 4, 1, 2, 3, 7, 8])

### 4.7 将右边n个元素值取出加入到左边
    d.rotate(3)
    print(d)  # deque([3, 7, 8, 5, 4, 1, 2])

# 5.字符串的切片操作
    str = 'i love , you ? for ever,foo,info'
    str1 = str.split(' ')
    print(str1)

### 5.1.字符串的开头或结尾做文本匹配:同时针对多个选项做判断时，利用startswith，endswith提供可能选项的元组即可（ps：元组）
    # endwith判断以某字符结尾
    filenames = ['makefile.txt', 'hello.py', 'span.c', 'kill.c++']
    li = []
    for name in filenames:
        if name.endswith(('.py', '.c')):
            li.append(name)
            print(name)

    print(li)
### 5.2 字符串判断以某字符开头的startwith
    li1 = []
    for name in filenames:
        if name.startswith(('h', 's', 'k')):
            li.append(name)
            print(name)

    print(li)

### 5.3.利用字符串的切片操作来实现开头或结尾做文本匹配
    file = 'span.txt'
    print(file[-4:])
    print(file[:4:2])
    url = 'https://www.taobao.com'
    if url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp':
        print(url)

### 5.4.文本模式的匹配与查找:常用的基本方法str.find(str,开始索引，结束索引) , str.startwith() , str.endswith() , 更或者是正则表达式
    import re

    text = '11/27/2019'
    if re.match('\d+/\d+/\d+', text):
        print(re.findall('(\d+).*?(\d+).*?(\d+)', text))
        print('yes')

    else:
        print('badwoman')
        
# 章节二：字符串与文本

    # -*- coding:utf-8 -*-
    import time,textwrap

# 1.字符串忽略大小写的搜索替换

### 1.1 re模块下的re.INGORECASE(即：flags = re.INGORCASE)
    import re

    text = 'python HELLO　，lower python,Mixed Python '
    dev = re.findall('python', text, flags=re.IGNORECASE)
    print(dev)
    dev_1 = re.sub('python', 'dragon', text, flags=re.IGNORECASE)
    print(dev_1)
    """
    >>>['python', 'python', 'Python']
    >>>dragon HELLO　，lower dragon,Mixed dragon
    """

# 2.删除字符串中不需要的字符
### 2.1strip()用于删除开始或结尾的指定字符，lstrip()与rstrip()分别从左或右删除指定字符操作
    s = ' hello world \n '
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())
    print(s.strip(' hello'))

### 2.2 利用replace()方法或正则表达式替换字符串中间内容
    str = 'hello   world \n bey jiu bey'
    print((str.replace(' ', '-')).replace('\n', '-'))
    print(re.sub('\s+', ' ', str))

    # 拓：文件读取多行数据
    with open('aa.txt', 'r', encoding='utf-8') as f:
       # 生成列表表达式，这种方法非常高效，不需要预先读取所有数据到一个临时列表中
         lines = (line.strip() for line in f)
         for line in lines:
             print(line)


# 3.字符串的对齐操作：可以使用字符串的ljust(字符总长度，填充字符),rjust(字符总长度，填充字符) 和 center(字符总长度，填充字符)方法
    txt = 'hello python'
    print(txt)
    print(txt.ljust(20, '^'))
    print(txt.rjust(20, '-'))
    print(txt.center(19, '-'))

# 4.合并拼接字符串

### 4.1 若合并的字符串是一个序列(列表，元组，字典，文件，集合和生成器等)或可迭代对象，最快的方法就是join()方法
    parts = ['IS', 'moby', 'c++', 'python']
    print(','.join(parts))
    print('--'.join(parts))

### 4.2 加号(+)拼接字符串
    start = time.time()
    a = 'china no.1'
    b = 'for better'
    print(a + ' ' + b)
    print('a:{}--b:{}'.format(a, b))
    time.sleep(1.2)
    end = time.time()
    print(end-start)
    print(time.ctime())

# 5.以指定列宽格式化字符串
### 5.1使用textwrap(文本换行)格式化字符串的输出
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under."

    """
    textwrap.fill(s,num,initial_indent = ' ',subsequent_indent = ' ')
    s:目标字符串
    num:一行显示的字符数
    initial_indent = ' ':表示首行缩进多少个字符
    subsequent_indent = ' ':表示除首行外的所有行数缩进多少个字符
    """
    print(textwrap.fill(s, 40))
    print(textwrap.fill(s, 41, initial_indent='    ', subsequent_indent='     '))
