from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from pyquery import PyQuery as pq
import time
import json

options = webdriver.ChromeOptions()
#   设置无图模式
prefs = {
    'profile.default_content_setting_values': {
        'images': 2
    }
}
# options.add_argument('--headless')          # 浏览器隐藏
options.add_argument('disable-infobars')#去除显示受控制
options.add_argument('--disable-gpu')
# options.add_experimental_option('prefs', prefs)        #设置无图模式
browser = webdriver.Chrome(chrome_options=options,executable_path='./chromedriver')
wait = WebDriverWait(browser, 5)


def get_last_page(qq):
    try:
        # url = f'https://user.qzone.qq.com/{qq}/311'
        url=f'http://user.qzone.qq.com/{qq}/311'
        browser.get(url)

        # try:
        #     browser.find_element(By.NAME, 'login_frame')  # 发现登陆的frame
        # except:
        #     raise
        # else:
        #     try:
        #         browser.switch_to.frame('login_frame')  # 发现之后进入login_frame
        #         login = wait.until(EC.element_to_be_clickable(
        #             (By.ID, 'img_out_1330065671')))  # 获取点击按钮  也可以进行输入账号密码，这个是自己的#最好现在电脑上登陆一次，把缓存留下
        #         login.click()  # 进行点击
        #     except Exception as e:
        #         print('error',e)
        #         raise
        time.sleep(5)

        try:
            browser.find_element_by_id('login_div')
            a = True
        except:
            a = False
        if a == True:
            # 如果页面存在登录的DIV，则模拟登录
            browser.switch_to.frame('login_frame')
            browser.find_element_by_id('switcher_plogin').click()
            browser.find_element_by_id('u').clear()  # 选择用户名框
            browser.find_element_by_id('u').send_keys('1330065671')
            browser.find_element_by_id('p').clear()
            browser.find_element_by_id('p').send_keys('TSL87326980')
            browser.find_element_by_id('login_button').click()
            time.sleep(3)
        browser.implicitly_wait(3)

        pages = browser.page_source
        f = open('aa.html', 'w')
        f.write(pages)


        # #下面这个找页数的似乎只对登陆的那个号有效，对其它号无效
        # browser.switch_to.frame('app_canvas_frame')  # 进入switch_to_frame
        # page_last = wait.until(EC.presence_of_element_located(
        #     (By.CSS_SELECTOR, '#pager_last_0 > span'))).text  # 最后一页
        # print('page_last:',int(page_last))
        # return int(page_last)
    except Exception as e:
        # get_last_page(qq)
        print('e',e)


flag = True

def get_page_text(n):
    global flag
    try:
        print('n:',n)
        if flag:
            browser.switch_to.frame('app_canvas_frame')#要添加这个否则找不到，当是非登陆的qq号时
            # flag=False
        content = browser.find_elements_by_css_selector('.content')  # 所有含有content的
        stime = browser.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
        for con, sti in zip(content, stime):
            data = {
                'time': sti.text,
                'shuos': con.text
            }
            yield data
            print(data)
        browser.switch_to.parent_frame()


        # doc = pq(browser.page_source)           # 获取页面的html
        # items = doc('#msgList > li.feed').items()          # 获取所有的说说
        # for item in items:      # 对说说进行分开
        #     yield {
        #         'time': item.find('div.box.bgr3 > div.ft > div.info > .c_tx3 > .c_tx').text(),
        #         'text': item.find('.content').text().lstrip('♡\n')
        #     }
        text = wait.until(EC.presence_of_element_located((By.ID, f'pager_go_{n-1}')))   # 获取跳转页的输入框
        text.send_keys(n+1)     # 输入下一页
        text.send_keys(Keys.ENTER)      #进行确定
    except Exception as e:
        print('出错',e)
        browser.close()


def write_page(page):
    with open('qq.txt', 'a', encoding='utf-8') as f:
        for page in get_page_text(page):
            f.write(json.dumps(page, ensure_ascii=False) + '\n')       # 将dict转换为json格式进行保存


if __name__ == '__main__':
    page_last = get_last_page('1029725413')#好友的qq号码hn2379044736#似乎只有登陆的那个号可以2379044736
    for i in range(1, 100):#page_last+1
        write_page(i)
    browser.close()