## 一、random模块以及随机选择

      random模块的几种方法：
      1.random() 产生大于0小于1之间的随机的小数
      2.uniform(a,b) 产生a, b范指定围内随机小数
      3.randint(a,b) 产生a，b范围内随机整数,包含a，b
      4.randrange(a,b) 产生a, b范围内的整数，包含开头不包含结尾
      5.choice(list) 随机返回序列中的一个数据
      6.shuffle() 打乱列表顺序
       ———————————————— 


### 1.random() 产生大于0小于1之间的随机的小数

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

### 3.randint(a,b) 产生a，b范围内随机整数,包含a，b

    import random
    ret1=random.randint(1,4)
    print(ret1)   #产生1到4之间随机整数，在1,2,3,4之间随机选取一个整数

### 4.randrange(a,b) 产生a, b范围内的整数，包含开头不包含结尾,可指定步长，步长可有可无

    import random
    ret=random.randrange(1,6,2)    步长为2，在1,3,5中随机去一个整数
    print(ret)        # 1 or 3 or 5

### 5.choice(lst) 随机返回序列中的一个数据

    import random
    lst=['a','b','c']
    ret=random.choice(lst)     随机选取lst中的一个元素
    print(ret)    # a or b  or c

### 6.shuffle() 打乱列表顺序

    import random
    lst=['a','b','c']
    random.shuffle(lst)     将lst内有序排列的元素变为无序元素
    print(lst)

    运行结果：

    ['c', 'b', 'a']
    ———————————————— 

