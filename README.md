# Tips
详细记录一些常见易混知识点，涵盖python，Django，js，SQL，web，spider....

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
