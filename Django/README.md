# Django 补述：

## 环境搭建
	- anaconda+pycharm
	- anaconda使用
		- conda list: 显示当前环境安装的包
		- conda env list:显示安装的虚拟环境列表
		- conda create -n env_name python=3.6
		- 激活conda的虚拟环境
			- (Linux)source activate env_name
			- (win) activate env_name
		- pip install django=1.8

### 创建第一个django程序
		- 命令行启动
        django-admin startproject project_name
        cd project_name
		python manage.py startapp app_name
        
		运行：python manage.py runserver

  # 1.Django目录
   
   ##### (当项目较小时，即只有一个APP项目时，将templates，static文件存放与项目，APP同级目录)
   
            目录结构：
        |--APP
            |   |--views.py
            |   |-- __init__.py
            |   |-- models.py
            |   |-- urls.py
            |   |-- admin.py
            |   |-- apps.py
            |   |-- tests.py
        |--templates
            |--a.html
        |--static
            |--css
                |--a.css
                |--b.css
            |--js
                |--c.js
                |--d.js
            |--images
                |--e.jpeg
                |--f.jpeg
        |-- djangoproject
            |   |-- __init__.py
            |   |-- settings.py
            |   |-- urls.py
            |   |-- wsgi.py 
        |-- manage.py
        |-- requirements
            |   |-- common.txt
            |   |-- dev.txt
            |   |-- prod.txt
            |   |-- test.txt
        |-- requirements.txt
        
   ##### (当项目较大时，即存在多个APP项目时，将templates，static文件存放在APP目录下)：
   
        目录结构：
        |--APP
            |   |--views.py
            |   |-- __init__.py
            |   |-- models.py
            |   |-- urls.py
            |   |-- admin.py
            |   |-- apps.py
            |   |-- tests.py
                |--templates
                    |--a.html
                |--static
                    |--css
                        |--a.css
                        |--b.css
                    |--js
                        |--c.js
                        |--d.js
                    |--images
                        |--e.jpeg
                        |--f.jpeg
        |-- djangoproject
            |   |-- __init__.py
            |   |-- settings.py
            |   |-- urls.py
            |   |-- wsgi.py 
        |-- manage.py
        |-- requirements
            |   |-- common.txt
            |   |-- dev.txt
            |   |-- prod.txt
            |   |-- test.txt
        |-- requirements.txt
        
   # 2.url编写
    -project目录下的URL设置为：
    
        from django.contrib import admin
        from django.urls import path, include
        
        urlpatterns = [
            path('/', admin.site.urls),
            # home/为主URL，而include的作用是拼接APP目录下的urls.py文件中的path
            # 即此例的URL为：home/timer(必须按这种标准方法写URL)
            path('home/', include('APP_name.urls'))
        
        ]
        
    -APP目录下新建一个urls.py文件：
        from django.contrib import admin
        from django.urls import path
        from . import views  # 导入views文件中的视图函数(标准写法)
        
        urlpatterns = [
        path('admin/', admin.site.urls),
    
        path('timer/',views.timer,name = 'timer'),
    ]
    
   # 3.视图
   
   存在一个settings.py文件，里面存在任意的参数，比如
   USER_NAME = 'chd'
   PASSWORD = 123456
   思考这样一个问题，如何在Python文件中调用settings.py文件中的这两个参数：
   
   1.涉及到scrapy时，解决方法如示：
   
    通过Settings对象的方法:从scrapy.conf中导入settings.py,并使用其中的参数设置
    from scrapy.conf import settings
    
    username = settings.get('USER_NAME') 有时会这样写self.settings.get('USER_NAME')
    password = settings.get('PASSWORD')
    
   2.涉及到Django时，解决方法如示：
   
    from django.conf import settings
    
    调用方法：settings.configure，configure() 可以设置任何配置项，每个参数对应一个值。参数名称必须大写，而且参数名必须是真实存在
     username = settings.USER_NAME
     password = settings.PASSWORD
   
    from django.shortcuts import render
    
    
    def timer(request):
        import time
        ctime = time.strftime('%Y-%m-%d %H:%M:%S')   # 2018-06-30 05:48:11
        """
        render方法：
            1、帮忙找到timer.html取出里面的数据；
            2、按照固定的语法（{}）把变量嵌套到html文件中
        """
        return render(request, 'timer.html', {"date":ctime})    # 使用render方法，返回一个页面
#### ps:当视图HTML文件需要传入多个值时
#### content={
#### 	'name':'chd',
#### 	'age':18
####  }
#### return render(request,'live.html',content = content)
   
   # 4.模板（主目录下新建templates文件夹）
   
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
     
        <script src="/static/js/jquery-3.3.1.js"></script>
        <!--引入css文件-->
        <link rel="stylesheet" href="/static/css/timer.css">
    </head>
    <body>
        <h4>当前时间：{{ date }}</h4>
		<a href="https://www.baidu.com/>
                <img src="/static/images/logo.png" alt="logo"/>
            </a>
    </body>
    <!--引入js文件，注意引入位置，不然找不到h4元素-->
    <script src="/static/js/timer.js"></script>
    </html>
注意：改成自己的图片名称，注意图片和link的前缀：/static/images/ 别写成 static/images/ ，这样会无法显示


### 模板与变量、标签：
	- 变量的表示方法： {{var_name}}
	- 在系统调用模板的时候，会用相应的数据查找相应的变量名称，如果能找到，则填充，或者叫渲染，否则，跳过

	## 模板-标签
	- for标签： {% for .. in .. %}
	- 用法：
			{% for .. in .. %}
				循环语句
			{% endfor %}

	## if标签
	- 用来判断条件
	- 代码示例：

			{% if 条件 %}
				条件成立执行语句
			{% elif 条件 %}}
				条件成立执行语句
			{% else %}
				以上条件都不成立执行语句
			{% endif %}}
			
	 examples：
	 （1）遍历每一个元素：
		{% for i in l %}
		    <p>{{  i }}</p>
		{% endfor %}
		利用{% for obj in list reversed %}反向完成循环

		{% for i in l reversed %}
		    <p>{{  i }}</p>
		{% endfor %}
	（2）遍历一个字典：views.py中有：info = {"name":"yuan","age":22}

		{% for i in info %}
		    <p>{{ i }}</p>
		{% endfor %}
		  页面显示：name:yuan     age:22

	（3）遍历对象数组

		{% for person in person_list %}
		    <p>{{ person.name }}  {{ person.age }}</p>
		{% endfor %}

		{# forloop.counter 序号，默认从1开始计数  counter0的序号，从0开始计数 #}
		{% for person in person_list %}
		    <p>{{ forloop.counter0 }} {{ person.name }}  {{ person.age }}</p>
		{% endfor %}
		
		  页面显示：alex 333       egon 222

			 0 alex 333       1 egon 222
			 
#### csrf_token这个标签用于跨站请求伪造保护。{% csrf_token %}可以渲染出一个input标签。点击提交时，会提交给服务器验证通过校验。　

	（1）代码示例：
	  urls.py:

	from django.contrib import admin
	from django.urls import path, re_path

	from app01 import views

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('index/', views.index),    # 含正则的时候需要使用re_path
	    path('login/', views.login)
	]
　　
    app01/views.py:
  
	from django.shortcuts import render,HttpResponse
	# Create your views here.

	def login(request):
	    if request.method == "POST":
		return HttpResponse("OK")
	    return render(request, "login.html")
	    
    /static/login.html:
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Title</title>
	</head>
	<body>
	<form action="" method="post">
	    {% csrf_token %} # 防跨站请求
	    <input type="text" name="user">
	    <input type="submit">
	</form>
	</body>
	</html>

    
   # 5.settings
   
## 5.1 静态文件（js、css、images...）
    STATIC_URL = '/static/'   # 别名（不要改动）
 
    STATICFILES_DIRS = [     # 别名对应的实际路径（STATICFILES_DIRS不能有任何改动）
        os.path.join(BASE_DIR, "static")  # 对应的是创建的static文件，这个文件名可以变动
    ]
      
## 5.2 templates模板设置
          TEMPLATES = [
           {
               'BACKEND': 'django.template.backends.django.DjangoTemplates',
               'DIRS': [os.path.join(BASE_DIR,'templates')],
               'APP_DIRS': True,
               'OPTIONS': {
                   'context_processors': [
                       'django.template.context_processors.debug',
                       'django.template.context_processors.request',
                       'django.contrib.auth.context_processors.auth',
                       'django.contrib.messages.context_processors.messages',
                   ],
               },
           },
       ]


## 5.3设置目标APP
          INSTALLED_APPS = [
           'django.contrib.admin',
           'django.contrib.auth',
           'django.contrib.contenttypes',
           'django.contrib.sessions',
           'django.contrib.messages',
           'django.contrib.staticfiles',
           'APP_name'
       ]
       
## 5.4 数据库的配置   
#### 5.4.1 sqlite3配置
	   DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	    }
	}
	
#### 5.4.1 MySQL配置
	1. 使用MySQL数据库首先需要安装驱动程序

	pip install PyMySQL
	
	2. 在Django的工程同名子目录的init.py文件中添加如下语句
	import pymysql
	
	pymysql.install_as_MySQLdb():作用是让Django的ORM能以mysqldb的方式来调用PyMySQL。 
	
	3. 修改DATABASES配置信息

	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
			'HOST': '127.0.0.1',  # 数据库主机
			'PORT': 3306,  # 数据库端口
			'USER': 'root',  # 数据库用户名
			'PASSWORD': 'mysql',  # 数据库用户密码
			'NAME': 'django_demo'  # 数据库名字
		}
	}
#### 5.4.1 Oracle配置
	DATABASES = {
		'default': {
		  'ENGINE': 'django.db.backends.oracle',
		  'NAME': 'IP:端口号/service_name',
		  'USER': '用户名',
		  'PASSWORD': '密码',
		}
	  }
### 路由解耦：

#### 三、应用include函数实现分发
    
    　　为了实现路由解耦，创建/first_pro/app01/urls.py文件。将/first_pro/first_pro/urls.py中关于app01的路由配置注释。
    
   -1、应用include函数设置/first_pro/app01/urls分发路径
    
    from django.contrib import admin
    from django.urls import path,re_path, include
     
    from app01 import views
     
     
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('timer/', views.timer),
     
        path('login/', views.login),
     
        #分发：
        # re_path(r"app01/", include("app01.urls"))
        # 改写如下：不用app01
        re_path(r"^", include("app01.urls"))
    ]
    
    （1）分发总结
    　　1）分发配置为re_path(r"app01/", include("app01.urls"))时:访问页面需要按照如下规则：

    　　2）分发配置为re_path(r"^", include("app01.urls"))时：访问页面不需要添加app01:
    
    （2）include使用注意
    　　1）include() 的正则表达式并不包含一个 $ （字符串结尾匹配符），但是包含了一个斜杆／；
    
    　　2）每当Django遇到 include() 时，它将截断匹配的URL，并把剩余的字符串发往包含的URLconf作进一步处理。

   -2、在/first_pro/app01/urls.py进一步配置app01路由

    # -*- coding:utf-8 -*-
       
    from django.contrib import admin
    from django.urls import path,re_path
     
    from app01 import views
     
     
    urlpatterns = [
        # 路由配置：  路径--------->视图函数
        # 正则匹配：r'^articles/2003/$'  以articles/2003/开头且以articles/2003/结尾
        re_path(r'^articles/2003/$', views.special_case_2003),  # special_case_2003(request)
     
        # 正则匹配四位的任意数字，多对一
        re_path(r'^articles/([0-9]{4})/$', views.year_archive),  # year_archive(request,1999)
     
        # 正则匹配一个四位的数字作为年，还要匹配一个2位的数字作为月
        # re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),  # month_archive(request,2009,12)
     
        # 改写为有名分组
        re_path(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$', views.month_archive)  # month_archive(request,y=2009,m=12)
     
        # ([0-9]+)：匹配前面的数字一次或无限次作为详情
        # re_path(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail)
    ]

### 四、路由控制——登录验证示例

   -1、在/first_pro/first_pro/urls.py(主路由)中，编写路由配置login：


    from django.contrib import admin
    from django.urls import path,re_path, include
     
    from app01 import views
     
     
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('timer/', views.timer),
        path('login/', views.login)
    ]
    
   -2、修改/first_pro/app01/views.py文件，配置login视图函数

    from django.shortcuts import render,HttpResponse
     
    def login(request):
        print(request.method)  # GET或POST
        # get请求来的话拿到页面，post请求来的话做校验
        if request.method == 'GET':
            return render(request, "login.html")
        # post请求
        else: 
            print(request.POST)  # <QueryDict: {'user': ['yuan'], 'pwd': ['123']}>
     
            user = request.POST.get("user")
            pwd = request.POST.get("pwd")
     
            if user=="yuan" and pwd=="123":
                return HttpResponse("登录成功")  # 返回字符串
            else:
                return HttpResponse("用户名或密码错误!")
    　　取请求的方式：request.method。
    
    　　得到GET请求的时候，通过render方法拿到页面；得到POST请求的时候，由于request.POST得到一个字典，通过get()方法拿到键值。

   -3、在/first_pro/templates/中，创建login.html模板

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <!--在不指名action的情况下，默认使用当前页面的ip地址和端口（同源），指明情况下时，action='URL' -->
        <form action="http://127.0.0.1:8000/login/" method="post">
            用户名 <input type="text" name="user">
            密码 <input type="password" name="pwd">
            <input type="submit">
        </form>
    </body>
    </html>
    　　action代表的是一个路径。由于同源的原因，可以写为action="http://127.0.0.1:8000/login/"，也可以写为action="/login/"。
    
    　　由于提交的是login函数，在urls.py控制器中查找到对应的path('login/', views.login)。找到对应的视图函数来进行处理。

   -4、在浏览器登录，输入正确用户名和密码后，执行效果：
   
### 五、Django2.0版的path

	思考情况如下：
	urlpatterns = [ 
		re_path('articles/(?P<year>[0-9]{4})/', year_archive), 
		re_path('article/(?P<article_id>[a-zA-Z0-9]+)/detail/', detail_view), 
		re_path('articles/(?P<article_id>[a-zA-Z0-9]+)/edit/', edit_view), 
		re_path('articles/(?P<article_id>[a-zA-Z0-9]+)/delete/', delete_view), 
	]
	
###### 存在两个问题：

	  第一个问题，函数 year_archive 中year参数是字符串类型的，因此需要先转化为整数类型的变量值，当然year=int(year) 不会有诸如如TypeError或者ValueError的异常。那么有没有一种方法，在url中，使得这一转化步骤可以由Django自动完成？

	  第二个问题，三个路由中article_id都是同样的正则表达式，但是你需要写三遍，当之后article_id规则改变后，需要同时修改三处代码，那么有没有一种方法，只需修改一处即可？

　　在Django2.0中，可以使用 path 解决以上的两个问题。

1、基本示例

	from django.urls import path 
	from . import views 
	urlpatterns = [ 
		path('articles/2003/', views.special_case_2003), 
		path('articles/<int:year>/', views.year_archive), 
		path('articles/<int:year>/<int:month>/', views.month_archive), 
		path('articles/<int:year>/<int:month>/<slug>/', views.article_detail), 
			] 
	基本规则：

	1.使用尖括号(<>)从url中捕获值。相当于有名分组，括号内的int是path内置的转换器
	2.捕获值中可以包含一个转化器类型（converter type），比如使用 <int:name> 捕获一个整数变量。若果没有转化器，将匹配任何字符串，当然也包括了 / 字符。
	3.无需添加前导斜杠
	
	对first_pro进行修改：/first_pro/first_pro/urls.py：

	from django.contrib import admin
	from django.urls import path,re_path, include

	from app01 import views

	urlpatterns = [
		path("articles/<int:year>/",views.path_year)   # path_year(request,2010)
	]
	
	对于/first_pro/app01/views.py:
	from django.shortcuts import render,HttpResponse
 
	# Create your views here.
	def month_archive(request,y,m):
		print(m)   # 11
		print(type(m))   # <class 'str'>
		print(y)   # 2010
		print(type(y))   # <class 'str'>
		return HttpResponse(y+"-"+m)


	def path_year(request, year):
		print(year)             # 2010
		print(type(year))    # <class 'int'>
		return HttpResponse("path year")
	运行效果：


###### 以下是根据 2.0官方文档 而整理的示例分析表（了解内容）：　　

	2、path转化器（path converters）
	  文档原文是Path converters，暂且翻译为转化器。

	Django默认支持以下5个转化器：

		str,匹配除了路径分隔符（/）之外的非空字符串，这是默认的形式
		int,匹配正整数，包含0
		slug,匹配字母、数字以及横杠、下划线组成的字符串。（变量常用）
		uuid,匹配格式化的uuid，如 075194d3-6885-417e-a8a8-6c931e272f00
		path,匹配任何非空字符串，包含了路径分隔符 （捕获任何字符串，非空即可，但是?不行作用是分隔符）
		
	3、注册自定义转化器
	对于一些复杂或者复用的需要，可以定义自己的转化器。转化器是一个类或接口，它的要求有三点：

		regex类属性，字符串类型
		to_python(self, value)方法，value是由类属性regex所匹配到的字符串，返回具体的Python变量值，以供Django传递到对应的视图函数中
		to_url(self, value)方法，和to_python相反，value是一个具体的Python变量值，返回其字符串，通常用于url反向引用
	
	应用示例：
	（1）创建/first_pro/app01/url_convert.py文件

	class MonConvert:
		# regex 类属性，字符串类型。因此不能随便取其他名字
		regex = "[0-9]{2}"   # 两位的数字

		# to_python(self, value)方法，value是由类属性regex所匹配到的字符串，返回具体的Python变量值
		def to_python(self, value):
			return int(value)

		# to_url(self, value) 方法，value是一个具体的Python变量值，返回其字符串，通常用于url反向引用
		def to_url(self, value):
			return '%04d' % value
	（2）注册定义的url转换器：/first_pro/first_pro/urls.py

	from django.contrib import admin
	from django.urls import path,re_path, include, register_converter   # 注意register_converter模块引入

	from app01.url_convert import MonConvert   # 引入创建的转换器
 
	# 注册定义的url转换器
	register_converter(MonConvert, "mm")

	from app01 import views

	urlpatterns = [
		path("articles/<mm:month>", views.path_month)
	]
	（3）自定义转化器/first_pro/app01/urls.py

	from django.shortcuts import render,HttpResponse

	# 自定义转化器
	def path_month(request, month):
		print(month, type(month))
		return HttpResponse("path month....")
	（4）访问验证


### 六、路由控制——名称空间

    　　命名空间（英语：Namespace）是表示标识符的可见范围。一个标识符可在多个命名空间中定义，它在不同命名空间中的含义是互不相干的。这样，在一个新的命名空间中可定义任何标识符，它们不会与任何已有的标识符发生冲突，因为已有的定义都处于其它命名空间中。
    
    　　由于name没有作用域，Django在反解URL时，会在项目全局顺序搜索，当查找到第一个name指定URL时，立即返回。
    
    　　我们在开发项目时，会经常使用name属性反解出URL，当不小心在不同的app的urls中定义相同的name时，可能会导致URL反解错误，为了避免这种事情发生，引入了命名空间。
    
    命名空间解决URL反解错误：
    
　　-1）配置命名空间　

    /first_pro/first_pro/urls.py（主路由）：
    
    
    from django.contrib import admin
    from django.urls import path,re_path, include
     
    from app01 import views
     
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('timer/', views.timer),
     
        #分发：
        re_path(r"^app01/", include(("app01.urls","app01"))),   # 换为一个元组
        re_path(r"^app02/", include(("app02.urls","app02"))),
    ]
    　　注意：这里include里面包含的是一个元组　
    
    /first_pro/app01/views.py（APP1下的views）:
    
    from django.shortcuts import reverse
     
    def index(request):
        # 反向解析
        return HttpResponse(reverse("app01:index"))
        
    /first_pro/app02/views.py（APP2下的views）:　
    
    from django.shortcuts import reverse
     
    def index(request):
        # 反向解析
        return HttpResponse(reverse("app02:index"))
    　　2）在页面上访问测试，可以看到引入了命名空间后，URL反解正常。
          
### 七、django项目中使用redis存储session

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


## 七、Model类的使用

###  7.1定义和数据库表映射的类

    - 在应用中的models.py文件中定义class
    - 所有需要使用ORM的class都必须是 models.Model 的子类
    - class中的所有属性对应表格中的字段
    - 字段的类型都必须使用 modles.xxx 不能使用python中的类型
###	7.2字段常用参数

    1. max_length : 规定数值的最大长度
    2. blank : 是否允许字段为空,默认不允许
    3. null : 在DB中控制是否保存为null, 当该字段为空时，Django 会将数据库中该字段设置为 NULL。默认为 False
    4. default : 默认值
    5. unique : 唯一
    6. verbose_name : 假名
    7. choice : 二元选择数组
        """
        一系列二元组，用作此字段的选项。如果提供了二元组，默认表单小部件是一个选择框，而不是标准文本字段，并将限制给出的选项.
        每个二元组的第一个值会储存在数据库中，而第二个值将只会用于在表单中显示
        一个选项列表：
        
            YEAR_IN_SCHOOL_CHOICES = [
                ('FR', 'Freshman'),
                ('SO', 'Sophomore'),
                ('JR', 'Junior'),
                ('SR', 'Senior'),
                ('GR', 'Graduate'),
            ]
        """

###  7.3数据库的迁移
    1. 在命令行中,生成数据迁移的语句(生成sql语句)
        # 先进入目录主目录（cd my_project）

            python3(python) manage.py makemigrations
            
    2. 在命令行中,输入数据迁移的指令

            python3(python) manage.py migrate

            ps : 如果迁移中出现没有变化或者报错,可以尝试强制迁移

            ```
            # 强制迁移命令
            python3 manage.py makemigrations 应用名
            python3 manage.py migrate 应用名
            ```
    3. 对于默认数据库，为了避免出现混乱，如果数据库中没有数据，每次迁移前可以把系统自带的sqlite3数据库删除
    
    4.常见的一些坑：
        -解决Django No changes detected 本地无法生成迁移文件：
            -其中有一种原因是因为你在项目工程Demo的settings.py对新生成的子应用没有进行注册（即INSTALLED_APPS中没有新增新建的APP_name）
		-外键(ForeignKey)和一对一(OneToOneField)的参数中可以看出,都有on_delete参数,而 django 升级到2.0之后,表与表之间关联的时候,必须要写on_delete参数,否则会报异常
    
    
### 7.4查看数据库中的数据

```
1. 启动命令行 : python3 manage.py shell
ps: 注意点: 对orm的操作分为静态函数和非静态函数两种.静态是指在内存中只有一份内容存在,调用的时候使用 类名. 的方式.如果修改了那么所有使用的人都会受影响.
2. 在命令行中导入对应的映射类
	from 应用.models import 类名
3. 使用 objects 属性操作数据库. objects 是 模型中实际和数据库进行交互的 Manager 类的实例化对象.
4. 查询命令
	- 类名.objects.all() 查询数据库表中的所有内容. 返回的结果是一个QuerySet类型,实际上是类列表中装这个一个一个数据对象.
	- 类名.objects.filter(条件) 
```

```
# from 应用名.models import 类名
from myapp.models import Student

# 查询Student表中的所有数据,得到的是一个QuerySet类型
Student.objects.all()

# 如果要取出所有QuerySet类型中的所有数据对象,需要遍历取出所有的对象,再用对象.属性来查看值
s = Student.object.all()
for each in s:
	print(each.name , each.age , each.address , each.phone)

# 如果要进行过滤筛选,使用filter()方法
Student.objects.filter(age=18)

当输入Question.objects.all()查看所有对象时无法显示具体的值
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
等等。<Question: Question object (1)> 对于我们了解这个对象的细节没什么帮助。
让我们通过编辑 Question 模型的代码（位于 polls/models.py 中）来修复这个问题。给 Question 和 Choice 增加 __str__() 方法。

polls/models.py
from django.db import models

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
给模型增加 __str__() 方法是很重要的，这不仅仅能给你在命令行里使用带来方便，Django 自动生成的 admin 里也使用这个方法来表示对象。

注意：这些都是常规的 Python方法。让我们添加一个自定义的方法，这只是为了演示：
polls/models.py
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

```



#### 2. 添加数据

```
对象 = 类()   # 使用类实例化对象
对象.属性 = 值  # 给对应的对象的属性赋值
对象.save()  # 必须要执行保存操作,否则数据没有进入数据库
```

python3 manage.py shell 命令行中添加数据

```
# from 应用名.models import 类名

from myapp.models import Student

# 实例化对象
s = Student()

# 给对象的属性赋值
s.name = '张三'
s.address = '云南昭通'
s.phone = '13377886678'
s.age = 20

# 保存数据
s.save()
```
## 八、Django的cookie序列化

### 序列化（Serialization）：
	简单来说就是将对象持久性的保存起来，因为原来的对象是在内存中，程序运行结束后就要释放内存，所有的对象，变量等都会被清除，而序列化则可以将他们保存在文件中。
	反序列化：读取文件到内存中，转回对象继续使用的过程
	# 序列化
	 def save_cookie(self,response):
		 """
		 序列化cookies
		 ;return：
		 """
	 	cookie_dict = requests.utils.dict_from_cookiejar(response.cookies)
		with open(COOKIE_FILE_PATH,'w+',encoding = 'utf-8') as f:
			json.dump(cookie_dict,f)
			
	  # 读取cookies
	   def read_cookie(self,response):
		 """
		 反序列化cookies
		 ;return：
		 """
		with open(COOKIE_FILE_PATH,'r+',encoding = 'utf-8') as f:
			cookie_dict = json.load(f)
			cookies = requests.utils.cookiejar_from_dict(cookie_dict)
			return cookies
	  
