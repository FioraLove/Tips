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
