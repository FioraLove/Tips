## 1.在同一个文件夹下

1.1调用函数
  source.py文件：

  def func():
      pass

  new.py文件：
    import source
    # 或者
    from  source import func

1.2调用类
    Student.py文件：

    class Student:
        def __init__(self, name, age, sex):
            self name = name
            self age = age
            self sex =sex

        def learn(self):
            print("学生学习！")
    
    handler.py文件：

    from Student import Student
    s = Student('egon', 18, 'male')
    s.learn()

    # 或者
    import Student
    s = Student.Student('jack', 28, 'male')
    s.learn()

## 2.在不同一个文件夹下
由于Python import模块时，是在sys.path里按顺序查找的。需要先将要使用文件的文件路径加入sys.path中。

    import sys
    sys.path.appent(r'/home/admin/PythonProject/CourseSelesct/')
    import Student

    s = Student.Student('egon', 18, 'male')
    s.learn()
