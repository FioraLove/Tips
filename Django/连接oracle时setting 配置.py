"""
打开settings.py文件,配置oracle连接:

DATABASE_ENGINE = 'oracle' # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = 'django' # Or path to database file if using sqlite3.
DATABASE_USER = 'django' # Not used with sqlite3.
DATABASE_PASSWORD = 'django' # Not used with sqlite3.
DATABASE_HOST = '' # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = '1521' # Set to empty string for default. Not used with sqlite3.

DATABASE_ENGINE 填入数据库驱动,这里自然填入oracle

DATABASE_NAME 填入sid,可以查看本机的tnsnames.ora是如何配置的

DATABASE_USER 数据库用户

DATABASE_PASSWORD 用户密码

DATABASE_HOST 直接填入ip地址就可以(如果数据库在本机也可以不填)

DATABASE_PORT oracle服务的端口号

"""
# 数据库地址
DB_SERVER = "1192.5.5.5"
# 数据库用户
DB_USER = "xx"
# 数据库密码
DB_PASSWORD = "123456"
# 数据库名
DB_DATABASE = "xx"


# Database

# 保存为Django自带的轻量sqlite3数据库
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': DB_DATABASE, #数据库名称
        'USER': DB_USER, #用户名
        'PASSWORD': DB_PASSWORD, #密码
        'HOST': DB_SERVER , #HOST
        'PORT': '1521', #端口
        }
}
