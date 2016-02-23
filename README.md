# baike_spider
## 使用python编写爬虫程序简单爬取百科百科的1000个页面url链接以及一些内容，算作python的简单入门实例

##这是刚刚学习的一个简单的python入门爬虫程序，主要包含以下内容：
###1、spider_main.py——》python爬虫程序主入口，初始化所有模块，以及调度爬虫任务
###2、url_manager.py——》url管理器，包括待爬取的url列表和已爬取的url列表，以及判断该url先前是否已经抓取过
###3、html_downloader.py——》html页面信息下载器，抓取url所在页面的信息
###4、html_parser.py——》html页面数据解析器，解析当前页面的有效数据以及一些新的url列表
###5、html_outputer.py——》html页面信息输出器，将爬虫程序抓取的信息输出到一个html页面进行展示

