//
// Created by ZhengnanLee on 15/6/26.
//
#include <unistd.h>
#include <string>

#include "1602I2C.h"
#include "1602I2C.cpp"

using namespace std;

const int deviceID = 0x27; // 1602 address

// BLEN = false;

int main() {
  I2CLED led(deviceID);
  // wiringPiI2CWrite(fd, 0x00);
  
  string uptime = "uptime";
  string ipaddr =
      "ifconfig eth0|grep inet|awk -Faddr: \'{print $2}\'|awk \'{print $1}\'";
  // char *cpuuse = "top -n1 | awk '/Cpu\(s\):/ {print $2}'";
  
  string cputemp = "cat /sys/class/thermal/thermal_zone0/temp";
  string gputemp = "vcgencmd measure_temp|awk -F= \'{print $2}\'";
  
  
  string totalmem = "free -m|grep Mem:|awk \'{print $2}\'";
  string freemem = "free -m|grep cache:|awk \'{print $4}\'";
  

  while (true) {
    string load = led.cmd_system(uptime.c_str());
    load = load.substr(load.find(": ") + 2, load.size());
	string ip = led.cmd_system(ipaddr.c_str());
	ip = ip.substr(0, ip.find('\n'));
	// string cpu = led.cmd_system(cpuuse);
	led.print_screen(0, 0, load);
    led.print_screen(0, 1, ip);
	// led.print_screen(0, 1, cpu);
    delay(2500);
    led.clear_lcd();
	
	
	string cpu_temp = led.cmd_system(cputemp.c_str());
	cpu_temp = "C:" + cpu_temp.substr(0, 2) + "." + cpu_temp.substr(1, 1);
	// double temp = atof(cpu_temp.c_str()) / 1000;
	// char *cpu_temp_char;
	// sprintf(cpu_temp_char, "%2.2f", temp);
	
	string gpu_temp = led.cmd_system(gputemp.c_str());
	gpu_temp = "G:" + gpu_temp.substr(0, 4);
	
	string total_mem = led.cmd_system(totalmem.c_str());
	total_mem = total_mem.substr(0, total_mem.length()-1);
	string free_mem = led.cmd_system(freemem.c_str());
	free_mem = free_mem.substr(0, free_mem.length()-1);
	string mem_info = "M:F"+free_mem+"/T"+total_mem+" MiB";
	
	led.print_screen(0, 0, cpu_temp);
	led.print_screen(8, 0, gpu_temp);
	led.print_screen(0, 1, mem_info);
	delay(2500);
	led.clear_lcd();
	
  }
  return 0;
}