from selenium import webdriver
import time,os
import pandas as pd
import xlrd,xlwt
# from xlutils.copy import copy
#使用selenium
#使用selenium的隐藏PhantimJS浏览器登陆账号后对内容获取
#注意frame与iframe的格式框切换
#driver = webdriver.PhantomJS(executable_path="E:\\mac\\id\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver=webdriver.Chrome(executable_path='./chromedriver')
#driver.set_preference('network.proxy.type', 1)
#driver.set_preference('network.proxy.http', '127.0.0.1')
#driver.set_preference('network.proxy.http_port', 17890)
driver.maximize_window()
all_shuo=[]
def get_shuoshuo(qq,path):
    # testexist(path)
    try:
        driver.set_page_load_timeout(10)
        driver.get('http://user.qzone.qq.com/{}/311'.format(qq))
        time.sleep(3)
    except:
        print (u'网页启动异常，请重新打开')
        time.sleep(2)
        driver.quit()
    try:
        driver.find_element_by_id('login_div')
    except:
        print (u"非好友无法进入空间无权限抓取内容")
        driver.quit()
    else:
        #登录QQ空间
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()#选择用户名框
        driver.find_element_by_id('u').send_keys('1330065671') #输入个人登录账号
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys('TSL87326980') #输入个人登录密码
        driver.find_element_by_id('login_button').click()
        time.sleep(3)
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
    except:
        print (u'空间加载异常，请重新打开')
        time.sleep(2)
        driver.quit()
    else:
        driver.switch_to.frame('app_canvas_frame')
    #    last_page=driver.find_element_by_css_selector('.mod_pagenav')
    #    page_num=re.findall('\d+',last_page.text)[-1]
        next_page='page'
        page=1
        try:

            while next_page:
                content = driver.find_elements_by_css_selector('.content')
                stime = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
                for con,sti in zip(content,stime):
                    data = {
                        'time':sti.text,
                        'shuos':con.text
                    }
                    # write_data(data['time'],data['shuos'],path)
                    all_shuo.append(data)
                    print('data',data)
                next_page=driver.find_element_by_link_text(u'下一页')
                page=page+1
                print (u'正在抓取第%d页面内容······'%page)
                next_page.click()

                time.sleep(3)
                driver.implicitly_wait(3)


            driver.quit()

        except:
            print (u'抓取到%d页面结束'%page)
            driver.quit()

# def  testexist(path):
#     if not os.path.exists(path):
#         w= xlwt.Workbook()
#         w.add_sheet('Sheet1')
#         w.save(path)
#     else:
#         os.remove(path)
#         w= xlwt.Workbook()
#         w.add_sheet('Sheet1')
#         w.save(path)

# def write_data(data1,data2,path):
#     f=xlrd.open_workbook(path)
#     sheet=f.sheet_by_name('Sheet1')
#     src=copy(f)
#     row=sheet.nrows
#     src.get_sheet(0).write(row,0,data1)
#     src.get_sheet(0).write(row,1,data2)
#     src.save(path)

if __name__ == '__main__':
   # work_path=raw_input(u'请输入存储数据路径--excle表格类型')2571278041
    work_path='shuo.csv'
    get_shuoshuo('2379044736',work_path)#输入好友QQ号hn2379044736
    df = pd.DataFrame(all_shuo)
    print('df', df.head())
    df.to_excel('shuo.xls')

   # '''/Users/ozintel/Downloads/Tsl_python_progect/znfw_project/znfw_crawer/simulation_browser_crawer/get_friends_shuo.py'''
