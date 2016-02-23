#coding=utf-8
# Created by feizi at 2016/2/23

import urllib2

#html页面下载器
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        #使用urllib2的urlopen方法抓取页面信息
        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()