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

# 点击搜索按钮 -id
search_btn_xpath = "//*[contains(@resource-id,'com.android.settings:id/search')]"
driver.find_element_by_xpath(search_btn_xpath).click()

# 点击搜索页面返回按钮 -class
search_re_btn_xpath = "//*[contains(@class, 'android.widget.ImageButton')]"
driver.find_element_by_xpath(search_re_btn_xpath).click()

# 通过xpath点击更多按钮-text
more_xpath = "//*[contains(@text,'更多')]"
driver.find_element_by_xpath(more_xpath).click()


# 退出
time.sleep(2)
driver.quit()
