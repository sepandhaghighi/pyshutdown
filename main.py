import datetime
import time
import subprocess as sub
import sys

flag_dict={"-r":"Restart","-h":"Hibernate","-s":"Shutdown"}
def cancel():
    c_input=input("Press Ctrl+C to cancel process")
    sub.Popen("shutdown -a",shell=True)
def get_method():
    flag=""
    get_method=input("Please Enter Method , Shutdown[1] , Hibernate[2] , Restart[3]")
    if get_method=="2":
        flag="-h"
    elif get_method=="3":
        flag="-r"
    else:
        flag="-s"
    return flag
def print_time(sleep_list,method):
    print("Your Computer Will Be ",flag_dict[method],"In ",str(sleep_list[0]),"Hour and",str(sleep_list[1]),"Minute")
def duration():
    try:
        get_hour=int(input("Please Enter Hour :"))
    except ValueError:
        get_hour=0
    try:
        get_minute=int(input("Please Enter Minute :"))
    except ValueError:
        get_minute=0
    sleep_time=get_hour*3600+get_minute*60
    flag=get_method()
    print_time([get_hour,get_minute],flag)
    if flag=="-h":
        time.sleep(float(sleep_time))
        sub.Popen("shutdown -h -f",shell=True)
        sys.exit()
    else:
        sub.Popen("shutdown "+flag+" -f -t "+str(sleep_time),shell=True)
    cancel()

def instantly():
    flag=get_method()
    inp=input('Are you sure?[y]')
    if inp.upper()=="Y":
        sub.Popen("shutdown "+flag+" -f",shell=True)
    else:
        sys.exit()    
        
        
def sleep_time_convert(get_hour,get_minute):
    date_time=datetime.datetime.now()
    now=str(date_time.time()).split(":")
    sleep_hour=get_hour-int(now[0])
    if sleep_hour<0:
        sleep_hour=sleep_hour+24
    sleep_minute=get_minute-int(now[1])
    if sleep_minute<0:
        sleep_minute=sleep_minute+60
        sleep_hour=sleep_hour-1
    sleep_time=sleep_hour*3600+sleep_minute*60
    return [sleep_time,sleep_hour,sleep_minute]

def localtime():
    try:
        get_hour=int(input("Please Enter Hour :"))
    except ValueError:
        get_hour=0
    try:
        get_minute=int(input("Please Enter Minute :"))
    except ValueError:
        get_minute=0
    sleep_time=sleep_time_convert(get_hour,get_minute)
    flag=get_method()
    print_time(sleep_time[1:],flag)
    if flag=="-h":
        time.sleep(sleep_time[0])
        sub.Popen("shutdown -h -f",shell=True)
    else:
        sub.Popen("shutdown "+flag+" -f -t "+str(sleep_time[0]),shell=True)
    
    cancel()


if __name__=="__main__":
    try:
        input1=int(input("Duration[1] or LocalTime[2] or Instantly[3]"))
    except ValueError:
        input1=1
    except KeyboardInterrupt:
        print("pyshut terminated!!")
        sys.exit()
    try:
        if input1==1:
            duration()
        elif input1==2:
            localtime()
        else:
            instantly()
    except KeyboardInterrupt:
        print("pyshut terminated!!")
        sub.Popen("shutdown -a",shell=True)
        sys.exit()
    
    
