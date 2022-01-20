from scapy.all import *
import sys
import random
import datetime
import argparse
import threading
import ipaddress

alives = []
dead   = []

def pingSingle(host):
    rand_ip_id = random.randint(1,65535)
    rand_icmp_id = random.randint(1,65535)
    rand_icmp_seq = random.randint(1,65535)

    packet = IP(dst=host, ttl=128, id=rand_ip_id)/ICMP(id=rand_icmp_id, seq=rand_icmp_seq)
    response = sr1(packet, timeout=1, verbose=0)
    if response:
        alives.append(host)
        # print("[+] {} is alive.".format(host))
    else:
        dead.append(host)
        # print("[-] {} is not alive.".format(host))

def pingScan(hosts):
    ip_list = ipaddress.ip_network(hosts) # 生成 ip 地址
    thread_list = []
    for ip in ip_list:
        t = threading.Thread(target=pingSingle, args=(str(ip),))
        thread_list.append(t)
        t.start()
        # pingSingle(str(ip))

    for threadlist in thread_list:
        threadlist.join()

def main():
    banner = r'''
           .__
______ |__| ____    ____
\____ \|  |/    \  / ___\
|  |_> >  |   |  \/ /_/  >
|   __/|__|___|  /\___  /
|__|           \//_____/  v1.0
    '''
    print(banner)
    parser = argparse.ArgumentParser()
    parser.add_argument("-H","--Host",type=str, help="Enter target IP ex: 192.168.91.138 or 192.168.91.0/24.")
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    host = args.Host
    start_time = datetime.datetime.now()
    print(start_time)
    print("Scaning...")
    pingScan(host) # def pingScan()
    for i in alives:
        print("[+] {} is alive.".format(i))
    print("[*] All scans completed!")
    print()
    end_time = datetime.datetime.now()
    print(end_time)
    print("总用时: ",end_time-start_time)


if __name__ == "__main__":
    main()