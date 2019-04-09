#coding=utf-8
import sys
import requests
import time
import json
import random
import threading
from bs4 import BeautifulSoup
from selenium import webdriver
from loading import loading

reload(sys)
sys.setdefaultencoding('utf-8')

# User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1

header_data_wanyi_rank = {
    'Host' : 'manhua.163.com',
    'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1',
    'Accept' : '*/*',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding' : 'gzip, deflate',
    'X-Requested-With' : 'XMLHttpRequest',
    'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer' : 'http://localhost:8081/djypcg/',
    'Connection' : 'keep-alive',
    'Pragma' : 'no-cache',
    'Origin' : 'https://h5.manhua.163.com',
    'Cache-Control' : 'no-cache'
}



def has_class_but_no_title(tag):
    return tag.has_attr('class') and not tag.has_attr('title')

# 火狐
def firfox_loading(chapter_urls_list):
    wanyi_url = 'https://manhua.163.com/'
    #driver = webdriver.Chrome(executable_path='J:/pythonleo/driver/chromedriver')
    #driver=webdriver.Firefox(executable_path='J:\pythonleo\driver\geckodriver')
    driver=webdriver.Chrome(executable_path='J:/pythonleo/driver/chromedriver')
    driver.implicitly_wait(2)

    down_read = open("down.txt",'r')
    list = down_read.readlines()
    down_read.close()



    for key in chapter_urls_list:

        if key + "\n" in list:
            print "have down"
            continue

        url = wanyi_url + key
        # 这里可以用Chrome、Phantomjs等，如果没有加入环境变量，需要指定具体的位置



        try:
            driver.get(url)
            try:
                myDynamicElement = driver.find_element_by_class_name("j-load-more-button")
                myDynamicElement.click()
                js = 'document.getElementsByClassName("j-load-more-button")[0].click();'
                driver.execute_script(js)
            except:
                pass
            chapter_load(driver.page_source)
            down_file = open("down.txt",'a+')
            down_file.writelines(key + "\n")
            down_file.close()
        except:
            erro_file = open("wrong.txt",'a+')
            erro_file.writelines(url + "\n")
            erro_file.close()
        #
        #

    # file = open('wanyi_chapters.html','w')
    # file.writelines(driver.page_source)
    # file.close()
    driver.close()


def get_list(url_ids):
    print "https://h5.manhua.163.com/reader/section/" + url_ids + ".json"
    file = requests.get("https://h5.manhua.163.com/reader/section/" + url_ids + ".json")
    decodejson = json.loads(file.content)
    with open('./'+"pic_json_data.json",'w')as f:
        json.dump(decodejson,f)

    with open('./'+'pic_json_data.json')as f:
        cookie=json.load(f)

    if cookie['msg'] == '成功':
        url_list = []
        for key in cookie['images']:
            url_list.append(key['highUrl'])
        return url_list

# 获取日漫版的全部url 这里有个排行 周点击量的数据
def get_manhua_chapter_urls():
    url = 'https://manhua.163.com/rank/list.do?type=1000&periodType=1'
    re_data =  requests.get(url)
    soup = BeautifulSoup(re_data.text,"html.parser")
    div_list = soup.find_all("div" ,class_='rank-row-one-third f-fl')
    div_list = soup.find_all("div" ,class_='comic-item comic-item--h sub-rank-comic-item')
    chapter_urls_list = []
    for key in div_list:
        chapter_urls_list.append(key.find_all("div" ,class_='comic-desc')[0].a['href'])

    return chapter_urls_list



def chapter_load(charpter_html):
    soup = BeautifulSoup(charpter_html,"html.parser")
    div_list = soup.find_all("div" ,class_='m-chapter-item f-fl ')
    contentList = []
    for key in div_list:
        map_temp = {}
        map_temp['href'] = get_list(key.a['href'].replace('/reader',""))
        time.sleep(random.randrange(1,2))
        map_temp['title'] = key.a['title']
        map_temp['chapter_nums'] = key.span.span.text
        contentList.append(map_temp)
    # download_threads = []
    # def download_callback():
    #     downloaded_num = 0
    #     count = 0
    #     downloaded_num += 1
    #
    # for key in div_list:
    #     threadnums = 0
    #     for serchs in download_threads:
    #         if serchs.isAlive():
    #             threadnums = threadnums + 1
    #     print threadnums
    #     if threadnums > 10:
    #         time.sleep(1)
    #     download_thread = threading.Thread(target=get_list,
    #                                        args=(key.a['href'].replace('/reader',"")))
    #     download_threads.append(download_thread)
    #     download_thread.start()
    # [ t.join() for t in download_threads ]
    #
    # for key in download_threads:
    #     contentList.append(key.get_result)
    chapter_nums =  len(div_list)
    chapter_list = soup.find_all("div" ,class_='sr-detail f-pr')
    chapter_name = chapter_list[0].find_all('h1',class_='sr-detail__heading')[0].string
    chapter_intro = chapter_list[0].find_all('dl',class_='sr-dl multi-lines j-desc-inner')[0].dd.text


    load_requset=loading()
    charpter_map = {}
    charpter_map['comicName'] = chapter_name
    charpter_map['comicIntrd'] = chapter_intro
    charpter_map['count'] = chapter_nums
    charpter_map['contentList'] = contentList
    charpter_map['load_type'] = '.jpg'
    map_list = []
    map_list.append(charpter_map)
    load_requset.down_data(map_list)


netcard = '/proc/net/dev'
def get_net_data():
    nc = netcard or '/proc/net/dev'
    fd = open(nc, "r")
    netcardstatus = False
    for line in fd.readlines():
        if line.find("eth0") >= 0 or line.find("enp") >= 0:
            netcardstatus = True
            field = line.split()
            recv = field[0].split(":")[1]
            recv = recv or field[1]
            send = field[8]
    if not netcardstatus:
        fd.close()
        print 'Please setup your netcard'
        sys.exit()
    fd.close()
    return (float(recv), float(send))

if __name__ == '__main__':
    # 首先获取榜单页面 获取漫画id信息
    # 漫画页面 获取漫画信息
    # 下载

    # 查询下载失败原因  在下载目录下更新一张表 用于记录下载的漫画名称 id 第二次下载时 跳过这些漫画
    # 出错处理

    chapter_urls_list = get_manhua_chapter_urls()
    firfox_loading(chapter_urls_list)













