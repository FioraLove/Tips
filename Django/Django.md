# Django 补述：

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
    </body>
    <!--引入js文件，注意引入位置，不然找不到h4元素-->
    <script src="/static/js/timer.js"></script>
    </html>
    
   # 5.settings
   
   ## 5.1
    STATIC_URL = '/static/'   # 别名（不要改动）
 
    STATICFILES_DIRS = [     # 别名对应的实际路径（STATICFILES_DIRS不能有任何改动）
        os.path.join(BASE_DIR, "static")  # 对应的是创建的static文件，这个文件名可以变动
    ]
    
    
   ## 5.2
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

   ## 5.3
          INSTALLED_APPS = [
           'django.contrib.admin',
           'django.contrib.auth',
           'django.contrib.contenttypes',
           'django.contrib.sessions',
           'django.contrib.messages',
           'django.contrib.staticfiles',
           'APP_name'
       ]

    
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
