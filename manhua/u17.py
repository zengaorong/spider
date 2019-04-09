#coding=utf-8
import time
import sys
import requests
from bs4 import BeautifulSoup
import re
import base64
import json
import ast
import demjson

reload(sys)
sys.setdefaultencoding('utf-8')

def getdata():
    down_url = "http://www.u17.com/chapter/51336.html#image_id=420285"
    html_data = requests.get(down_url)
    #print html_data.text

    soup = BeautifulSoup(html_data.text,"html.parser")
    #div_list = soup.find_all("script" ,class_='rank-row-one-third f-fl')

    #soup = BeautifulSoup(data, "html.parser")
    pattern = re.compile(r"var image_config = (.+?);", re.M | re.S)
    script = soup.find_all("script", text=pattern)
    # print type(script[0])
    # print script[0].image_config
    print script[0].text

    #print pattern.search(script[0].text).group(0).replace('var','')
    to_json_str =  pattern.search(script[0].text).group(0).replace('var','')
    to_json_str =  to_json_str.replace('\r\n','')
    to_json_str =  to_json_str.replace('\"','"')
    to_json_str =  to_json_str.replace('image_config = ','')
    to_json_str =  to_json_str.replace(';','')
    #print to_json_str
    # data = json.loads(to_json_str)

    json_obj = demjson.decode(to_json_str)
    print json_obj['image_list']

    #print json.loads(data)



    #div_list = soup.find_all("div" ,class_='comic-item comic-item--h sub-rank-comic-item')


getdata()
# url_s = 'aHR0cDovL2ltZzUudTE3aS5jb20vMTEvMDQvMTQzMjUvMTA4MDA1XzEzMDM1NDUzMTRfNmlUZ1BaT1QwajVjLjExOWIwX3N2b2wuanBn'
# print base64.b64decode(url_s)



# test_str = '{comic: {"comic_id":"14325","name":"\u957f\u6b4c\u884c","cate_id":"1","series_status":"0","accredit":"3","user_id":"108005"}}'
# print json.loads(test_str)

