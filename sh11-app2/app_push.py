from appium import webdriver
import os, base64

desired_caps = {}
# 测试系统
desired_caps['platformName'] = 'Android'
# 被测试系统版本
desired_caps['platformVersion'] = '5.1'
# 设备名字 随便写 不能为空
desired_caps['deviceName'] = 'sanxing'
# app包名
desired_caps['appPackage'] = 'com.android.settings'
# app启动名
desired_caps['appActivity'] = '.Settings'
# 声明手机驱动对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 数据
data = "hello python"
# base64编码
b64_data = str(base64.b64encode(data.encode("utf-8")), "utf-8")
# 发送文件到手机/sdcard/hello.txt
# driver.push_file("/sdcard/hello.txt", b64_data)

# 仅指定路径 不指定文件名字
driver.push_file("/sdcard", b64_data)

# 退出
driver.quit()
