# Tips

#### 详细记录一些常见易混知识点，涵盖python，Django，js，SQL，web，spider....<br>
<img src="其它/images/5a2e2395122c7.jpg" width=60% /><br>

### 一、存在一个settings.py文件，里面存在任意的参数，比如

   USER_NAME = 'chd'
   
   PASSWORD = 123456
   
   思考这样一个问题，如何在Python文件中调用settings.py文件中的这两个参数？？
   
   
   -1.涉及到scrapy时，解决方法如示：
   
    通过Settings对象的方法:从scrapy.conf中导入settings.py,并使用其中的参数设置
    from scrapy.conf import settings
    
    username = settings.get('USER_NAME') 有时会这样写self.settings.get('USER_NAME')
    password = settings.get('PASSWORD')
    
   -2.涉及到Django时，解决方法如示：
   
   
    from django.conf import settings
    
    调用方法：settings.configure，configure() 可以设置任何配置项，每个参数对应一个值。参数名称必须大写，而且参数名必须是真实存在
     username = settings.USER_NAME
     password = settings.PASSWORD
     
#### Django模拟登陆时怎么获取cookie以及保存cookie
	
	        # 获取cookie
            cookies_ct = requests.utils.dict_from_cookiejar(session.cookies)
            # 将cookie保存至本地文件
            with open(settings.COOKIE_PATH, "w") as fp:
                json.dump(cookies_ct, fp)

### 二、Redis数据库

    # -*- coding:utf-8 -*-
    # redis数据库连接
    from redis import StrictRedis

  -连接方式一：StrictRedis对象
  
    redis = StrictRedis(host='localhost', port=6379, db=0, password=None)
    redis.set('lover', 'woman')
    print(redis.get('name'))
    print(redis.get('lover'))
    print(redis.get('age'))


   -连接方式二：
   
    from redis import ConnectionPool

    pool = ConnectionPool(host='localhost', port=6379, db=0, password=None)
    redis = StrictRedis(connection_pool=pool)
    redis.set('lover', 'woman')
    print(redis.get('name'))
    print(redis.get('lover'))
    print(redis.get('age'))
    

### 三、Redis数据库功能

#### 1.django项目中使用redis存储session

    说明：
         django默认将session信息存储在数据库中，我们需要通过修改settings.py配置文件，然后将session存储到redis中
         
   -1 安装依赖包：
   
        pip install django-redis-sessions
        
   -2 修改settings.py配置文件
    
    # 设置使用redis存储session信息
    SESSION_ENDINE = 'redis_sessions.session'
    # redis服务的ip地址
    SESSION_REDIS_HOST = 'loaclhost'
    # redis服务的端口
    SESSION_REDIS_PORT = 6379
    # redis使用哪个数据库
    SESSION_REDIS_DB = 2
    # redis密码
    SESSION_REDIS_PASSWORD = ''
    # redis存储信息前缀
    SESSION_REDIS_PREFIX = 'session'
    
   -3 测试，操作session信息   
    --打开APP_name/views.py文件，创建set_session,get_session的视图
   
    from django.http import HttpResponse

    def set_session(request):
        """设置session"""
        request.session['name'] = name

        return HttpResponse('设置session')

    def get_session(request):
        """获取session"""
        uname = request.session['name']

	    return HttpResponse(ame)

#### 2.基本操作（键的操作，字符串，列表，hash，集合，有序集合等）

    # -*- coding:utf-8 -*-
    # 一、redis数据库连接
    from redis import StrictRedis

    # 连接方式一：StrictRedis对象
    redis = StrictRedis(host='localhost', port=6379, db=3, password=None)
    redis.set('lover', 'woman')
    redis.set('beatutiful','pretty')
    print(redis.get('name'))
    print(redis.get('lover'))
    print(redis.get('age'))


    # 二、键的操作
    # 判断键是否存在:
    print(redis.exists('age'))

    # 删除某个键
    print(redis.delete('content'))

    # 判断键的类型
    print(redis.type('beatutiful'))

    # 获取当前数据库的键的数目
    print(redis.dbsize())

    # 设定键的过期时间 ，单位为秒，-1表示永不过期
    print(redis.expire('name',300))

    # 获取键的过期时间，单位为秒
    print(redis.ttl('name'))

    # 将键移动到其它数据库：move(键名，数据库代号)
    redis.move('age',db=1)

    # 三、字符串的操作
    # set(name,value):给数据库中键名为name的string赋予值value
    redis.set('name','bob')
    redis.set('age',20)

    # 返回数据库中键名为name的string的值value
    print(redis.get('name'))

    # 返回多个键对应的value组成的列表
    print(redis.mget(['name','age','lover']))

    # 四、列表操作
    # 在键名为name的列表末尾添加值为value的元素，也可传入多个
    redis.rpush('list', 1, 2, 3, 4)

    # 在键名为name的列表头部添加值为value的元素，也可传入多个
    redis.lpush('list', -1, 0)

    # 返回列表的长度
    print(redis.llen('list'))

    # 返回索引start与end之间的内容(索引从角标1开始)
    print(redis.lrange('list', 1, 3))
    print(redis.lrange('list',1,6))





   ### 特别注意：redis.flushdb()表示删除当前选择的数据库中的所有键
   ### redis.flushall() ：删除所有数据库中的键

    # 连接方式二：
    from redis import ConnectionPool

    pool = ConnectionPool(host='localhost', port=6379, db=0, password=None)
    redis = StrictRedis(connection_pool=pool)
    redis.set('lover', 'woman')
    print(redis.get('name'))
    print(redis.get('lover'))
    print(redis.get('age'))


    # 五、集合操作：元素是不重复的

    # 向键名为name的集合中添加元素
    redis.sadd('tags','book','tea','coffee')
    redis.sadd('tags1','coffee','water')
    redis.expire('tags',7200)

    # 返回键名为name的集合的元素个数
    print(redis.scard('tags'))

    # 判断某个元素是否是键名为name的集合元素
    print(redis.sismember('tags', 'book'))
    print(redis.sismember('tags', 'noob'))

    # 返回所有给定的键的集合的交集
    print(redis.sinter('tags','tags1'))

    # 返回所有给定键的集合的并集
    print(redis.sunion('tags','tags1'))

    # 求并集并将并集保存到新的集合中
    redis.sunionstore('new_tags',['tags','tags1'])

    # 返回所有给定键的集合的差集
    print(redis.sdiff('tags','tags1'))

    # 求差集并将差集保存到新的集合dest中
    redis.sdiffstore('new_diff',['tags','tags1'])
    
#### 3. redis主从配置
	
	资料网站：https://blog.csdn.net/weixin_41846320/article/details/83753667
		 https://www.cnblogs.com/cang12138/p/9132288.html
		 https://www.cnblogs.com/carrychan/p/9396997.html
    redis库下载地址：https://github.com/MicrosoftArchive/redis/releases

   - 3.1安装从库
   
    解压文件后，复制一份Redis文件并重命名，当做从库
	
	  文件目录：
	  |----
	 	---master_6379
		---slave_6380
		---slave_6381
	
   - 3.2修改从库文件中 redis.windows.conf 的端口号
   
   
   		 1. master_6379 不做更改

		 2.slave_6380文件夹中redis.windows.conf文件配置
			 port 6380
			 # 设置该从机的主机为127.0.0.1:6379
			 slaveof 127.0.0.1 6379 #格式为slaveof 主机的host 主机的port 


          	 3. slave_6381文件夹中redis.windows.conf文件配置 
				 # 设置该从机的主机为127.0.0.1:6379
                 			port 6381
				 slaveof 127.0.0.1 6379
				 
		  4. 假设主从机是同一台计算机时，假设Master和Slave在同一台主机（即需调整从机为不同的监听端口），
		  Master的端口为6379，slave1的端口为6380，salve2的端口为6381.....
		  假设Master和Slave不在同一台主机： redis.windows.conf 文件slavesof的设置是一模一样的，各从机的监听端口设置为6379
				 
				 
- 3.3、安装服务，需要重新设置名称。然后去服务中，开启“redis6380”（此时就可以连接6380的库了）

	  redis-server --service-install redis.windows.conf  --service-name Redis6380
	  
- 3.4、知识点：
  		
		1.cmd命令进入各redis库目录下，键入命令：redis-cli -p 端口号 启动redis服务
		2.键入命令 info replication 查看redis数据库相关信息包括：主机，从机属性
		
#### 4.redis哨兵（sentinel）搭建

		什么是哨兵机制
			Redis集群中，如果主服务器宕机（扑街）则需要手动去重启或者切换主服务器。通过哨兵机制能实现自动监听，并在从服务器中投票选举出新的master

			Redis的哨兵机制功能如下：

			监控(Monitoring): 哨兵(sentinel) 会不断地检查你的Master和Slave是否运作正常。

			提醒(Notification):当被监控的某个 Redis出现问题时, 哨兵(sentinel) 可以通过 API 向管理员或者其他应用程序发送通知。

			自动故障迁移(Automatic failover):当一个Master不能正常工作时，哨兵(sentinel) 会开始一次自动故障迁移操作,它会将失效Master的其中一个Slave升级为新的Master, 并让失效Master的其他Slave改为复制新的Master; 当客户端试图连接失效的Master时,集群也会向客户端返回新Master的地址,使得集群可以使用Master代替失效Master


   -4.1 服务器（Master）配置：在redis安装目录下新建sentinel.conf文件，内容如下：
   
	    # 当前Sentinel服务运行的端口
		port 26379
		# 哨兵监听的主服务器
		sentinel monitor mymaster 192.168.1.246 6379 2
		# 3s内mymaster无响应，则认为mymaster宕机了
		sentinel down-after-milliseconds mymaster 3000
		# 如果10秒后,mysater仍没启动过来，则启动failover
		sentinel failover-timeout mymaster 10000
		# 执行故障转移时， 最多有1个从服务器同时对新的主服务器进行同步
		sentinel parallel-syncs mymaster 1
		# 哨兵监听需要密码认证
		sentinel auth-pass mymaster test@2017
		# 线程守护
		daemonize no
		# 日志路径
		logfile "D:/gateway/log/sentinel.log"



   -4.2 开启哨兵机制：
   
   		-遵循先主后备原则：开启主服务，在开启从机服务，最后开启哨兵机制服务
		Redis bin目录启动哨兵机制：cmd命令进入sentinel.conf即可启动
		
   -总结
   
	哨兵机制只是某台服务器上的软件，只占用该台服务器的端口
	一台服务器可以被多个哨兵监听，集群中每个从服务器都可以开启哨兵机制
	哨兵机制至少需要3台服务器。因为master宕机后，至少要有其他服务器投从服务器一票
		
#### 5.Python一般脚本文件编写流程：
	1.文件配置一般在config.json中，比如：用户名，账号，密码，人员信息等等
	2.在settings.py 文件中导入.json文件中的配置
	    # 载入配置文件
	    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # 返回当前path文件的上一级目录
	    with open(os.path.join(BASE_DIR,"settings.json"),"r") as f:
		SETTINGS = json.load(f)

	    #  配置文件的内容获取
	    SERVER = SETTINGS["DB_CONFIG"]["DB_SERVER"]
	    # json格式新的调用方法：json.load(f)的变量名["对象名"]["键名"]

	3.在主文件.py 中导入文件import settings
	    文本格式内容为：settings.SERVER，settings.PASSWORD等等

	脚本目录：
	    |
	    |--core.py
	    |
	    |--settings.py
	    |
	    |--config.json
	    |
	    |--a.py
	    |--b.py
	    |
	    |--.gitignore   
=======
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
    
### ```软硬件的Bug报错```

#### 1.[安装Docker后VMware和VirtualBox无法启动 VT-x is not available??](https://blog.csdn.net/huryer/article/details/91126391)<br>
><span style="color: green"> 要在windows上使用docker-desktop，需要打开Hyper-V；如果要运行VMware 或Oracle VM VirtualBox，需要禁用Hyper-V;鱼和熊掌不可兼得 </span>

#### 2.[解决Windows10中Virtualbox安装虚拟机没有64位选项(N种情形盘点)](https://www.4spaces.org/windows-10-virtualbox-no-64bit/)

#### 3.[Nginx相关介绍](https://www.cnblogs.com/wcwnina/p/8728391.html)

#### 4.[ChromeDriver与Chrome版本对应参照表](https://blog.csdn.net/BinGISer/article/details/88559532) &nbsp;&nbsp;[ChromeDriver下载链接](http://chromedriver.storage.googleapis.com/index.html) &nbsp;&nbsp;[chromedriver安装教程](https://blog.csdn.net/qq_40604853/article/details/81388078)
#### 5.[解决Chrome调试(debugger)总是进入paused in debugger状态](https://blog.csdn.net/jasmine0178/article/details/89636155)
