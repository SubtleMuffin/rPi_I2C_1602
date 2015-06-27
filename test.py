#!/user/bin/env python 
import smbus
import time
import sys
import LCD1602 as LCD
from datetime import datetime
from subprocess import *
import commands

ip = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
uptime = "uptime"


def get_cpu_temp():
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    return 'C:''{:.2f}'.format(float(cpu) / 1000)


def get_gpu_temp():
    tmp = commands.getoutput('vcgencmd measure_temp|awk -F= \'{print $2}\'').replace('\'C', '')
    gpu = float(tmp)
    return 'G:''{:.2f}'.format(gpu)


def get_time_now():
    return datetime.now().strftime('    %H:%M:%S\n   %Y-%m-%d')


def get_ip_info():
    return commands.getoutput('ifconfig wlan0|grep inet|awk -Faddr: \'{print $2}\'|awk \'{print $1}\'')


def get_mem_info():
    total = commands.getoutput('free -m|grep Mem:|awk \'{print $2}\'')
    free = commands.getoutput('free -m|grep cache:|awk \'{print $4}\'')
    return 'M:F' + free + '/T' + total + ' MiB'


def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output


if __name__ == '__main__':
    LCD.init_lcd()
    LCD.turn_light(0)


    # LCD.print_lcd(0,0,datetime.now().strftime('%b %d %H:%M:%S\n'))
    # LCD.print_lcd(1,1,'local time')
    # print('wait 5 seconds')
    # time.sleep(5)


    while True:
        # nowtime = datetime.now().strftime('%b %d %H:%M:%S')
        # mintime = time.strftime('%M',time.localtime(time.time()))
        # print('current time:'+nowtime)
        # LCD.print_lcd(0,0,nowtime)
        # if mintime == 59:
        # LCD.turn_light(1)
        # print('mintime:'+mintime)


        top = run_cmd(uptime)
        ipaddr = run_cmd(ip)

        LCD.print_lcd(0, 0, top[top.find(": ") + 2:].strip(','))
        LCD.print_lcd(0, 1, ipaddr[:ipaddr.find('\n')])

        time.sleep(2.5)

        LCD.clear_lcd()

        cpu_temp = get_cpu_temp()
        gpu_temp = get_gpu_temp()
        mem = get_mem_info()
        LCD.print_lcd(0, 0, cpu_temp)
        LCD.print_lcd(8, 0, gpu_temp)
        LCD.print_lcd(0, 1, mem)
        time.sleep(2.5)
        LCD.clear_lcd()