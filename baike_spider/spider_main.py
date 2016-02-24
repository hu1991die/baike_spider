#coding=utf-8
# Created by feizi at 2016/2/23
#程序总入口
import datetime

from baike_spider import html_downloader
from baike_spider import html_outputer
from baike_spider import html_parser
from baike_spider import url_manager


class SpiderMain(object):
    #初始化加载所有模块,构造器
    def __init__(self):
        #url管理器
        self.urls = url_manager.UrlManager()
        #页面下载器
        self.downloader = html_downloader.HtmlDownloader()
        #页面数据解析器
        self.parser = html_parser.HtmlParser()
        #网页信息输出器
        self.outputer = html_outputer.HtmlOutputer()

    #爬虫调度
    def craw(self, root_url):
        #计数
        count = 1
        #将页面中待爬取的url列表添加进URL管理器中
        self.urls.add_new_url(root_url)

        # print '开始时间：'
        # print time.strftime('%Y-%m-%d %H:%M:%S')

        #开始时间
        start_time = datetime.datetime.now()

        #循环爬取数据
        while self.urls.has_new_url():
            #捕获异常信息
            try:
                #获取待爬取的url
                new_url = self.urls.get_new_url()

                print 'craw %d : %s ' % (count, new_url)

                #爬取页面有效数据信息
                html_cont = self.downloader.download(new_url)
                #解析器对页面数据信息进行解析，两个参数，当前待爬取的url，以及爬取好的页面数据,得到新的url列表以及数据信息
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                #将新的url添加进url管理器
                self.urls.add_new_urls(new_urls)
                #同时收集数据
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break
                count = count + 1
            except:
                print 'craw failed'

        end_time = datetime.datetime.now()
        # print '总共耗时：' + str((end_time - start_time).seconds) + ' 秒'
        print '总共耗时：%s 秒' % (end_time - start_time).seconds
        self.outputer.output_html()

#爬虫入口
if __name__=="__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
