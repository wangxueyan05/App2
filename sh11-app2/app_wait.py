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
# 声明手机驱动对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# # 通过显示等待的方式 点击设置列表页面 更多按钮
# more_xpath = "//*[contains(@text, '更多')]"
# # 找到元素返回元素定位对象
# WebDriverWait(driver, 5, 1).until(lambda x: x.find_element_by_xpath(more_xpath)).click()


"""异常"""
# 通过显示等待的方式 点击设置列表页面 更多按钮
more_xpath = "//*[contains(@text, '更多1')]"

try:
    # 打印开始时间
    print("开始时间:", time.strftime("%H:%M:%S", time.localtime()))
    # 找到元素返回元素定位对象
    WebDriverWait(driver, 5, 1).until(lambda x: x.find_element_by_xpath(more_xpath)).click()
except:
    # 结束时间
    print("结束时间:", time.strftime("%H:%M:%S", time.localtime()))

# 退出
time.sleep(2)
driver.quit()
