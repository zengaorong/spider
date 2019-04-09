#coding=utf-8
import requests
import sys
from bs4 import BeautifulSoup
from story import story_spider_for_biequge
reload(sys)
sys.setdefaultencoding('utf-8')

# url = "http://www.biquge.lu/book/39651/"
# respons = requests.get(url)
# respons.encoding='gbk'
# print type(respons.text)
#
# with open("chapter.html","w") as f:
#     f.writelines(respons.text.replace('\r','\n'))



# html_list = None
# with open("chapter.html","r") as f:
#     html_list = f.readlines()

#print respons.text


soup = BeautifulSoup(open("chapter.html","r"),'html.parser')



chapter_soup = soup.find('div',{'class','listmain'})
chapter_list = chapter_soup.find_all('dd')
# 除去最新章节的6章
for key in chapter_list[6:]:
    print key.string
    print key.find('a')['href']
    #http://www.biquge.lu/book/39651/19467857.html
    story_spider_for_biequge('http://www.biquge.lu/'+key.find('a')['href'])
    break