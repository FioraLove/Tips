## 一、[random模块以及随机选择](https://www.cnblogs.com/dylancao/p/8202888.html) <br>

<img src = "https://github.com/FioraLove/Tips/blob/Dev-1/%E5%85%B6%E5%AE%83/images/5927f2c7269aa.jpg?raw=true" width=70%><br>


      random模块的几种方法：
      1.random() 产生大于0小于1之间的随机的小数
      2.uniform(a,b) 产生a, b范指定围内随机小数
      3.randint(a,b) 产生a，b范围内随机整数,包含a，b
      4.randrange(a,b) 产生a, b范围内的整数，包含开头不包含结尾
      5.choice(list) 随机返回序列中的一个数据,可以从任何序列，比如list列表中，选取一个随机的元素返回，可以用于字符串、列表、元组等
      6.shuffle() 打乱列表顺序
      7.sample((seq, n) 从序列seq中选择n个随机且独立的元素,比如list列表中，选取一个随机的元素返回，可以用于字符串、列表、元组等
       ———————————————— 


#### 1.random() 产生大于0小于1之间的随机的小数

    import random
    ret=random.random()
    print(ret)   #产生0到1之间随机小数
    运行结果：
    0.7992248491999175

### 2.uniform(a,b) 产生a, b范指定围内随机小数

    import random
    ret=random.uniform(1,4)
    print(ret)     #产生1到4之间随机小数

    运行结果：

    2.7213781289518244   

#### 3.randint(a,b) 产生a，b范围内随机整数,包含a，b

    import random
    ret1=random.randint(1,4)
    print(ret1)   #产生1到4之间随机整数，在1,2,3,4之间随机选取一个整数

#### 4.randrange(a,b) 产生a, b范围内的整数，包含开头不包含结尾,可指定步长，步长可有可无

    import random
    ret=random.randrange(1,6,2)    步长为2，在1,3,5中随机去一个整数
    print(ret)        # 1 or 3 or 5

#### 5.choice(lst) 随机返回序列中的一个数据

    import random
    lst=['a','b','c']
    ret=random.choice(lst)     随机选取lst中的一个元素
    print(ret)    # a or b  or c

#### 6.shuffle() 打乱列表顺序

    import random
    lst=['a','b','c']
    random.shuffle(lst)     将lst内有序排列的元素变为无序元素
    print(lst)

    运行结果：

    ['c', 'b', 'a']
    ———————————————— 
#### 7.random.sample(seq,n)序列seq中选择n个随机且独立的元素
      info =['a', 'b', 'c', 'd', 'e']
      random.sample(info,2)
      
      运行结果：
      ['d', 'e']

### [二、string模块](https://github.com/FioraLove/Tips/blob/Dev-1/%E4%B8%89%E6%96%B9%E5%BA%93/string%E6%A8%A1%E5%9D%97.py)

    a = string.ascii_letters  # 表示获取包含大小写的所有英文字母
    b = string.ascii_lowercase  # 获取所有的小写字母
    c = string.ascii_uppercase  # 获取所有的大写英文字母
    d = string.digits  # 获取所有的数字
    
### [三、os模块](https://github.com/FioraLove/Tips/blob/Dev-1/%E4%B8%89%E6%96%B9%E5%BA%93/os%E6%A8%A1%E5%9D%97.md)
    os.path.dirname()
    os.path.abspath(__file__)
    os.path.join(path1,path2,...path)
    os.systeam('程序名')：启动py程序
       

### [调用其它文件的类和函数](https://www.cnblogs.com/xiugeng/p/8681520.html)   &nbsp;&nbsp;&nbsp;[源文件出处](https://github.com/FioraLove/Tips/blob/Dev-1/%E4%B8%89%E6%96%B9%E5%BA%93/%E8%B0%83%E7%94%A8%E5%85%B6%E5%AE%83%E6%96%87%E4%BB%B6%E7%9A%84%E7%B1%BB%E5%92%8C%E5%87%BD%E6%95%B0.py)
    同一文件下调用其它文件的
    不同文件下调用类和函数:由于Python import模块时，是在sys.path里按顺序查找的。需要先将要使用文件的文件路径加入sys.path中。

    import sys
    sys.path.appent(r'/home/admin/PythonProject/CourseSelesct/')
    import Student

    s = Student.Student('egon', 18, 'male')
    s.learn()
    
### [四、sys模块](https://www.cnblogs.com/xiugeng/p/8716223.html)
    sys.version：python解释器的版本信息
    sys.path：查找模块所在目录的目录名列表（模块搜索路径，初始化时使用pythonPATH环境变量的值）
    sys.platform：输出一个字符串，是解释器正在其上运行的“平台”名称。一般是操作系统名称，如果是Jpython则是JAVA虚拟机
    sys.getrecursionlimit()  # 获取最大递归层数  默认是1000（0-999）
    sys.setrecursionlimit(1200)  # 设置最大递归层数
    sys.getdefaultencoding()   # 获取解释器默认编码
    sys.getfilesystemencoding()   # 获取内存数据存到文件里的默认编码
