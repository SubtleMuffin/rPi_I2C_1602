# rPi_I2C_1602
This is a simple system monitor of Raspberry Pi via 1602 LCD on I2c protocol.

##C++ Version

###Installation(Primarily build from source)

To use it, you have to install wiringPi libraries and enable I2C specifications via /etc/modules in Raspberian system(not in Ubuntu mate).

####wiringPi-Installation
To use it, you have to install wiringPi libraries.
```Shell
sudo apt-get install build-essential
sudo apt-get install git-core
git clone git://git.drogon.net/wiringPi
cd wiringPi
./build
```
To test wiringPi's installation
```Shell
gpio -v
gpio readall
```

####Load I2C devices
```Shell
sudo nano /etc/modules
```
then add
```Shell
i2c-bcm2708
i2c-dev
```
####Build from source
```shell
git clone https://github.com/zhengnanlee/rPi_I2C_1602.git
g++ -o test test.cpp -L/u9sr/local/lib -lwiringPi -lwiringPiDev -lpthread -lm
```
###Execute
```shell
sudo ./test
```

##Python Version

###Install dependencies

```shell
sudo apt-get install python-dev python-setuptools
sudo easy_install -U distribute
sudo apt-get install python-pip i2c-tools python-smbus
sudo pip install rpi.gpio
```

###Execute
```shell
sudo python test.py
```

##Detect I2C Devices

###If you are using Raspberry Pi 1 A/B/B+

```shell
sudo i2cdetect -y 0
```

###If you are using Raspberry Pi 2 B

```shell
sudo i2cdetect -y 1
```

###Results
The results may be

```shell
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- 27 -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```



