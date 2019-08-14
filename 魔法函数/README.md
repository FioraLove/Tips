### 1.__repr__和__str__这两个方法都是用于显示的

        上面我们发现在print的时候，两个魔法函数显示的效果是一样的，那这两个魔法函数区别在哪呢，__repr__和__str__这两个方法都是用于显示的，
        __str__是面向用户的，而__repr__面向程序员。在print的时候两者项目一样，但是在交互命令下__repr__同样有着print的效果，
        但是__str__还是输出对象内存地址。也就说在交互式命令下我们可以看到其效果，
        另外__str__ 方法其实调用了 __repr__ 方法。
        
        # -*- coding:utf-8 -*-
        class Student(object):
            def __init__(self, id, name, age):
                self.id = id
                self.name = name
                self.age = age

            def __str__(self):
                return ('学号：{} -- 姓名：{} -- 年龄：{}'.format(self.id, self.name, self.age))


        s = Student(111, "Bob", 18)
        print(s)
        # 不加__str__魔法函数时，输出结果：<__main__.Student object at 0x000000000227FF60>
        # 加了__str__魔法函数时，输出结果：学号：111 -- 姓名：Bob -- 年龄：18

### 2. Python中这个__repr__函数，对应repr(object)这个函数，返回一个可以用来表示对象的可打印字符串

        class A(object):

            def __init__(self, name=None, id=1):
                self.name = name
                self.id = id

            # 改进后：直接打印hello Python
            def __repr__(self):
                return ('hello python')


        if __name__ == '__main__':
            a = A()
            print(a)  # 打印结果为<__main__.A object at 0x000000000283FF60>表示为内存地址


        # __str__()
        class A():
            def __init__(self, name=None, id=1):
                self.id = id
                self.name = name

            def __str__(self):
                return "进入函数"


        if __name__ == '__main__':
            print(A())


### 3. 魔法函数__doc__　表示类的描述信息(仅展示首次出现双引号中的注释内容)


        class foo(object):
            # hee（不显示）
            """hello python xxx"""
            """heoo"""

            def func(self):
                """hello man（不显示）"""
                print('hello python')


        print(foo.__doc__)


### 4.魔法函数__module__ 和  __class__

          __module__ 和  __class__ :
          __module__ 表示当前操作的对象在那个模块
          __class__  表示当前操作的对象的类是什么


            class C:

                def __init__(self):
                    self.name = 'wupeiqi'

            from lib.aa import C

            obj = C()
            print obj.__module__  # 输出 lib.aa，即：输出模块
            print obj.__class__      # 输出 lib.aa.C，即：输出类


### 5.魔法函数__init__ 构造方法，通过类创建对象时，自动触发执行。

### 6.魔法函数__del__
         析构方法，当对象在内存中被释放时，自动触发执行。

        注：此方法一般无须定义，因为Python是一门高级语言，程序员在使用时无需关心内存的分配和释放，因为此工作都是交给Python解释器来执行，所以，析构函数的调用是由解释器在进行垃圾回收时自动触发执行的


###  7.魔法函数__call__ 对象后面加括号，触发执行。注：构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()
        class Foo:

            def __init__(self):
                pass

            def __call__(self, *args, **kwargs):
                print ('__call__')


        obj = Foo()  # 执行 __init__
        obj()  # 执行 __call__
        
### 8.魔法函数__dict__ 查看类或对象中的所有成员 

        class Province(object):
            country = 'China'

            def __init__(self, name, count):
                self.name = name
                self.count = count

            def func(self, *args, **kwargs):
                print('func')


        # 获取类的成员，即：静态字段、方法、
        print(Province.__dict__)

        # 输出：{'country': 'China', '__module__': '__main__', 'func': <function func at 0x10be30f50>, '__init__': <function __init__ at 0x10be30ed8>, '__doc__': None}

        obj1 = Province('HeBei', 10000)
        print(obj1.__dict__)

        # 获取 对象obj1 的成员
        # 输出：{'count': 10000, 'name': 'HeBei'}

        obj2 = Province('HeNan', 3888)
        print(obj2.__dict__)
        # 获取 对象obj1 的成员
        # 输出：{'count': 3888, 'name': 'HeNan'}
        
### 9.魔法函数__getitem__、__setitem__、__delitem__用于索引操作，如字典。以上分别表示获取、设置、删除数据

    class Foo(object):

        def __getitem__(self, key):
            print('__getitem__', key)

        def __setitem__(self, key, value):
            print('__setitem__', key, value)

        def __delitem__(self, key):
            print('__delitem__', key)


    obj = Foo()

    result = obj['k1']  # 自动触发执行 __getitem__
    obj['k2'] = 'alex'  # 自动触发执行 __setitem__
    del obj['k1']
    
### 10.
