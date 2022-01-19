from scapy.all import *
import datetime
import argparse
import ipaddress
import threading

ip_mac_list = []

def arpSingle(host,interface):
    packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=host, hwdst="ff:ff:ff:ff:ff:ff")
    ans,unans = srp(packet, timeout=1, iface=interface,verbose=0)
    #print(ans[0])
    for send,rcv in ans:
        ip_mac = rcv.sprintf("%ARP.psrc% --- %ARP.hwsrc%")
        #print(ip_mac)
        ip_mac_list.append(ip_mac)

def arpScan(hosts,interface):
    ip_list = ipaddress.ip_network(hosts) # create ip
    thread_list =[]
    for ip in ip_list:
        t = threading.Thread(target=arpSingle, args=(str(ip),interface)) # target=arpSinglie()
        thread_list.append(t)
        t.start()

    for threadlist in thread_list:
        threadlist.join()

def main():
    banner = r'''
   _____                _________                     
  /  _  \_____________ /   _____/ ____ _____    ____  
 /  /_\  \_  __ \____ \\_____  \_/ ___\\__  \  /    \ 
/    |    \  | \/  |_> >        \  \___ / __ \|   |  \
\____|__  /__|  |   __/_______  /\___  >____  /___|  /
        \/      |__|          \/     \/     \/     \/  .
    '''
    print(banner)
    parser = argparse.ArgumentParser()
    parser.add_argument("-H","--Host",type=str,help="Enter target IP, ex: 192.168.91.1 or 192.168.91.0/24.")
    parser.add_argument("-i","--iface",type=str,help="Select your network card, ex: ens33")
    args = parser.parse_args()
    hosts = args.Host
    iface = args.iface
    #print(hosts)
    start_time = datetime.datetime.now()
    print("Scaning...\n")
    arpScan(hosts,iface) # def arpScan()
    for i in ip_mac_list:
        print("[+] IP&MAC: {} ".format(i))
    print("[*] All scans completed!")
    print()
    end_time = datetime.datetime.now()
    print(end_time)
    print("总用时: ",end_time-start_time)


if __name__ == "__main__":
    main()