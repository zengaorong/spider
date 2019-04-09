#coding=utf-8
import time
import sys
from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf-8')


def login(name, passwd):
    url = 'https://pan.baidu.com/'
    # 这里可以用Chrome、Phantomjs等，如果没有加入环境变量，需要指定具体的位置
    driver = webdriver.Chrome(executable_path='J:/pythonleo/driver/chromedriver')
    driver.maximize_window()
    driver.get(url)
    print('开始登录')
    chg_field = driver.find_element_by_class_name('pass-login-tab').find_element_by_class_name('account-title')
    chg_field.click()

    name_field = driver.find_element_by_id('TANGRAM__PSP_4__userName')
    name_field.send_keys(name)
    passwd_field = driver.find_element_by_id('TANGRAM__PSP_4__password')
    passwd_field.send_keys(passwd)
    login_button = driver.find_element_by_id('TANGRAM__PSP_4__submit')
    login_button.click()
    time.sleep(20)
    return driver.get_cookies()


if __name__ == '__main__':
    login_name = "zengaorong1"
    login_passwd = "6monthdleo"
    cookies = login(login_name, login_passwd)
