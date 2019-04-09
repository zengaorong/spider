
#coding=utf-8
import sys
import time
import requests
from bs4 import BeautifulSoup
from datetime import  datetime
reload(sys)
sys.setdefaultencoding('utf-8')

# head = {
#     "Connection": "keep-alive",
#     "Cache-Control": "no-cache",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
#     "Accept": "image/webp,image/apng,image/*,*/*;q=0.8"
# }
# url = "http://www.biquge.lu/s.php?ie=gbk&s=15244670192641769733&q=%s"%"元尊"
#
# respons = requests.get(url,headers=head)
#
# with open("list.html","w") as f:
#     f.writelines(respons.text.replace('\r','\n'))
#
# print respons.text

soup = BeautifulSoup(open("list.html",'r'),"html.parser")
# print soup
div_list = soup.find_all("div",{'class','bookbox'})
#print div_list

# 小说库 小说id 小说url 最近章节url 章节名称 最新章节url 名称 作者 简介
# 对于数据库 添加章节字段 但是不是在该处 而是执行更新的时候
#story_id story_url,story_name,story_chapter_url,story_chapter_name,story_intro,author

story_list = []
for cell in div_list:
    temp_list = []
    #print type(cell)
    list_a = cell.find_all('a')
    story_url,story_chapter_url,story_name,story_chapter_name = list_a[1]['href'],list_a[2]['href'],list_a[1].string,list_a[2].string
    #print story_url,story_chapter_url,story_name,story_chapter_name
    author = cell.find('div',{'class','author'}).string
    story_intro = cell.find('p').string



# story_list = soup.find("div",_class='nav')
# print story_list