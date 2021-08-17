from appium import webdriver
import os, base64, time

from selenium.webdriver.support.wait import WebDriverWait

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

# 点击搜索按钮 -id com.android.settings:id/search
driver.find_element_by_id("com.android.settings:id/search").click()

# 定位输入框输入内容 -id android:id/search_src_text
search = driver.find_element_by_id("android:id/search_src_text")

# 输入英文符号数据 123hg！#
search.send_keys("123hg!#")

# 清空输入框操作
search.clear()

# 输入中文 中国
search.send_keys("中国")

# 退出
time.sleep(2)
driver.quit()
