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

# 手机文件路径/sdcard/hello.txt
# 拉取文件 返回base64编码数据
res_data = driver.pull_file("/sdcard/hello.txt")

# 打印原生数据
print("原生数据:", res_data)
# 打印解码数据
print("解码数据:", str(base64.b64decode(res_data), "utf-8"))

# 退出
driver.quit()
