### [time/datetime模块](https://www.cnblogs.com/xiugeng/p/8643791.html)
<img src="https://github.com/FioraLove/Tips/blob/Dev-1/%E5%85%B6%E5%AE%83/images/5b1f582a33199.jpg?raw=true" width=60%> <br>

#### 1.时间戳(timestamp)：时间戳表示从1970年1月1日00:00:00开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。
    >>> time.time()
    1521948761.733449
    >>> type(time.time())
    <class 'float'>

#### 2.格式化的时间字符串：2014-11-11 11:11，即time.strftime('%Y-%m-%d')
    >>> import time
    >>> time.strftime('%Y-%m-%d')
    '2019-10-23'
    >>> time.strftime('%Y-%m-%d %H:%M:%S')
    '2019-10-23 09:03:45'
#### 3.元组(struct_time)共九个元素,返回struct_time的函数主要有gmtime()，localtime()，strptime()

    >>> import time
    >>> time.localtime()
    time.struct_time(
    tm_year=2018,   # 年
    tm_mon=2,  # 月    
    tm_mday=26,   # 日
    tm_hour=2,  # 时
    tm_min=47,  # 分
    tm_sec=49,  # 秒
    tm_wday=0,   # 星期几（0代表星期日）
    tm_yday=57,   # 一年中第几天
    tm_isdst=0)   # 是否夏令时，默认是-1

```获取元祖struct_time中的某一项：time.localtime()[n]:按照元祖逻辑切片取值```

