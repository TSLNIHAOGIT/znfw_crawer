from selenium import webdriver
import time

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
option.add_argument('-headless')  # 无头参数
# 打开chrome浏览器

driver = webdriver.Chrome(chrome_options=option,executable_path='./chromedriver')

driver.get("https://www.baidu.com")


#获取页面名为wraper的id标签的文本内容
data = driver.find_element_by_id('wrapper').text

#打印数据内容
print(data)

print ('driver.title',driver.title)



#生成页面快照并保存
driver.save_screenshot("chrome_baidu1.png")


driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(2)
#生成页面快照并保存
driver.save_screenshot("chrome_baidu2.png")#要等待页面加载完成否则截图是空的

driver.quit()




