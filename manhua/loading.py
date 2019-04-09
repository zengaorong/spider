#coding=utf-8
import sys
import os
import time
import threading
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
# 封装 load方法 用于下载


class loading:

    # 两个初始化方法  先完成一种 传过来一个list 里面包含 项目名称 文件夹名称 文件数量 下载的URL 文件的类型
    def __init__(self):
        pass

    def __mkdir(self,path):
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        #print path
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


    def __load_one_chapter(self,comicName,comicIntrd,count,contentList,load_type,callback):
        retry_num = 0
        retry_max = 3
        self.__mkdir(comicName)
        self.__mkdir(comicName + "\\" + contentList['title'])
        serchfile = comicName + "\\" + contentList['title']
        num = 0
        if contentList['href'] == None or contentList['href'] == "":
            return
        if contentList['chapter_nums'] == 1:
            open(r'%s\%s.txt'%(comicName,comicName) , 'w').write(comicIntrd)
        for key in contentList['href']:
            #wait_url(time.time())
            load_url = key
            while True:
                try:
                    ir = requests.get(load_url,timeout=10)
                    sz = open(r'%s\%s%s.jpg'%(serchfile,contentList['title'],num) , 'wb').write(ir.content)
                    num = num + 1
                    break
                except:
                    retry_num += 1
                    if retry_num >= retry_max:
                        raise
                    print('下载失败，重试' + str(retry_num) + '次')
                    time.sleep(2)
                    # gloab_wronglist.append([contentName,comic_id])
        print contentList['title'] + "下载完成"
        callback()



    # 下载项目名称 文件夹名称 文件数量 下载的URL 文件的类型
    def down_data(self,map_lists):
        print map_lists
        _comicName  = _comicIntrd = _count = _contentList = _load_type =None
        for chapter_part in map_lists:
            _comicName = chapter_part['comicName']
            _comicIntrd = chapter_part['comicIntrd']
            _count = chapter_part['count']
            _contentList = chapter_part['contentList']
            _load_type = chapter_part['load_type']

        download_threads = []

        def __download_callback():
            downloaded_num = 0
            count = 0
            downloaded_num += 1
            #print('\r{}/{}... '.format(downloaded_num, count))

        for i in range(0,len(_contentList)):
            #for i in range(405,406):
            threadnums = 0
            for serchs in download_threads:
                if serchs.isAlive():
                    threadnums = threadnums + 1
            print threadnums
            if threadnums > 5:
                time.sleep(1 + threadnums-5)
            download_thread = threading.Thread(target=self.__load_one_chapter,
                                               args=(_comicName,_comicIntrd,_count,_contentList[i],_load_type,__download_callback))
            download_threads.append(download_thread)
            download_thread.start()
        [ t.join() for t in download_threads ]





