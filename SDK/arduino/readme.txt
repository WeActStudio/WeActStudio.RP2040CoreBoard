1.Arduino IDE安装
      打开Arduino IDE-->工具-->开发板管理器-->arduino mbed os rp2040 boards，点击安装
      中间会提示安装驱动，勾选信任，点击安装
      安装好以后在开发板管理器的arduino mbed os rp2040 boards下选择aspberry Pi Pico
注：下载地址：https://www.arduino.cn/thread-5838-1-1.html
                        https://github.com/arduino/arduino-ide

2.上传arduino (相当于刷入arduino固件)
     a.按住BOOTSEL按钮，将RP2040插入电脑；
     b.将Arduino IDE --> 文件 --> 示例 --> Basics --> Blink 上传到rp2040
     c.选择Arduino IDE--->工具-->端口-->串行端口 的相应串口
注：刷入一次即可

3.它就是一块arduino板了。
特殊引脚定义 C:\Users\用户名\AppData\Local\Arduino15\packages\arduino\hardware\mbed_rp2040\2.6.1\variants\RASPBERRY_PI_PICO\pins_arduino.h  
注：版本不同，路径稍微有点差异，一层一层找，不要直接复制