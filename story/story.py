#coding=utf-8
import sys
import time
import requests
from bs4 import BeautifulSoup
from datetime import  datetime
reload(sys)
sys.setdefaultencoding('utf-8')

head = {
    "Connection": "keep-alive",
    "Cache-Control": "no-cache",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8"
}

#https://www.yangguiweihuo.com/11/11516/23008885.html
# url = "https://www.yangguiweihuo.com/11/11516/23008885.html"
# url = "https://www.biquke.com/bq/3/3714/2739693.html"
# url = "http://www.biquge.lu/s.php?ie=gbk&s=15244670192641769733&q=1"

def story_spider_for_biequge(url):
    respons = requests.get(url,headers=head,timeout=30)
    with open("result.html","w") as f:
        f.writelines(respons.text.replace('\r','\n'))

    soup = BeautifulSoup(open("result.html"),"html.parser")
    div_list = soup.find("div" ,id="content")
    print div_list
    #print div_list
    datas = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    %s
    </body>
    </html>
    '''%div_list

    now = datetime.now()
    with open("%s.html"%now.strftime('%Y-%m-%d-%H-%M-%S'),'w') as f:
        f.writelines(datas)








# lists = []
# with open("result1.html","r") as f:
#     lists = f.readlines()
#
# for key in lists:
#     print repr(key)
#     print key
#
# print '<!DOCTYPE html>\r<html>\r<body id="wrapper">\r</body>\r</html>'