#coding=utf-8
import sae
import os
import sys
from flask import Flask, request, render_template,jsonify
from sae.storage import Bucket
import time
import requests
import re
import json
from sae.ext.storage import monkey
from sae.taskqueue import Task, TaskQueue
monkey.patch_all()
reload(sys)
sys.setdefaultencoding('utf-8')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    #全局变量
    url_02 = "http://api.ishuhui.com/index/ish/ver"
    shuhui_load_dict = {}
    ir = requests.get(url_02)
    book_json = json.loads(ir.content) 
    bucket = Bucket('t')
    filestr = "/s/" + "t/" + "download_id_list.txt"
    download_id_list = getdown_id(bucket,filestr)
    
    time_over = time.strftime('%y-%m',time.localtime(time.time()))
    print time_over
    print download_id_list
    
    
    for key in range(0,10):
        temp_array = []
        chapater_id =  book_json['data']['cartoonLatest'][key]['id']
        chapater_book =  book_json['data']['cartoonLatest'][key]['book']
        chapater_number =  book_json['data']['cartoonLatest'][key]['number']
        chapater_title =  book_json['data']['cartoonLatest'][key]['title']
        chapater_name =  book_json['data']['cartoonLatest'][key]['name']
        temp_array = [chapater_name,chapater_title,chapater_id]
        shuhui_load_dict[chapater_id] = temp_array    
        
        if str(chapater_id) in download_id_list:
            continue       
        print "新的漫画".encode('GBK') + str(chapater_id)        
        url_04 = "http://hhzapi.ishuhui.com/cartoon/post/ver/c1579509/id/" + str(chapater_id) + '.json'
        ir = requests.get(url_04)
        decodejson = json.loads(ir.content)
        picture_nus = decodejson['data']['content_img']
        
        if len(json.loads(picture_nus)) == 0:
            numstr = str(chapater_book) + "-0-" + "n-" + str(chapater_number)
            url_load = "http://api.ishuhui.com/cartoon/post/ver/f6887413/num/" + numstr + '.json'
            ir = requests.get(url_load)
            decodejson = json.loads(ir.content)
            down_id = decodejson['data']['posts'][0]['url'].replace("http://hanhuazu.cc/cartoon/post?id=","")
            url_04 = "http://hhzapi.ishuhui.com/cartoon/post/ver/c1579509/id/" + str(down_id) + '.json'
            ir = requests.get(url_04)
            decodejson = json.loads(ir.content)
            
        load_picture(decodejson)
    bucket.put_object('download_id_list.txt', dict_to_text(shuhui_load_dict))     
    return "<h2>hoe<h2>"

def dict_to_text(data_dict):
    outstr = ""
    for key in data_dict:
        outstr = outstr + str(data_dict[key][0]) + '\t' + str(data_dict[key][1]) + '\t' + str(data_dict[key][2]) + '\n'
        
    return outstr

def getdown_id(bucket,filestr): 
    download_id_list = []
    if os.path.exists(filestr):
        listarray = bucket.get_object_contents('download_id_list.txt')
        for line in listarray.split('\n'):
            # 读取文档内容，循环存入漫画id
            if line == "\n" or line == "":
                continue
            download_id_list.append(line.split('\t')[2])
    else:
        bucket.put_object('download_id_list.txt', '')
        
    return download_id_list

def load_picture(load_decodejson): 
    bucket = Bucket('t')
    picture_dict = load_decodejson['data']['content_img']
    load_book_text = load_decodejson['data']['book_text']
    load_title = load_decodejson['data']['title']
    #这里在新浪云要变换下
    serchfile = load_book_text + "/" + load_title
    num = 0
    print "now loading:" + serchfile
    picture_dict = json.loads(picture_dict)
    sort_key = sorted(picture_dict)
    time_over = time.strftime('%y-%m',time.localtime(time.time()))
    monthfile = time_over + "/" + load_book_text
    
    '''
    try:
        print os.path.splitext(picture_dict[sort_key[0]].replace('/upload',""))[1]
    except Exception,e:
        print str(e)
        
    '''
    for key in sort_key:
        #wait_url(time.time())
        load_url = "http://pic01.ishuhui.com" + picture_dict[key].replace('/upload',"")
        #print load_url
        ir = requests.get(load_url)
        #sz = open(r'%s\num%s.jpg'%(serchfile,num) , 'wb').write(ir.content)
        pic_type = os.path.splitext(picture_dict[sort_key[0]].replace('/upload',""))[1]
        writeDate(bucket,creataddrname(load_book_text,load_title,'%s%s'%(load_title,num),pic_type),ir.content)
        writeDate(bucket,creataddrname(monthfile,load_title,'%s%s'%(load_title,num),pic_type),ir.content)
        num = num + 1  
    print load_title + "下载完成"
  
    
def writeDate(bucket,storagefile,file_data):
        bucket.put_object(storagefile,file_data)   
        
def creataddrname(manhuaname,charpatername,picturename,tpye):
    return manhuaname + "/" + charpatername + "/" + picturename  + tpye

application = sae.create_wsgi_app(app)