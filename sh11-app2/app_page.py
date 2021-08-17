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

# 打印当前屏幕内元素结构 返回值xml字符串
# print(driver.page_source)

# with open("./page.xml", "w", encoding="utf-8") as f:
#     f.write(driver.page_source)

# 判断设置页面是否打开
if "更多" in driver.page_source:
    print("设置页面打开成功")
# 退出
# driver.quit()
