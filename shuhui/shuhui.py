#coding=utf-8
import sys
import time
import os
import json
import requests
import math
from sys import getsizeof
reload(sys)
sys.setdefaultencoding('utf-8')
gloab_time = 0
global_data = 0
isbreak = False
def home():
    #全局变量
    url_02 = "http://api.ishuhui.com/index/ish/ver"
    shuhui_load_dict = {}
    ir = requests.get(url_02)
    download_id_list = getdown_id()
    book_json = json.loads(ir.content)

    time_over = time.strftime('%y-%m',time.localtime(time.time()))
    print time_over

    for key in range(0,10):
        temp_array = []
        chapater_id =  book_json['data']['cartoonLatest'][key]['id']
        chapater_book =  book_json['data']['cartoonLatest'][key]['book']
        chapater_number =  book_json['data']['cartoonLatest'][key]['number']
        chapater_title =  book_json['data']['cartoonLatest'][key]['title']
        chapater_name =  book_json['data']['cartoonLatest'][key]['name']
        temp_array = [chapater_name,chapater_title,chapater_id]
        #在添加新漫画前介绍
        if isbreak:
            if str(chapater_id)  not in download_id_list:
                continue
            else:
                shuhui_load_dict[chapater_id] = temp_array
                continue
        shuhui_load_dict[chapater_id] = temp_array


        if str(chapater_id) in download_id_list:
            continue

        print "新的漫画".encode('GBK') + str(chapater_id)
        url_04 = "http://hhzapi.ishuhui.com/cartoon/post/ver/c1579509/id/" + str(chapater_id) + '.json'
        ir = requests.get(url_04)
        decodejson = json.loads(ir.content)
        picture_nus = decodejson['data']['content_img']
        if len(json.loads(picture_nus)) == 0:
            #实现第二套方案
            '''
            url_04 = "http://hhzapi.ishuhui.com/cartoon/post/ver/c1579509/id/" + str(chapater_id-1) + '.json'
            ir = requests.get(url_04)
            decodejson = json.loads(ir.content)
            picture_nus = decodejson['data']['content_img']
            print "重新下载".encode('GBK')
            print chapater_id
            '''
            numstr = str(chapater_book) + "-0-" + "n-" + str(chapater_number)
            url_load = "http://api.ishuhui.com/cartoon/post/ver/f6887413/num/" + numstr + '.json'
            #url_04 = "http://hhzapi.ishuhui.com/cartoon/post/ver/c1579509/id/" + str(8979) + '.json'
            ir = requests.get(url_load)
            decodejson = json.loads(ir.content)
            down_id = decodejson['data']['posts'][0]['url'].replace("http://hanhuazu.cc/cartoon/post?id=","")
            url_04 = "http://hhzapi.ishuhui.com/cartoon/post/ver/c1579509/id/" + str(down_id) + '.json'
            print url_04
            ir = requests.get(url_04)
            decodejson = json.loads(ir.content)
            #load_picture(decodejson)

        load_picture(decodejson)

    file = open("download_id_list.txt",'w')
    file.writelines(dict_to_text(shuhui_load_dict))
    file.close()


def dict_to_text(data_dict):
    outstr = ""
    for key in data_dict:
        outstr = outstr + str(data_dict[key][0]) + '\t' + str(data_dict[key][1]) + '\t' + str(data_dict[key][2]) + '\n'

    return outstr


def getdown_id():
    path_file = "download_id_list.txt"
    download_id_list = []
    if os.path.exists(path_file):
        file = open(path_file,'r')
        for line in file.readlines():
            # 读取文档内容，循环存入漫画id
            download_id_list.append(line.strip().split('\t')[2])

    else:
        file = open(path_file,'w')
        file.close()

    return download_id_list


def loading_test(nums):
    url_04 = "http://hhzapi.ishuhui.com/cartoon/post/ver/c1579509/id/" + str(nums) + '.json'
    decodejson = json.loads(ir.content)
    load_picture(decodejson)


def load_picture(load_decodejson):
    global global_data
    global isbreak
    picture_dict = load_decodejson['data']['content_img']
    load_book_text = load_decodejson['data']['book_text']
    load_title = load_decodejson['data']['title']
    #这里在新浪云要变换下
    serchfile = load_book_text + "\\" + load_title
    num = 0
    print "now loading:" + serchfile
    picture_dict = json.loads(picture_dict)
    sort_key = sorted(picture_dict)
    mkdir(load_book_text)
    mkdir(load_book_text + "\\" + load_title)

    time_over = time.strftime('%y-%m',time.localtime(time.time()))
    mkdir(time_over)
    mkdir(time_over + "\\" + serchfile)
    monthfile = time_over + "\\" + serchfile
    bar = ProgressBar(total = len(sort_key))

    for key in sort_key:
        #wait_url(time.time())
        load_url = "http://pic01.ishuhui.com" + picture_dict[key].replace('/upload',"")
        #print load_url
        ir = requests.get(load_url,timeout=10)
        global_data = global_data + int(sys.getsizeof(ir.content))
        sz = open(r'%s\%s%s.jpg'%(serchfile,load_title,num) , 'wb').write(ir.content)
        kz = open(r'%s\%s%s.jpg'%(monthfile,load_title,num) , 'wb').write(ir.content)
        #print num
        num = num + 1
        bar.move()
        bar.log()
    print load_title + "下载完成"

    if global_data > 1024*1024*12:
        print "data > 12M"
        isbreak = True

#如果图片下载时间<1秒 等待        
def wait_url(nowtime):
    global gloab_time
    if gloab_time == 0:
        gloab_time = nowtime
    else:
        if nowtime - gloab_time < 2:
            time.sleep(nowtime - gloab_time)


def mkdir(path):

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    print path
    isExists=os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        #print path+' 创建成功'
        # 创建目录操作函数

        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        #print path+' 目录已存在'
        return False

requestSession = requests.session()
UA = 'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-CN; \
HTC Velocity 4G X710s Build/IML74K) AppleWebKit/534.30 \
(KHTML, like Gecko) Version/4.0 UCBrowser/10.1.3.546 \
U3/0.8.0 Mobile Safari/534.30' # UC UA
requestSession.headers.update({'User-Agent': UA})



def getHtml():
    # path url = http://m.ac.qq.com/chapter/index/id/505441/cid/1
    #v2ex_session = requests.Session()
    #f = v2ex_session.get(login_page)

    cid_page = requestSession.get('http://www.37zw.net/1/1257/619223.html').text
    #op = requestSession.get("http://m.ac.qq.com/chapter/index/id/505441/cid/1")
    #print op.text
    file = open("myhtml.html",'w')
    file.writelines(cid_page)
    file.close()

def getSizeInNiceString(sizeInBytes):
    for (cutoff, label) in [(1024*1024*1024, "GB"),(1024*1024, "MB"),(1024, "KB"),]:
        if sizeInBytes >= cutoff:
            return "%.1f %s" % (sizeInBytes * 1.0 / cutoff, label)
    if sizeInBytes == 1:
        return "1 byte"
    else:
        bytes = "%.1f" % (sizeInBytes or 0,)
    return (bytes[:-2] if bytes.endswith('.0') else bytes) + ' bytes'

def ByteFormat(size,unit='Bytes'):
    units = ['Bytes','KB','MB','GB','TB','PB']
    return ('%.2f'+" "+unit) % (size/math.pow(1024,units.index(unit)))


class ProgressBar:
    def __init__(self, count = 0, total = 0, width = 50):
        self.count = count
        self.total = total
        self.width = width
    def move(self):
        self.count += 1
    def log(self):
        sys.stdout.write(' ' * (self.width + 9) + '\r')
        sys.stdout.flush()
        #print s
        progress = self.width * self.count / self.total
        sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
        sys.stdout.write('#' * progress + '-' * (self.width - progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()


if __name__=='__main__':
    home()