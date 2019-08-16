# -*- coding:utf-8 -*-
import time, socket, struct
"""
1.关于用程序来开机，是怎么做到的呢？这就是 WOL 技术 Wake-On-Lan, 利用计算机在关机或休眠状态时，网卡及主板部分仍然有微弱的供电，
当然要保持电源是插上的，而且是有线连接。所以即使在关机情况下，网卡还是有一定运作能力的，可以监听计算机外部的网上广播信息，
当发现特定格式的信息后就会执行开机
2. mac地址查找：cmd->ipconfig/all -> 选择以太网适配器 本地连接： -> 物理地址
"""

def wake_up(mac='B0-83-FE-A0-42-E9'):
    MAC = mac
    BROADCAST = "172.18.130.88"
    if len(MAC) != 17:
        raise ValueError("MAC address should be set as form 'XX-XX-XX-XX-XX-XX'")
    mac_address = MAC.replace("-", '')
    data = ''.join(['FFFFFFFFFFFF', mac_address * 20])  # 构造原始数据格式
    send_data = b''

    # 把原始数据转换为16进制字节数组，
    for i in range(0, len(data), 2):
        send_data = b''.join([send_data, struct.pack('B', int(data[i: i + 2], 16))])
    print(send_data)

    # 通过socket广播出去，为避免失败，间隔广播三次
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(send_data, (BROADCAST, 7))
        time.sleep(1)
        sock.sendto(send_data, (BROADCAST, 7))
        time.sleep(1)
        sock.sendto(send_data, (BROADCAST, 7))

        print("Done")
    except Exception as e:

        print(e)
