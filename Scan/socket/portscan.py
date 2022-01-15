'''
Author: gakki_yyds
Date: 2022-01-10 16:26:38
LastEditors: gakki_yyds
LastEditTime: 2022-01-11 14:41:49
Description: socket 端口扫描
FilePath: \端口扫描\portscan.py
'''
import socket
import argparse
import datetime
import threading

open = []
close = []

def port_scan(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    state = sock.connect_ex((host, port))
    if not state:
        # print("[+] {}:{} is open.".format(host,port))
        open.append(port)
    else:
        # print("[-] {}:{} is close.".format(host,port))
        close.append(port)
    sock.close()
   
def main():

    banner = r'''
    __________              __      _________                     
\______   \____________/  |_   /   _____/ ____ _____    ____  
 |     ___/  _ \_  __ \   __\  \_____  \_/ ___\\__  \  /    \ 
 |    |  (  <_> )  | \/|  |    /        \  \___ / __ \|   |  \
 |____|   \____/|__|   |__|   /_______  /\___  >____  /___|  /
                                      \/     \/     \/     \/ 
    '''
    print(banner)
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--host", type=str, default="127.0.0.1",help="Target ip/hostname ex: 127.0.0.1/default='127.0.0.1'")
    parser.add_argument("-p","--ports", type=str, default="1-1024" ,help="Target ports ex: 1-65535/default='1-1024'")
    parser.add_argument("-t","--thread", type=int, default=100, help="Number of threads ex: 100/default:100")
    args = parser.parse_args()
    host = args.host
    ports = args.ports

    if "-" in ports:
        ports = ports.split("-")
        port_start = int(ports[0])
        port_end = int(ports[1])

    thread_num = args.thread
    thread_list = []
    # print(thread_num)

    start_time = datetime.datetime.now()
    print(start_time)
    print("Scaning...")

    for i in range(thread_num+1): # thread_num 个线程
        for port in range(port_start, port_end+1): # 输入的要扫描的端口
            t = threading.Thread(target=port_scan,args=(host,port)) # def sock_port(host,port)
            thread_list.append(t)
            t.start()
    
    for threadlist in thread_list:
        threadlist.join()

    opend = list(set(open)) # set 集合去除重复内容再转为list
    closed = list(set(close))
    for i in opend:
        print("[+] {}:{} is open.".format(host,i))
    # print("\n")
    # for i in closed:
    #     print("[-] {} {} is close.".format(host,i))    
    print("[*] All scans completed!")
    end_time = datetime.datetime.now()
    print(end_time)
    print("总用时:",end_time - start_time)

if __name__ == '__main__':
    main()
