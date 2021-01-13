# 1.templates目录与static目录区别：
    -templates目录是放html静态模板的，static目录是放css和js这些静态文件的。二者都是在settings.py中配置
    
    -templates文件夹是放在project的目录（主目录下）下面的，是项目中或者说项目中所有的应用公用的一些模板
    
    -目录结构：
        |--APP
        |--templates
            |--a.html
        |--static
            |--css
                |--a.css
                |--b.css
            |--js
            |--images
        |-- djangoproject
            |   |--
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
        
# 2.templates文件配置：

    """
        TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
    """
    
# 3.static配置：
    """
        #配置 staitc 目录
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = (
        ("css", os.path.join(STATIC_ROOT,'css')),
        ("js", os.path.join(STATIC_ROOT,'js')),
        ("images", os.path.join(STATIC_ROOT,'images')),
    )
    """
