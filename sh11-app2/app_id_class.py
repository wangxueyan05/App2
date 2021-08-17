from appium import webdriver
import os, base64, time

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

# 设置页面点击搜索按钮-id com.android.settings:id/search
driver.find_element_by_id("com.android.settings:id/search").click()

# 搜索页面点击返回按钮-class android.widget.ImageButton
driver.find_element_by_class_name("android.widget.ImageButton").click()

# 退出
time.sleep(2)
driver.quit()
