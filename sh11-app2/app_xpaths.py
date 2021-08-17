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
ids_xpath = "//*[contains(@resource-id,'com.android.settings:id/title')]"
value1 = driver.find_elements_by_xpath(ids_xpath)
for i in value1:
    print("ids:", i.text)

# 获取所有class属性值为 android.widget.TextView的文本内容
classes_xpath = "//*[contains(@class,'android.widget.TextView')]"
value2 = driver.find_elements_by_xpath(classes_xpath)
for i in value2:
    print("classes:", i.text)

# 文本为 示 的两个元素
texts_xpath = "//*[contains(@text,'示')]"
value3 = driver.find_elements_by_xpath(texts_xpath)
for i in value3:
    print("texts:", i.text)

# 退出
time.sleep(2)
driver.quit()
