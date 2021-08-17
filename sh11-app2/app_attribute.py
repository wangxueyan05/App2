from appium import webdriver
import time

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
# 重置手机键盘
desired_caps['resetKeyboard'] = True
# 使用unicode
desired_caps['unicodeKeyboard'] = True
# 声明手机驱动对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 定位搜索按钮 -取content-desc属性值
con = driver.find_element_by_id("com.android.settings:id/search").get_attribute("name")
# 打印属性值
print("搜索按钮content-desc属性值:", con)

# 定位WLAN
wlan = driver.find_element_by_xpath("//*[contains(@text,'WL')]")

# 打印text
print("text属性:", wlan.get_attribute("text"))

# 打印resource-id
print("resource-id属性值:", wlan.get_attribute("resourceId"))

# class
print("class属性值:", wlan.get_attribute("className"))

# 退出
time.sleep(2)
driver.quit()
