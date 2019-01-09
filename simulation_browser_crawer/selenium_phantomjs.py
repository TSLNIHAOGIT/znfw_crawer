#导入webdriver
from selenium import webdriver
import time

#要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

#调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS(executable_path='phantomjs-2.1.1-macosx/bin/phantomjs')
driver.set_window_size(1366, 768)
driver.get("https://www.baidu.com/")

data=driver.find_element_by_id('kw')
print('data',data)

#获取页面名为wraper的id标签的文本内容
data = driver.find_element_by_id('wrapper').text

#打印数据内容
print(data)

print ('driver.title',driver.title)

#生成页面快照并保存
driver.save_screenshot("baidu.png")

# id="kw"是百度搜索输入框，输入字符串"长城"
driver.find_element_by_id('kw').send_keys(u'长城')

# id="su"是百度搜索按钮，click()是模拟点击
driver.find_element_by_id('su').click()

#获取新的页面快照
driver.save_screenshot("长城.png")

#打印网页渲染后的源代码
print(driver.page_source)

#获取当前页面Cookie
print(driver.get_cookies())

#ctrl+a全选输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
#ctrl+x剪切输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

#输入框重新输入内容
driver.find_element_by_id('kw').send_keys('itcast')

#模拟Enter回车键
driver.find_element_by_id('su').send_keys(Keys.RETURN)
time.sleep(5)

#清空输入框内容
driver.find_element_by_id('kw').clear()

#生成新的页面快照
driver.save_screenshot('itcast.png')

#获取当前url
print(driver.current_url)

driver.quit()
# 页面操作
# Selenium的WebDriver提供了各种方法来寻找元素，假设下面有一个表单输入框：
#
# <input type="text" name="user-name" id="passwd-id" />
# 那么：
#
# #获取id标签值
# element = driver.find_element_by_id("passwd-id")
# #获取name值
# element = driver.find_element_by_name("user-name")
# #获取标签名
# element = driver.find_element_by_tag("input")
# #也可以通过XPath来匹配
# element = driver.find_element_by_xpath(//input[@id="passwd-id"])