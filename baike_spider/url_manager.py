#coding=utf-8
# Created by feizi at 2016/2/23

#URL管理器
class UrlManager(object):
    #构造函数(待爬取的url列表，已经爬取过的url列表)
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    #添加单个待爬取的url到url管理器中
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    #添加多个待爬取的url列表到url管理器中（批量添加）
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            #循环添加
            self.add_new_url(url)

    #判断是否有新的待爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    #获取新的待爬取的url
    def get_new_url(self):
        #从待爬取的url列表中取出一个待爬取的url,pop()方法先取出再移除
        new_url = self.new_urls.pop()
        #取出待爬取的url之后再添加进已爬取的url列表中
        self.old_urls.add(new_url)
        #返回待爬取的url
        return new_url
