# -*- coding:utf-8 -*-
# from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from pyquery import PyQuery as pq
import time
import json


# #使用Selenium的webdriver实例化一个浏览器对象，在这里使用Phantomjs
# driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
# #设置Phantomjs窗口最大化
# driver.maximize_window()
# 登录QQ空间
def get_shuoshuo(qq):
    # # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    option.add_argument('-headless')  # 无头参数
    # option.add_experimental_option('prefs', prefs)  # 设置无图模式
    # # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option, executable_path='./chromedriver')


    # driver = webdriver.PhantomJS(executable_path='phantomjs-2.1.1-macosx/bin/phantomjs')
    # # driver.set_window_size(1366, 768)
    # # #设置Phantomjs窗口最大化
    # driver.maximize_window()

    #使用get()方法打开待抓取的URL
    driver.get('http://user.qzone.qq.com/{}/311'.format(qq))#进入说说的链接
    time.sleep(5)
    #等待5秒后，判断页面是否需要登录，通过查找页面是否有相应的DIV的id来判断
    try:
        driver.find_element_by_id('login_div')#说明出现了登陆界面
        a = True
    except:
        a = False
    if a == True:
        #如果页面存在登录的DIV，则模拟登录
        driver.switch_to.frame('login_frame')#frame内元素定位，首先要进入frame;frame标签有frameset、frame、iframe三种
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()  # 选择用户名框
        driver.find_element_by_id('u').send_keys('1330065671')
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys('TSL87326980')
        driver.find_element_by_id('login_button').click()
        time.sleep(3)
    driver.implicitly_wait(3)
    #判断好友空间是否设置了权限，通过判断是否存在元素ID：QM_OwnerInfo_Icon
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
        b = True
    except:
        b = False
    #如果有权限能够访问到说说页面，那么定位元素和数据，并解析
    if b == True:

        driver.switch_to.frame('app_canvas_frame')
        # wait = WebDriverWait(driver, 5)
        # page_last = wait.until(EC.presence_of_element_located(
        #     (By.CSS_SELECTOR, '#pager_last_0 > span'))).text  # 最后一页
        # print('last page',page_last)

        content = driver.find_elements_by_css_selector('.content')#所有含有content的
        stime = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
        for con, sti in zip(content, stime):
            data = {
                'time': sti.text,
                'shuos': con.text
            }
            print(data)
        pages = driver.page_source
        # soup = BeautifulSoup(pages, 'lxml')
    #尝试一下获取Cookie，使用get_cookies()
    cookie = driver.get_cookies()
    cookie_dict = []
    for c in cookie:
        ck = "{0}={1};".format(c['name'], c['value'])
        cookie_dict.append(ck)
    i = ''
    for c in cookie_dict:
        i += c
    print('Cookies:', i)
    print("==========完成================")
    time.sleep(15)
    driver.close()
    driver.quit()
if __name__ == '__main__':
    get_shuoshuo('2379044736')#好友的qq号码lw1029725413,hnd892845462,hnx2379044736

    #进入别人说说链接会自动跳出首先要登陆自己的qq空间，然后才会进入