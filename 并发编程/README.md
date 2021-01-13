## [并发编程](https://www.cnblogs.com/xiugeng/p/8998022.html)
<img src="../其它/images/5a2e23a22908f.jpg" width=60%/><br>

### 一、为什么要有操作系统 

    　　现代的计算机系统主要是由一个或者多个处理器，主存，硬盘，键盘，鼠标，显示器，打印机，网络接口及其他输入输出设备组成。
    　　程序员无法把所有的硬件操作细节都了解到，管理这些硬件并且加以优化使用是非常繁琐的工作，这个繁琐的工作就是操作系统来干的，有了他，程序员就从这些繁琐的工作中解脱了出来，只需要考虑自己的应用软件的编写就可以了，应用软件直接使用操作系统提供的功能来间接使用硬件。


### 二、什么是操作系统及操作系统功能

    　　定义：操作系统就是一个协调、管理和控制计算机硬件资源和软件资源的控制程序。
    
    　　操作系统位于计算机硬件与应用软件之间，本质也是一个软件。操作系统由操作系统的内核（运行于内核态，管理硬件资源）以及系统调用（运行于用户态，为应用程序员写的应用程序提供系统调用接口）两部分组成。
    　　
    
    　　上图是操作系统所处的位置，操作系统应该分为两部分功能：
    
            1、隐藏了丑陋的硬件调用接口
            　　为应用程序员提供调用硬件资源的更好，更简单，更清>晰的模型（系统调用接口）。应用程序员有了这些接口后，就不用再考虑操作硬件的细节，专心开发自己的应用程序即可。
            
            例如：操作系统提供了文件这个抽象概念，对文件的操作就是对磁盘的操作，有了文件我们无需再去考虑关于磁盘的读写控制（比如控制磁盘转动，移动磁头读写数据等细节）。
            
            2、将应用程序对硬件资源的竞态请求变得有序化。
            例如：很多应用软件其实是共享一套计算机硬件，比方说有可能有三个应用程序同时需要申请打印机来输出内容，那么a程序竞争到了打印机资源就打印，然后可能是b竞争到打印机资源，也可能是c，这就导致了无序，打印机可能打印一段a的内容然后又去打印c...,操作系>统的一个功能就是将这种无序变得有序。

   ### 三、操作系统发展史
   
    1、第一代计算机（1940~1955）：真空管和穿孔卡片
    　　这个时期的电脑没有操作系统，所有程序设计都是直接操控硬件。程序员拿着他的插件版到机房里，将自己的插件板街道计算机里，这几个小时内他独享整个计算机资源，后面的一批人都得等着
    　　优点：在申请时间段内独享资源，即时调试程序。
    　　缺点：浪费计算机资源，一个时间段只有一个人用。
    
    2、第二代计算机（1955~1965）：晶体管和批处理系统
    　　程序员在穿孔卡片上写好程序，然后放在读卡机上，收集足够后，这些卡片读进磁带。机房管理人员把磁带装到磁带机上，操作人员装入一个特殊程序，它从磁带读取作业并运行输出到第二盘磁带，当作业全完成，取下输入和输出的磁带，把输出磁带拿到1401机器上进行脱机打印。
    　　1401：I/O操作  7094：计算操作
    　　特点：输入攒一大波、仍是顺序计算、输出攒一大波
    　　优点：批处理，节省时间
    　　缺点：1.流程需要人参与控制；2.计算过程仍然是顺序计算--》串行计算
    　　　　　3.程序员等待结果和重新调试的过程都需要等同批次的其他程序都运作完才可以。（影响开发效率）
    
    3、第三代计算机（1965~1980）：集成电路芯片和多道程序设计
    　　由于第二代计算机有两套机型：
    
    　　7094大型科学计算机：主要用于科学计算和工程计算。（面向字）
    　　1401商用计算机：主要用于银行和保险从事磁带归档和打印服务。（面向字符）
    　　IBM通过system/360系列来同时满足上述要求，低档机与1401相当，高档机与7094相当。
    
    （1）解决人为参与问题
    　　将作业从卡片读入磁盘，于是任何时刻当一个作业结束时，操作系统就能将一个作业从磁带读出，装进空出来的内存区域运行，这种技术叫做同时的外部设备联机操作：SPOOLING，该技术同时用于输出。
    
    （2）解决串行计算问题
    　　cpu运行的速度远远快于读取硬盘数据的速度，因此引入了内存，CPU可以非常快速地读取内存的数据。
    　　多道技术：多道指得是多个程序，解决多个程序竞争或共享同一个资源的有序调度问题，解决方式是多路复用，多路复用分时间复用和空间上的复用。
    　　空间上的复用：复用内存空间，内存同时存多个程序
          　　空间复用存在的问题：必须保证物理层面上多个程序的内存是互相隔离的。否则会丧失安全性和稳定性。正是由于内存物理隔离的问题，第三代计算机操作系统依然是批处理
    　　时间上的复用：大家共享cpu的时间，当一个程序在等待I/O时，另一个程序可以使用cpu，如果内存中可以同时存放足够多的作业，则cpu的利用率可以接近100%，类似于小学数学所学的统筹方法。
          　　切换情形：1）会在一个进程遇到io时进行；2）一个进程占用cpu时间过长也会切换，或者说被操作系统夺走cpu的执行权限。
    
    （3）解决像第一代一样即时调试自己的程序
    　　分时操作系统：多个联机终端+多道技术，索引计算机能够为许多用户提供快速的交互式服务，所有的用户都以为自己独享了计算机资源
    　　UNIX:Ken Thompson开发了一个简易、单用户版本的MULTICS，为了使程序能在任何版本的unix上运行，IEEE提出了一个unix标准，即posix（可移植的操作系统接口Portable Operating System Interface）
    　　minix:教学用系统
    　　Linux:芬兰学生Linus Torvalds基于minix它编写
      
    
### 4、第四代计算机（1980~至今）：个人计算机

    四、总结
    1、操作系统的作用
    　　1.隐藏丑陋复杂的硬件接口，提供良好的抽象接口
    　　2.管理、调度进程，并将多个进程对硬件的竞争变得有序。
    
    2、多道技术
    　　1.产生的背景：针对单核，实现并发（看起来多个进程像在同时运行，注意和并行的区别）  
    　　　　　　　　现在的主机一般是多核（几个核最多可以几个并行），那么每个核都会利用多道技术。
    　　　　　　　　有4个cpu，运行于cpu1的某个程序遇到io阻塞，会等到io结束再重新调度，会被调度到4个cpu中的任意一个，具体由操作系统调度算法决定。
    　　2.空间上的复用：内存中同时有多道程序
    　　3.时间上的复用：复用一个cpu的时间片
    　　　　　　注意：遇到io切，占用cpu时间过长也切，核心在于切之前将进程的状态保存下来，这样才能保证下次切换回来时，能基于上次切走的位置继续运行

## 多进程开发：

### 一、multiprocessing模块介绍

        python中的多线程无法利用多核优势，如果想要充分地使用多核CPU的资源（os.cpu\_count\(\)查看），在python中大部分情况需要使用多进程。
    
    　　Python提供了multiprocessing模块用来开启子进程，并在子进程中执行我们定制的任务（比如函数），该模块与多线程模块threading的编程接口类似。multiprocessing模块的功能众多：支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。
    
    　　需要再次强调的一点是：与线程不同，进程没有任何共享状态，进程修改的数据，改动仅限于该进程内

### 二、Process类的使用
 
    　　注意：在windows中Process()必须放到# if __name__ == '__main__':下：
    
    　　这是由于Windows没有fork，多处理模式启动一个新的Python进程并导入调用模块。如果在导入时调用Process()，那么这个将启动无限继承的新进程（或直到机器耗尽资源）。
    
    　　这对隐藏对Process()内部调用的原因，使用if __name__ == '__main__'，这个if语句中的语句将不会在导入时被调用。
    
   -2.1 创建并开启子进程的两种方法
    
        方式一：通过multiprocessing模块开启子进程
    from multiprocessing import Process
    import time
    
    def task(name):
        print("%s is running" % name)
        time.sleep(3)
        print("%s is done" % name)
    
    if __name__ == '__main__':
        p = Process(target=task, args=('子进程1',))  # 得到对象
        # Process(target=task, kwargs={'name': "子进程1"})

        p.start()   # 给操作系统发送启动信号
        print("主")
        """
        主
        子进程1 is running
        子进程1 is done
        """
        
   -方式二：不用默认的multiprocessing模块，继承并订制自己的类
    
    from multiprocessing import Process
    import time
    class MyProcess(Process):
        def __init__(self, name):
            super().__init__()
            self.name = name
    
        def run(self):  # run()是固定形式，p.start本质是调用的绑定的run方法
            print('%s is running'%self.name)
            time.sleep(3)
            print("%s is done" % self.name)
    
    if __name__ == '__main__':
        p = MyProcess('子进程')
        p.start()   # 给操作系统发送启动信号
        print('主')
        """
        主
        子进程 is running   # 间隔三秒
        子进程 is done
        """
        
   -2.2 练习题：
   
       1、思考开启进程的方式一和方式二各开启了几个进程？
    
    答：两个方式都是开启了一个主进程和四个子进程。
    
    　　2、进程之间的内存空间是共享的还是隔离的？下述代码执行的结果？
    
    答：进程之间的内存空间是隔离的，执行输出：“子进程内：0”
    
### 三.Process对象的join方法

   -3.1 join方法：优先运行子进程，主进程卡在原地，子进程结束后，运行主进程后面的代码
    简单理解为：若有join()方法，先执行子程序，然后在执行主程序；不存在join方法时，直接先执行主程序

    from multiprocessing import Process
    import time, os
    
    def task():
        print('%s is running, parent id is <%s>' % (os.getpid(), os.getppid()))   # 进程和父进程查看方式
        time.sleep(3)
        print("%s is done, parent id is <%s>" % (os.getpid(), os.getppid()))
    
    if __name__ == '__main__':
        p = Process(target=task, )
        p.start()
    
        p.join()   # 优先运行子进程，主进程卡在原地
        print('主进程', os.getpid(), 'pycharm ID', os.getppid())
        print(p.pid)  # 子进程运行完，变为僵尸进程，主进程仍能够查到子进程的pid，当主进程结束后，所有僵尸子进程将被丢掉。
        """
        is running, parent id is <827>
        is done, parent id is <827>
        主进程 827 pycharm ID 504
        """
        
   -3.2 并发执行，约束主程序要等在子程序后结束
   
    from multiprocessing import Process
    import time, os
    
    def task(name ,n):
        print('%s is running' % name)
        time.sleep(n)
    
    if __name__ == '__main__':
        start = time.time()
        p1 = Process(target=task, args=("子进程1",5))
        p2 = Process(target=task, args=("子进程2",3))
        p3 = Process(target=task, args=("子进程3",2))
        """
        进程开启顺序由操作系统统筹控制，顺序是不一定的
        主进程 1014 pycharm ID 504
        子进程2 is running
        子进程1 is running
        子进程3 is running
        """
        p1.start()
        p2.start()
        p3.start()
        # 再添加join函数前，主程序的执行输出次序是完全随机的，需要加join()保证主程序等到在子进程之后执行完成
        p1.join()
        p2.join()
        p3.join()
        # 以上并非串行执行，实际是并发执行，只是约束了主程序要等在子程序后结束
        # print('主进程', os.getpid(), 'pycharm ID', os.getppid())
        print("主进程", (time.time()-start))
        """
        子进程1 is running
        子进程2 is running
        子进程3 is running
        主进程 5.010260343551636   # 主程序只等了5秒，说明确实是并发执行
        """

### 四.守护进程

       主进程创建守护进程
    
    　　其一：守护进程会在主进程代码执行结束后就终止
    
    　　其二：守护进程内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children
    
    注意：进程之间是互相独立的，主进程代码运行结束，守护进程随即终止
    
   -4.1 守护进程一定要在进程开启前设置
   
    案例一：验证守护进程内部不能再开子进程
    from multiprocessing import Process
    import time
    
    def task(name):
        print("%s is running" % name)
        time.sleep(2)
    
    
    if __name__ == '__main__':
        p = Process(target=task, args=('子进程', ))
        p.daemon=True    # 守护进程一定要在进程开启前设置
        p.start()
    
        print("主进程")
    """
    主进程    ————》子进程还没开始就已经结束了
    """  
    
    案例二：验证守护进程内部不能再开子进程 
    
    # 验证守护进程内部能再开子进程——》守护进程再开子进程会造成问题：会造成一堆孤儿
    from multiprocessing import Process
    import time
    
    def task(name):
        print("%s is running" % name)
        time.sleep(2)
        p = Process(target=time.sleep, args=(3, ))
        p.start()
    
    if __name__ == '__main__':
        p = Process(target=task, args=('子进程', ))
        p.daemon=True    # 守护进程一定要在进程开启前设置
        p.start()
    
        p.join()   # 让主进程等待子进程结束
    
        print("主进程")
    """
    AssertionError: daemonic processes are not allowed to have children
    """ 
    
    案例三：
    from multiprocessing import Process

    import time
    def foo():
        print(123)
        time.sleep(1)
        print("end123")
    
    def bar():
        print(456)
        time.sleep(3)
        print("end456")
    
    if __name__ == '__main__':
        p1=Process(target=foo)
        p2=Process(target=bar)
    
        p1.daemon=True   # 主进程代码执行完毕后，守护进程死
        p1.start()
        p2.start()
        print("main-------")
        """
        不存在join()方法，可以理解为先执行主程序，再执行子程序p1，p2
        而且p1.daemon = Ture,即p1为守护程序      
        """
        
### 六.互斥锁
   
    # 互斥锁（进程同步）进程之间数据不共享,但是共享同一套文件系统,所以访问同一个文件,或同一个打印终端,是没有问题的,而共享带来的是竞争，竞争带来的结果就是错乱
    from multiprocessing import Process,Lock
    import time
    
    def task(name):
        print('%s 第一次' % name)
        time.sleep(1)
        print('%s 第二次' % name)
        time.sleep(1)
        print('%s 第三次' % name)
    # 并发运行,效率高,但竞争同一打印终端，谁抢到了谁打印
    
    if __name__ == '__main__':
        for i in range(3):
            p = Process(target=task, args=('进程%s' % i, ))
            p.start()
            
            
    案例二：
    from multiprocessing import Process, Lock
    import time
    
    def task(name, mutex):
        mutex.acquire()   # 上锁，哪个进程抢到锁，就一直给他运行
        print('%s 第一次' % name)
        time.sleep(1)
        print('%s 第二次' % name)
        time.sleep(1)
        print('%s 第三次' % name)
        mutex.release()   # 解锁
    
    
    if __name__ == '__main__':
        mutex = Lock()   # 只实例化一次，并传给子进程，要保证所有进程用同一把锁
        for i in range(3):
            p = Process(target=task, args=('进程%s' % i, mutex))  # 传递给子进程的锁
            p.start()
    """
    进程0 第一次
    进程0 第二次
    进程0 第三次
    进程1 第一次
    进程1 第二次
    进程1 第三次
    进程2 第一次
    进程2 第二次
    进程2 第三次
    """
    
  #####　互斥锁的意思就是互相排斥，如果把多个进程比喻为多个人，互斥锁的工作原理就是多个人都要去争抢同一个资源：卫生间，一个人抢到卫生间后上一把锁，其他人都要等着，等到这个完成任务后释放锁，其他人才有可能有一个抢到......所以互斥锁的原理，就是把并发改成穿行，降低了效率，但保证了数据安全不错乱

   -互斥锁运用：买票案例：db.txt里只有一张票，由于并发卖出了10次。需要把购票行为改为串行，只有第一个人可以买到票
   
    from multiprocessing import Process, Lock
    import json, time
    
    def search(name):
        """查票"""
        time.sleep(1)   # 模拟网络延迟,并发去看票数
        dic = json.load(open('db.txt', 'r', encoding='utf-8'))
        print('<%s> 查看到剩余票数[%s]' %(name, dic['count']))
    
    
    def get(name):
        """买票"""
        time.sleep(1)   # 模拟网络延迟
        dic = json.load(open('db.txt', 'r', encoding='utf-8'))
        if dic['count'] > 0:    # 确认有票
            dic['count'] -= 1
            time.sleep(3)
            # 写入文件，即购票成功，这个必须是基于其他人购票的结果，由并发改为串行
            json.dump(dic, open('db.txt', 'w', encoding='utf-8'))
            print('<%s> 购票成功' % name)
    
    
    def task(name, mutex):
        search(name)   # 查票并发执行，人人都可以看到票
        mutex.acquire()    # 上锁
        get(name)      # 购票改为串行，其他人都必须等着
        mutex.release()    # 解锁
    
    
    if __name__ == '__main__':
        mutex = Lock()
        for i in range(10):
            p = Process(target=task, args=('路人%s' % i, mutex))
            p.start()
            

### 总结：

    　　加锁可以保证多个进程修改同一块数据时，同一时间只能有一个任务可以进行修改，即串行的修改，没错，速度是慢了，但牺牲了速度却保证了数据安全。
    
    虽然可以用文件共享数据实现进程间通信，但问题是：
    
    　　1.效率低（共享数据基于文件，而文件是硬盘上的数据）
    
    　　2.需要自己加锁处理
    
    　　因此我们最好找寻一种解决方案能够兼顾：1、效率高（多个进程共享一块内存的数据）2、帮我们处理好锁问题。这就是mutiprocessing模块为我们提供的基于消息的IPC通信机制：队列和管道。
    
    　　1 队列和管道都是将数据存放于内存中
    
    　　2 队列又是基于（管道+锁）实现的，可以让我们从复杂的锁问题中解脱出来
    
    　　我们应该尽量避免使用共享数据，尽可能使用消息传递和队列，避免处理复杂的同步和锁问题，而且在进程数目增多时，往往可以获得更好的可获展性
       
### 六.队列

进程彼此之间互相隔离，要实现进程间通信（IPC），multiprocessing模块支持两种形式：队列和管道，这两种方式都是使用消息传递的。

   -1、创建队列的类（底层就是以管道和锁定的方式实现）
   
    Queue([maxsize]):创建共享的进程队列，Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。
    
   -2、参数介绍
   
    　　maxsize是队列中允许最大项数，省略则无大小限制。
    
    　　但需要明确：
    
    　　　　1、队列内存放的是消息而非大数据；
    
    　　　　2、队列占用的是内存空间，因而maxsize即使是无大小限制也受限于内存大小。
    
   -3、主要方法介绍 
    
    q.put方法用以插入数据到队列中，put方法还有两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。如果超时，会抛出Queue.Full异常。如果blocked为False，但该Queue已满，会立即抛出Queue.Full异常。
    q.get方法可以从队列读取并且删除一个元素。同样，get方法有两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，那么在等待时间内没有取到任何元素，会抛出Queue.Empty异常。如果blocked为False，有两种情况存在，如果Queue有一个值可用，则立即返回该值，否则，如果队列为空，则立即抛出Queue.Empty异常.
     
    q.get_nowait():同q.get(False)
    q.put_nowait():同q.put(False)
    
    q.empty():调用此方法时q为空则返回True，该结果不可靠，比如在返回True的过程中，如果队列中又加入了项目。
    q.full()：调用此方法时q已满则返回True，该结果不可靠，比如在返回True的过程中，如果队列中的项目被取走。
    q.qsize():返回队列中目前项目的正确数量，结果也不可靠，理由同q.empty()和q.full()一样
    
   -4、其他方法
    
    q.cancel_join_thread():不会在进程退出时自动连接后台线程。可以防止join_thread()方法阻塞
    
    q.close():关闭队列，防止队列中加入更多数据。调用此方法，后台线程将继续写入那些已经入队列但尚未写入的数据，但将在此方法完成时马上关闭。
    如果q被垃圾收集，将调用此方法。关闭队列不会在队列使用者中产生任何类型的数据结束信号或异常。
    例如，如果某个使用者正在被阻塞在get()操作上，关闭生产者中的队列不会导致get()方法返回错误。
    
    q.join_thread()：连接队列的后台线程。此方法用于在调用q.close()方法之后，等待所有队列项被消耗。
    默认情况下，此方法由不是q的原始创建者的所有进程调用。调用q.cancel_join_thread方法可以禁止这种行为
    
   -5、队列的使用
    
    
    from multiprocessing import Queue
    
    # 队列中应该放消息，不应该放大文件大数据
    # 队列可以不设置长度，但是队列是受制于内存大小的，不可能无限存放
    q = Queue(3)  # 指定队列大小
    q.put('hello')
    q.put({'a': 1})
    q.put([3,3,3,])
    
    print(q.full())   # 查看队列是否满了  # True
    # q.put(123)    # 队列满了再往里面放时，被锁住，只能在原地卡着。
    
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.empty())   # 判断队列是否全部清空  # True
    
    # print(q.get())   # 由于已经空了，程序也卡在原处
    """
    True
    hello
    {'a': 1}
    [3, 3, 3]
    True
    """   
    
### 生产者消费模型

    在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题。该模式通过平衡生产线程和消费线程的工作能力来提高程序的整体处理数据的速度。

    为什么要使用生产者消费者模型？
    
    　　生产者指的是生产数据的任务，消费者指的是处理数据的任务。
    　　在并发编程中，如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式
    
    什么是生产者和消费者模式？
    
    　　生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。
    　　生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。
        这个阻塞队列就是用来给生产者和消费者解耦的 
        
   -三种实现方式：
   
   -1.基于队列实现生产者消费模型
   
    from multiprocessing import Process,Queue
    import time,random,os
    def consumer(q,name):
        while True:
            res=q.get()
            time.sleep(random.randint(1,3))
            print('\033[43m%s 吃 %s\033[0m' %(name,res))
    
    def producer(q,name,food):
        for i in range(3):
            time.sleep(random.randint(1,3))
            res='%s%s' %(food,i)
            q.put(res)
            print('\033[45m%s 生产了 %s\033[0m' %(name,res))
    
    if __name__ == '__main__':
        q=Queue()
        #生产者们:即厨师们
        p1=Process(target=producer,args=(q,'egon','包子'))

    #消费者们:即吃货们
    c1=Process(target=consumer,args=(q,'alex'))

    #开始
    p1.start()
    c1.start()
    print('主程序')
    
##### 总结：
生产者消费者模型总结：

1、生产者消费者模型什么时候用？

　　程序中有两类角色：一类负责生产数据（生产者）；一类负责处理数据（消费者）。

2、怎么叫生产者消费者模型？

　　引入队列解决生产者和消费者之间的耦合，这个并不依赖进程，这实际是介绍了一种编程方式。

　　如果使用了Queue，说明生产者、消费者、queue都在一台机器，这属于集中式架构，严重影响性能和稳定性。

　　基于网络通信的消息队列：Rabbitmq。

3、生产者消费者模型好处？

　　引入生产者消费者模型为了解决的问题是：

　　（1）平衡生产者与消费者之间的工作能力，从而提高程序整体处理数据的速度。

　　（2）生产者消费者模型实现类程序的解耦合。

4、如何实现生产者消费者模型

　　如何实现：生产者<--->队列<--->消费者

　　此时的问题是主进程永远不会结束，原因是：生产者p在生产完后就结束了，但是消费者c在取空了q之后，则一直处于死循环中且卡在q.get()这一步。

　　解决方法：让生产者在生产完毕后，往队列中再发一个结束信号，这样消费者在接收到结束信号后就可以break出死循环。


   -2 改进方案一：生产者在生产完毕后发送结束信号None
   
    from multiprocessing import Process, Queue
    import time
    
    def producer(q):
        for i in range(10):
            res = '包子%s' % i
            time.sleep(0.5)   # 模拟生产时间
            print('生产者生产了%s' % res)
    
            q.put(res)  # 放入队列中
    
    
    def consumer(q):
        while True:    # 一直从队列取一旦取空了，会加一把锁，程序卡在这里
            res = q.get()   # 取队列中数据
            if res is None:break
            time.sleep(1)    # 模拟消费时间
            print('消费者消费了%s' % res)
    
    if __name__ == '__main__':
        # 容器
        q = Queue()
        # 生产者
        p1 = Process(target=producer, args=(q, ))
        # 消费者
        c1 = Process(target=consumer, args=(q, ))
    
        p1.start()
        c1.start()
    
        p1.join()   # 保证生产者都执行完，主进程才执行完
        q.put(None)  # 往队列里放入None,给消费者判断
        print("主进程")    

   -有几个消费者就需要发送几次结束信号
   
    from multiprocessing import Process, Queue
    import time
    
    def producer(q):
        for i in range(10):
            res = '包子%s' % i
            time.sleep(0.5)   # 模拟生产时间
            print('生产者生产了%s' % res)
    
            q.put(res)  # 放入队列中
    
            # q.put(None)  # 这种方式会将消费者提前停止
    
    
    def consumer(q):
        while True:    # 一直从队列取一旦取空了，会加一把锁，程序卡在这里
            res = q.get()   # 取队列中数据
            if res is None:break
            time.sleep(1)    # 模拟消费时间
            print('消费者消费了%s' % res)
    
    if __name__ == '__main__':
        # 容器
        q = Queue()
        # 生产者
        p1 = Process(target=producer, args=(q, ))
        p2 = Process(target=producer, args=(q,))
        p3 = Process(target=producer, args=(q,))
        # 消费者
        c1 = Process(target=consumer, args=(q, ))
        c2 = Process(target=consumer, args=(q,))
    
        p1.start()
        p2.start()
        p3.start()
        c1.start()
        c2.start()
    
        p1.join()   # 保证生产者都执行完，主进程才执行完
        p2.join()
        p3.join()
        # 跟在正常信号后面，必须保证所有的生产者都生产结束
        q.put(None)  # 往队列里放入None,给消费者判断
        q.put(None)  # 有几个消费者就需要几个结束信号
        print("主进程")
    
   -3 JoinableQueue(推荐)解决生产者消费模型
   
    JoinableQueue([maxsize])：这就像是一个Queue对象，但队列允许项目的使用者通知生成者项目已经被成功处理。通知进程是使用共享的信号和条件变量来实现的。
    
    参数介绍：maxsize是队列中允许最大项数，省略则无大小限制。
    
    方法介绍： 
    JoinableQueue的实例p除了与Queue对象相同的方法之外还具有：
    q.task_done()：使用者使用此方法发出信号，表示q.get()的返回项目已经被处理。如果调用此方法的次数大于从队列中删除项目的数量，将引发ValueError异常
    q.join():生产者调用此方法进行阻塞，直到队列中所有的项目均被处理。阻塞将持续到队列中的每个项目均调用q.task_done（）方法为止

    # JoinableQueue的用法和queue类似，只是这个queue是可以被join的
    from multiprocessing import Process, JoinableQueue
    import time
    
    def producer(q):
        for i in range(2):
            res = '包子%s' % i
            time.sleep(0.5)   # 模拟生产时间
            print('生产者生产了%s' % res)
    
            q.put(res)  # 放入队列中
        q.join()  # 生产者生产完等队列把数据都取完
    
    
    def consumer(q):
        while True:
            res = q.get()   # 取队列中数据
            if res is None:break
            time.sleep(1)    # 模拟消费时间
            print('消费者消费了%s' % res)
            q.task_done()   # 提供的接口，消费者告诉生产者取走了一个数据
    
    
    if __name__ == '__main__':
        # 容器
        q = JoinableQueue()
        q.join()    # 等队列执行完（等队列取完）
    
        # 生产者
        p1 = Process(target=producer, args=(q,))
        p2 = Process(target=producer, args=(q,))
        p3 = Process(target=producer, args=(q,))
        # 消费者
        c1 = Process(target=consumer, args=(q,))
        c2 = Process(target=consumer, args=(q,))
        # 主进程执行完之后，守护进程也终止，因此把消费者设置为守护进程
        c1.daemon=True
        c2.daemon=True
    
        p1.start()
        p2.start()
        p3.start()
        c1.start()
        c2.start()
    
        p1.join()
        p2.join()
        p3.join()
    
        print("主进程")  
        
        
### 一.什么叫线程
    　
    　　在传统操作系统中，每个进程有一个地址空间，而且默认就有一个控制线程
    
    　　线程顾名思义，就是一条流水线工作的过程（流水线的工作需要电源，电源就相当于cpu），而一条流水线必须属于一个车间，一个车间的工作过程是一个进程，车间负责把资源整合到一起，是一个资源单位，而一个车间内至少有一条流水线。
    
    　　所以，进程只是用来把资源集中到一起（进程只是一个资源单位，或者说资源集合），而线程才是cpu上的执行单位。
    
    　　多线程（即多个控制线程）的概念是，在一个进程中存在多个线程，多个线程共享该进程的地址空间，相当于一个车间内有多条流水线，都共用一个车间的资源。例如，北京地铁与上海地铁是不同的进程，而北京地铁里的13号线是一个线程，北京地铁所有的线路共享北京地铁所有的资源，比如所有的乘客可以被所有线路拉。
### 二、线程的创建开销小

    1、创建进程的开销要远大于线程？
    　　如果我们的软件是一个工厂，该工厂有多条流水线，流水线工作需要电源，电源只有一个即cpu（单核cpu）。一个车间就是一个进程，一个车间至少一条流水线（一个进程至少一个线程）；创建一个进程，就是创建一个车间（申请空间，在该空间内建至少一条流水线），而建线程，就只是在一个车间内造一条流水线，无需申请空间，所以创建开销小。
    
    2、进程之间是竞争关系，线程之间是协作关系？
    　　车间直接是竞争/抢电源的关系，竞争（不同的进程直接是竞争关系，是不同的程序员写的程序运行的，迅雷抢占其他进程的网速，360把其他进程当做病毒干死）
    　　一个车间的不同流水线式协同工作的关系（同一个进程的线程之间是合作关系，是同一个程序写的程序内开启动，迅雷内的线程是合作关系，不会自己干自己）


### 三、线程与进程的区别

    　　1、每启动一个进程，进程内都至少有一个线程。
    
    　　2、进程本身只是一个资源单位，并不能真正执行，进程内开的线程才是真正的运行单位。
    
    　　3、一个进程内可以启动多个线程，同一进程内线程间共享资源。
    
    　　4、启线程的开销远远小于开进程。
    
    　　5、线程可以相当程度控制相同进程下的线程，进程只能控制其子进程。
    
    　　6、对主线程的更改（取消、优先级更改等）可能会进程的其他线程的行为；对父进程的修改则不会影响子进程。

### 四、为何要用多线程

    　　多线程指的是，在一个进程中开启多个线程，简单的讲：如果多个任务共用一块地址空间，那么必须在一个进程内开启多个线程。详细的讲分为4点：
    
    　1. 同一个进程内的多个线程共享该进程内的地址资源

      2. 线程比进程更轻量级，线程比进程更容易创建可撤销，在许多操作系统中，创建一个线程比创建一个进程要快10-100倍，在有大量线程需要动态和快速修改时，这一特性很有用

      3. 若多个线程都是cpu密集型的，那么并不能获得性能上的增强，但是如果存在大量的计算和大量的I/O处理，拥有多个线程允许这些活动彼此重叠运行，从而会加快程序执行的速度。

      4. 在多cpu系统中，为了最大限度的利用多核，可以开启多个线程，比开进程开销要小的多。（这一条并不适用于python）
  
### 五、开启线程的方式

    import time, random
    # from multiprocessing import Process
    from threading import Thread
    
    
    def piao(name):
        print('%s piaoing' % name)
        time.sleep(random.randrange(1, 5))
        print('%s piao end' % name)
    
    if __name__ == '__main__':
        t1 = Thread(target=piao, args=('egon', ))
        t1.start()  # 主线程向操作系统发信号，又开了一个线程
        print("主线程")   # 执行角度看是主线程，从资源角度看是主进程
        # 这个程序总体是一个进程、两个线程
    """
    egon piaoing
    主进程
    egon piao end
    """
    
### 六、在一个进程下开启线程与在一个进程下开启多个子进程的区别

   -1 对比可知这两段代码可知，线程开销远小于进程，因为进程需要申请内存空间。
   
    import time
    from multiprocessing import Process
    from threading import Thread
    
    
    def piao(name):
        print('%s piaoing' % name)
        time.sleep(2)
        print('%s piao end' % name)
    
    if __name__ == '__main__':
        # p1 = Process(target=piao, args=('进程', ))
        # p1.start()
        """
        主线程
        进程 piaoing
        进程 piao end
        """
    
    
        t1 = Thread(target=piao, args=('线程', ))
        t1.start()
        """
        线程 piaoing
        主线程
        线程 piao end
        """
        print("主线程")
    
    
   -2、同一进程内的多个线程共享进程地址空间；但是进程间是隔离的，子进程变量修改不影响主进程
   
    举例案例：
    from threading import Thread
    from multiprocessing import Process
    
    n = 100
    def task():
        global n
        n = 0
    
    if __name__ == '__main__':
        """进程验证：
        p1 = Process(target=task,)
        p1.start()   # 会把子进程的n改为了0，看是否影响主进程
        p1.join()
        print("主进程", n)   # 主进程 100
        # 由此可见进程间是隔离的，子进程变量修改不影响主进程
        """
    
        """线程验证"""
        t1 = Thread(target=task, )
        t1.start()
        t1.join()
        print("主线程", n)   # 主线程 0
        
   -3 pid观察
   
    from threading import Thread
    from multiprocessing import Process, current_process  # current_process查看进程ID号
    import os   # os.getpid()也可以查看进程ID
    
    n = 100
    def task():
        # print(current_process().pid)
        print('子进程PID:%s   父进程的PID：%s' % (os.getpid(), os.getppid()))
    
    if __name__ == '__main__':
        p1 = Process(target=task,)
        p1.start()
    
        # print("主线程", current_process().pid)
        print("主线程", os.getpid())
    """
    主线程 6455
    子进程PID:6456   父进程的PID：6455
    """ 
    
### 七、线程对象的属性和方法

   -1、Thread实例对象的方法
   
    isAlive(): 返回线程是否活动的。
    getName(): 返回线程名。
    setName(): 设置线程名。
    
   -2、threading模块提供的一些方法
   
    threading.currentThread(): 返回当前的线程变量。
    threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
    threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
  
   -3、属性和方法的应用与验证
    -1 需要注意的是线程没有子线程的概念，线程都是属于进程的
    -2 join方法使得主线程等子线程运行完执行
    
### 八、守护线程

        一个进程内，如果不开线程，默认就是一个主线程，主线程代码运行完毕，进程被销毁。
    
    　　一个进程内，开多个线程的情况下，主线程在代码运行完毕后，还要等其他线程工作完才死掉，进程销毁。
    
    　　守护线程守护主线程，等到主线程死了才会被销毁。在有其他线程的情况下，主线程代码运行完后，等其他非守护线程结束，守护线程才会死掉。
    
    　　无论是进程还是线程，都遵循：守护xxx会等待主xxx运行完毕后被销毁。
    
    　　需要强调的是：运行完毕并非终止运行。运行完毕的真正含义：
    
    　　1、对主进程来说，运行完毕指的是主进程代码运行完毕。
    
    　　2、对主线程来说，运行完毕指的是主线程所在的进程内所有非守护线程统统运行完毕，主线程才能运行完毕。
    
    　　详细解释
    
    　　1、主进程在其代码结束后就已经算运行完毕了（守护进程在此时就被回收）,然后主进程会一直等非守护的子进程都运行完毕后回收子进程的资源(否则会产生僵尸进程)，才会结束
    
    　　2、主线程在其他非守护线程运行完毕后才算运行完毕（守护线程在此时就被回收）。因为主线程的结束意味着进程的结束，进程整体的资源都将被回收，而进程必须保证非守护线程都运行完毕后才能结束。
   
    案例一:
    from threading import Thread
    import time
    
    def sayhi(name):
        time.sleep(2)
        print("%s say hello" % name)
    
    if __name__ == '__main__':
        t = Thread(target=sayhi, args=('egon',))
    
        # 守护线程必须在t.start()前设置
        # 守护线程设置方式一：
        t.daemon=True
        # 守护线程设置方式二：
        # t.setDaemon(True)
    
        t.start()   # 立马创建子线程，但需要等待两秒，因此程序会先执行下面的代码
    
        print("主线程")
        print(t.is_alive())
    # 这一行代码执行完后，主线程执行完毕，由于主线程之外，只有一个守护线程，主线程不需要等守护线程执行结束，因此主线程和守护进程终止，进程结束。
    """
    主线程
    True
    """
    
    
### 九、互斥锁与join的区别
    
   -1 不加锁：并发执行，速度快，数据不安全
   
    案例：
        from threading import current_thread,Thread,Lock
        import os,time
        def task():
            global n
            print('%s is running' %current_thread().getName())
            temp=n
            time.sleep(0.5)
            n=temp-1
        
        
        if __name__ == '__main__':
            n=100
            lock=Lock()
            threads=[]
            start_time=time.time()
            for i in range(100):
                t=Thread(target=task)
                threads.append(t)
                t.start()
            for t in threads:
                t.join()
        
            stop_time=time.time()
            print('主:%s n:%s' %(stop_time-start_time,n))
        
        '''
        Thread-1 is running
        Thread-2 is running
        ......
        Thread-100 is running
        主:0.5216062068939209 n:99
        # 速度快，但是数据出错
        '''
   
   -2 加锁:未加锁部分并发执行,加锁部分串行执行,速度慢,数据安全
    
    案例：
    from threading import current_thread,Thread,Lock
    import os,time
    def task():
        #未加锁的代码并发运行
        time.sleep(3)
        print('%s start to run' %current_thread().getName())
        global n
        #加锁的代码串行运行
        lock.acquire()
        temp=n
        time.sleep(0.5)
        n=temp-1
        lock.release()
    
    if __name__ == '__main__':
        n=100
        lock=Lock()
        threads=[]
        start_time=time.time()
        for i in range(100):
            t=Thread(target=task)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        stop_time=time.time()
        print('主:%s n:%s' %(stop_time-start_time,n))
    
    '''
    Thread-1 is running
    Thread-2 is running
    ......
    Thread-100 is running
    主:53.294203758239746 n:0
    利用锁实现串行，保障数据安全，运行时间还可以接受
    '''
    
   -3 利用join方式将全部代码串行执行，数据安全但效率很低
   
        -加锁会将运行变成串行，同样适用join也可以得到串行的效果，数据也是安全的，
        -但是start后立即join，任务内的所有代码都是串行执行的，而加锁只是加锁的部分（修改共享数据的部分）是串行的，
        -两者从保护数据安全方面来说是一样的，但是加锁的效率更高。
        
### 十、死锁现象与递归锁

　　-死锁： 是指两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，若无外力作用，它们都将无法推进下去。
   -此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程
   
   
   
### 十一、进程池与线程池

   ##### 1.介绍：
    concurrent.futures   模块提供了高度封装的异步调用接口
    ThreadPoolExecutor： 线程池，提供异步调用
    ProcessPoolExecutor: 进程池，提供异步调用
    Both implement the same interface, which is defined by the abstract Executor class.

    基本方法：

    1、submit(fn, *args, **kwargs)
    异步提交任务
    
    2、map(func, *iterables, timeout=None, chunksize=1) 
    取代for循环submit的操作
    
    3、shutdown(wait=True) 
    相当于进程池的pool.close()+pool.join()操作
    wait=True，等待池内所有任务执行完毕回收完资源后才继续
    wait=False，立即返回，并不会等待池内的任务执行完毕
    但不管wait参数为何值，整个程序都会等到所有任务执行完毕
    submit和map必须在shutdown之前
    
    4、result(timeout=None)
    取得结果
    
    5、add_done_callback(fn)
    回调函数
    
   ####2.进程池
   
    from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
    import os, time, random
     
    def task(name):
        print("name: %s pid: %s run" % (name, os.getpid()))
        time.sleep(random.randint(1, 3))
    
    
    if __name__ == '__main__':
        pool = ProcessPoolExecutor(4)  # 指定进程池大小，最大进程数，如果不指定默认是CPU核数
    
        for i in range(10):
            """从始至终四个进程解决这10个任务，谁没事了接新任务"""
            pool.submit(task, 'ProcessPool-%s' % i)  # 提交任务的方式————异步调用：提交完任务，不用在原地等任务执行拿到结果。
    
        print("主进程")
        
        
   #### 3.线程池
   
    from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
    import os, time, random
    
    
    def task(name):
        print("name: %s pid: %s run" % (name, os.getpid()))
        time.sleep(random.randint(1, 3))
    
    
    if __name__ == '__main__':
        pool = ThreadPoolExecutor(4)
    
        for i in range(10):
            """从始至终四个进程解决这10个任务，谁没事了接新任务"""
            pool.submit(task, 'ThreadPool-%s' % i)  # 提交任务的方式————异步调用：提交完任务，不用在原地等任务执行拿到结果。
    
        pool.shutdown(wait=True)  # 把提交任务入口关闭，默认参数wait=True；同时还进行了pool.join()操作，等任务提交结束，再结束主进程
    
        print("主进程")
