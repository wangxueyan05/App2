from appium import webdriver
import os

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

# apk绝对路径
# cal_path = "/Users/mac/Documents/Worker/sh11-app2/com.example.corel.calc_2.1.1023_11.apk"
cal_path = os.getcwd() + os.sep + "com.example.corel.calc_2.1.1023_11.apk"

# 安装
# driver.install_app(cal_path)

# 卸载计算器-自己安装的 com.example.corel.calc
# driver.remove_app("com.example.corel.calc")

# 获取手机计算器-自己安装 -默认返回False
# print("计算器:", driver.is_app_installed("com.example.corel.calc"))

# 获取手机设置 -默认返回True
# print("设置:", driver.is_app_installed("com.android.settings"))

"""
练习：
	判断手机是否安装计算器，如果安装执行卸载操作，如果未安装执行安装操作
"""
if driver.is_app_installed("com.example.corel.calc"):
    driver.remove_app("com.example.corel.calc")
else:
    driver.install_app(cal_path)

# 退出
driver.quit()
