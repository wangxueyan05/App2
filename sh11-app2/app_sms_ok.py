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
desired_caps['appPackage'] = 'com.android.mms'
# app启动名
desired_caps['appActivity'] = '.ui.ConversationList'
# 重置手机键盘
desired_caps['resetKeyboard'] = True
# 使用unicode
desired_caps['unicodeKeyboard'] = True
# 声明手机驱动对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 点击新建按钮
driver.find_element_by_id("com.android.mms:id/action_compose_new").click()

# 输入手机号 13222222222
driver.find_element_by_id("com.android.mms:id/recipients_editor").send_keys("13222222222")


lis_text = ["hello", "12345", "中国"]
exp_data = []

for i in lis_text:
    # 输入发送内容 hello 12345 中国
    driver.find_element_by_id("com.android.mms:id/embedded_text_editor").send_keys(i)
    # 点击发送按钮
    driver.find_element_by_id("com.android.mms:id/send_button_sms").click()
    # 取已经发送数据 -定位一组方式
    values = driver.find_elements_by_id("com.android.mms:id/text_view") # 所有定位对象列表
    for n in values:
        exp_data.append(n.text)
    # 判断发送成功
    if i in exp_data:
        print("成功")

# 退出
time.sleep(2)
driver.quit()
