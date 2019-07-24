"""
Hash一般翻译为"散列"，或音译为"哈希"。将任意长度的输入（也叫预映射，pre-image）通过散列算法，变换为固定长度的输出，这个输出就是散列值。这种转换是一种压缩映射，散列值的空间通常远小于输入的空间。不同输入可能会散列为相同输出，因此不可能从散列值来唯一确定输入值。

　　Hash定义：一种将任意长度的消息压缩到某一固定长度的消息摘要的函数。
　　Hash功能：主要用于信息安全领域中加密算法，他把一些不同长度的信息转化成杂乱的128位的编码里,叫做HASH值.

　　hash就是找到一种数据内容和数据存放地址之间的映射关系
"""
#md5加密是不可反解的
import hashlib
#实例化对象
obj=hashlib.md5()      #先创建一个md5的对象
#写入要加密的字节
obj.update("admin".encode("utf-8"))   #对谁加密就把谁道前面，python3中必须是字节,所以必须用.encode()
#获取密文
secret=obj.hexdigest()
print(secret)
##############################################################
  
import hashlib
obj=hashlib.md5(b'12334')                #实例化md5的时候可以给传个参数，这叫加盐
obj.update("admin".encode("utf-8"))      #是再加密的时候传入自己的一块字节，
secret=obj.hexdigest()
print(secret)
##############################################################
  
#因为用户密码已经被加密过了，而且是加盐的，所以再用户验证的时候用字符串或者直接的加密的的字节都不能正确判断，只能用加盐的字节所判断
  
import hashlib
SALT = b'2erer3asdfwerxdf34sdfsdfs90'
def md5(pwd):
    # 实例化对象
    obj = hashlib.md5(SALT)
    # 写入要加密的字节
    obj.update(pwd.encode('utf-8'))
    # 获取密文
    return obj.hexdigest()
  
user = input("请输入用户名:")
pwd = input("请输入密码:")
if user == 'oldboy' and md5(pwd) == 'c5395258d82599e5f1bec3be1e4dea4a':
    print('登录成功')
else:
    print('登录失败')
