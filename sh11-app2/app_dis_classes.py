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

# 获取所有id属性值为com.android.settings:id/title的文本内容
# ids = driver.find_elements_by_id("com.android.settings:id/title")  # 返回是列表
#
# print("id:", type(ids))
# print(ids)
# for i in ids:
#     print("text:", i.text)  # 取元素的text属性值

# 获取所有class属性值为 android.widget.TextView的文本内容
classes = driver.find_elements_by_class_name("android.widget.TextView") # 返回列表

for i in classes:
    print("text:", i.text)  # 取元素的text属性值

# 退出
time.sleep(2)
driver.quit()
