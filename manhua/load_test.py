#coding=utf-8
import sys
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

reload(sys)
sys.setdefaultencoding('utf-8')

strs = requests.get(" http://www.baidu.com")
print strs.text

header_data_login = {
    'Host' : 'localhost:8081',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept' : '*/*',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding' : 'gzip, deflate',
    'X-Requested-With' : 'XMLHttpRequest',
    'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer' : 'http://localhost:8081/djypcg/',
    'Connection' : 'keep-alive',
    'Pragma' : 'no-cache',
    'Cache-Control' : 'no-cache'
}


WIDTH = 320
HEIGHT = 640
PIXEL_RATIO = 3.0
UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'



# 火狐
def firfox_loading():
    url = 'http://m.baidu.com'
    # 这里可以用Chrome、Phantomjs等，如果没有加入环境变量，需要指定具体的位置
    driver=webdriver.Firefox(executable_path='J:/pythonleo/driver/geckodriver')
    driver.get(url)
    action = webdriver.ActionChains(driver)
    # action.move_by_offset(0, 0).click() 正常 能够使用
    print "press"
    # action.send_keys(Keys.CONTROL + Keys.SHIFT + 'M')
    # action.key_down(Keys.F12).key_up(Keys.F12).perform()
    # action.send_keys(Keys.F12)
    action.perform()
    time.sleep(5)
    driver.close()

# 谷歌
def google_loading():
    # 谷歌手机模式启动
    mobileEmulation = {'deviceName': 'iPhone 4'}
    options = webdriver.ChromeOptions()
    #options.add_experimental_option('mobileEmulation', mobileEmulation)

    # 这里可以用Chrome、Phantomjs等，如果没有加入环境变量，需要指定具体的位置
    driver = webdriver.Chrome(executable_path='J:/pythonleo/driver/chromedriver',chrome_options=options)
    driver.maximize_window()

    driver.get('https://e-hentai.org/s/e1fdd6f001/1316041-13')
    pageSource = driver.page_source
    print pageSource

    action = webdriver.ActionChains(driver)
    action.send_keys(Keys.F12)
    action.perform()
    time.sleep(100)
    # quit 是完全关闭屏幕 close 是关闭标签页
    driver.quit()

def test_kkk():
    driver = webdriver.Chrome(executable_path='H:/pythonleo/driver/chromedriver')
    driver.get('http://m.baidu.com')
    builder = ActionChains(driver)
    builder.key_down(Keys.F12).perform()
    time.sleep(100)
    
    driver.quit()


# 实验下弄有妖气
def check_comic_u7():
    url_chapter = 'http://www.u17.com/comic/164261.html'
    url = 'http://www.u17.com/chapter/723986.html#image_id=5085531'
    check_url = 'http://www.u17.com/chapter/723986.html'
    re_data = requests.get(check_url)
    print re_data.text


#  似乎有妖气难度不高 额  漫画章节里面有这个 实验base64 解析有可以 如果不开会员 获取的是马赛克的  这个确实不清楚要怎么弄 
'''
<script>
var _cfg_tucao_disabled = 0;
var is_go_out = true;
var image_config = {
    comic: {"comic_id":"164261","name":"\u62fe\u9057\u5f55","cate_id":"1","series_status":"0","accredit":"0","user_id":"108005","affiche":"\u6f2b\u753b\u5bb6\u590f\u8fbe\u9996\u90e8\u5168\u5f69\u77ed\u7bc7\u6f2b\u753b\u96c6\u300a\u62fe\u9057\u5f55\u300b\u7cfb\u5217\u767b\u5f55\u6709\u5996\u6c14\uff0c\u6b22\u8fce\u6536\u85cf\u54e6","short_description":"\u6c5f\u6e56\u513f\u5973 \u751f\u6b7b\u6c89\u6d6e","read_order":"1","read_mode":"1","create_time":"1509758194","update_time":"1509758194","next_update_time":"0000-00-00","last_update_time":"1525212001","last_update_chapter_name":"\u7b2c4\u8bdd \u5148\u751f","last_update_chapter_id":"772213","group_ids":"2","theme_ids":"3,5","editor_level":"1","first_letter":"S","cover":"2017\/11\/108005_1509843405_MDUlDXv5O954.jpg","status":"2","is_read":"0","pass_chapter_num":"7","author_name":"\u590f\u8fbe","op_time":"1513665731","op_name":"\u4e03\u5f69\u6708\u5f7177","read_time":"1509761534","pass_time":"1509761534","chapter_num":"7","editor_id":"2","is_vip":"0","price":"0","share":"0","service":null,"recommend_time":"1525471201","week_more":"1","recommend_type":"0","mobile_share":"0","script_author":"\u590f\u8fbe","painting_author":"\u590f\u8fbe","modify_time":"2018-05-07 02:31:53","comic_type":"0","first_chapter_pass_time":null,"comic_parent":null,"gift":"","gift_images":"","last_three_chapter_id":"736088"},
    chapter: {"chapter_id":"723986","comic_id":"164261","name":"\u7b2c1\u8bdd \u7ea8\u7ed4","order_no":"1000","status":"2","create_time":"1509758357","update_time":"1512026113","op_time":"1509761400","op_name":"\u8bfa\u5c0f\u4e03","is_read":"1","read_time":"0","pass_time":"1509761400","type":"0","image_total":32,"user_id":"108005","image_encoding":"38657037","vip_images":"0","edit_chapter_id":"0","price":"0","sale":"0","user_read_num":"6683","read_num":"28598","total_tucao":"320","size":"4294967295","release_time":"1509811200","publish_time":"1509811200","grade_total":"0","grade_count":"0","zip_size":"2637290","crop_zip_size":"2637290","main_body":"0","linkt":0},
    prev_chapter: null,
    next_chapter: {"chapter_id":"730738","comic_id":"164261","name":"\u7b2c2\u8bdd \u5e08\u7236\uff081\uff09","order_no":"2000","status":"2","create_time":"1512008602","update_time":"1512552553","op_time":"1512009578","op_name":"KINZA_3104","is_read":"1","read_time":"0","pass_time":"1512009578","type":"0","image_total":"12","user_id":"108005","image_encoding":"68626215","vip_images":"0","edit_chapter_id":"0","price":"0","sale":"0","user_read_num":"1814","read_num":"8071","total_tucao":"76","size":"2874200064","release_time":"0","publish_time":"1512009578","grade_total":"0","grade_count":"0","zip_size":"1101048","crop_zip_size":"1100261","main_body":"1","linkt":0},
    image: {},
    prev_image: null,
    next_image: null,
    image_list: {"1":{"image_id":"5085532","width":"900","height":"1273","total_tucao":"32","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4OTYxX1diTG01VDVMNjM1Zi5jODIzOF9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":1},"2":{"image_id":"5085496","width":"900","height":"1273","total_tucao":"3","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTEyMDI2MTEzXzFndDdqaVJSanJHNC4xYzNlZF9zdm9sLmpwZw==","lightning":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxL3dwLzEwODAwNV8xNTEyMDI2MTEzXzFndDdqaVJSanJHNC43ODA2Nl81MC5qcGc=","is_seal":0,"page":2},"3":{"image_id":"5085497","width":"900","height":"1273","total_tucao":"7","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzIxXzY0MTdLNjNLbFgzNC44NGI3Yl9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":3},"4":{"image_id":"5085498","width":"900","height":"1273","total_tucao":"10","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzIxX1FGQUp5aVFzOXNveS41NTk5N19zdm9sLmpwZw==","lightning":"","is_seal":0,"page":4},"5":{"image_id":"5085499","width":"900","height":"1273","total_tucao":"7","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzIyX3g2NnZUMnZGRTJIWC41ODRhMF9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":5},"6":{"image_id":"5085500","width":"900","height":"1273","total_tucao":"4","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzIyX3o3Qm9ZMk1SRGVlay4wNDlmZF9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":6},"7":{"image_id":"5085501","width":"900","height":"1273","total_tucao":"6","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzIyXzgyTkV5Tm5IRWVOZC4yNGRlOV9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":7},"8":{"image_id":"5085502","width":"900","height":"1273","total_tucao":"13","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzIyXzE4NGEzbWowNjkxSS5lYzU5MF9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":8},"9":{"image_id":"5085503","width":"900","height":"1273","total_tucao":"8","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzIzXzRTU3ZyUjhBMEI1bC45MzU0OF9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":9},"10":{"image_id":"5085504","width":"900","height":"1273","total_tucao":"27","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzIzX05kd1dRWHhuV2x4eC4wNDA3ZF9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":10},"11":{"image_id":"5085505","width":"900","height":"1273","total_tucao":"7","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzI0X21IUUp1b1VkZU9ETy4wYjA0NV9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":11},"12":{"image_id":"5085506","width":"900","height":"1273","total_tucao":"8","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzI0X3paM3hhUTNjekFDNS4zNWViNl9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":12},"13":{"image_id":"5085507","width":"900","height":"1273","total_tucao":"9","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzI1X1RmeDl1QnlBYm5iRC5kMTFlNF9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":13},"14":{"image_id":"5085508","width":"900","height":"1273","total_tucao":"8","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzI2X2JDUUhlcFBxclBRNS5iNWVlZV9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":14},"15":{"image_id":"5085509","width":"900","height":"1273","total_tucao":"3","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzI3XzloQ0lXaFJHcTlaMS5iMzgwM19zdm9sLmpwZw==","lightning":"","is_seal":0,"page":15},"16":{"image_id":"5085510","width":"900","height":"1273","total_tucao":"2","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzI4X0w0MnNjN1V0ZU9XNy5mMTJmMV9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":16},"17":{"image_id":"5085511","width":"900","height":"1273","total_tucao":"6","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzI5XzBIU0Rmc0hCbm9zNy4zNDFmYV9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":17},"18":{"image_id":"5085512","width":"900","height":"1273","total_tucao":"4","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzMwXzkzTmRMM3Z0VjJEbi4wZWZmYV9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":18},"19":{"image_id":"5085513","width":"900","height":"1273","total_tucao":"1","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzMwX3RvWmdTYThyR0E4ZC4xNmY2NV9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":19},"20":{"image_id":"5085514","width":"900","height":"1273","total_tucao":"2","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzMwX1o1OXo1UlE5YllJaS5hYTVjYl9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":20},"21":{"image_id":"5085515","width":"900","height":"1273","total_tucao":"0","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzMxX3A0Y2NjUmEzQ09ETC5lNGZkM19zdm9sLmpwZw==","lightning":"","is_seal":0,"page":21},"22":{"image_id":"5085516","width":"900","height":"1273","total_tucao":"9","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzMyX0xHR0dHbEpwRVc3RS4wMjBlZF9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":22},"23":{"image_id":"5085517","width":"900","height":"1273","total_tucao":"26","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzMyXzNlaDh6MDA1a3o1MC45ZGE3Nl9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":23},"24":{"image_id":"5085518","width":"900","height":"1273","total_tucao":"15","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzMzXzBYQlVsOFhCS0x1TS44ZmUwZV9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":24},"25":{"image_id":"5085519","width":"900","height":"1273","total_tucao":"3","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzM0X2xqWWp6eVhobEs4Wi41NWJkYl9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":25},"26":{"image_id":"5085520","width":"900","height":"1273","total_tucao":"10","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzM1XzZ6bjNNZERoeFdBTC5mMTUwY19zdm9sLmpwZw==","lightning":"","is_seal":0,"page":26},"27":{"image_id":"5085521","width":"900","height":"1273","total_tucao":"11","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzM1X0ZFSWo2ZVRBbDZmMi5hOGQ2YV9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":27},"28":{"image_id":"5085522","width":"900","height":"1273","total_tucao":"11","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzM2X3daV2tyUGhrUnV3OC45ODdmZl9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":28},"29":{"image_id":"5085523","width":"900","height":"1273","total_tucao":"34","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzM2X0tscHZEN1B2VnFkSi4yNjViNV9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":29},"30":{"image_id":"5085524","width":"900","height":"1273","total_tucao":"10","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4MzM3XzkyMk8xNHJZcVFQby5iZDUyNF9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":30},"31":{"image_id":"5085525","width":"900","height":"1273","total_tucao":"11","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTEyMDI1NzYzX1MybUlKMml5aXZqcy4zYWNlYl9zdm9sLmpwZw==","lightning":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxL3dwLzEwODAwNV8xNTEyMDI1NzYzX1MybUlKMml5aXZqcy43M2VhY181MC5qcGc=","is_seal":0,"page":31},"32":{"image_id":"5085531","width":"900","height":"1273","total_tucao":"12","type":"0","src":"aHR0cDovL2ltZzEudTE3aS5jb20vMTcvMTEvMTY0MjYxLzEwODAwNV8xNTA5NzU4OTYwX0FHTGFsZjJvNDRLSC4yYzhjZl9zdm9sLmpwZw==","lightning":"","is_seal":0,"page":32}},
    image_pages: {"5085532":1,"5085496":2,"5085497":3,"5085498":4,"5085499":5,"5085500":6,"5085501":7,"5085502":8,"5085503":9,"5085504":10,"5085505":11,"5085506":12,"5085507":13,"5085508":14,"5085509":15,"5085510":16,"5085511":17,"5085512":18,"5085513":19,"5085514":20,"5085515":21,"5085516":22,"5085517":23,"5085518":24,"5085519":25,"5085520":26,"5085521":27,"5085522":28,"5085523":29,"5085524":30,"5085525":31,"5085531":32},
    scrollMode: {
        Link: 'http://www.u17.com/chapter_vip/723986.shtml',
        Hash: null
    }

};
var chapter_cache = {count:0};
</script>
'''


if __name__ == '__main__':
    google_loading()
