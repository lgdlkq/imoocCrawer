#!usr/bin/env python3
# coding=utf-8

__author__ = 'lgd'
from baike_spider import url_manager, html_downloader, html_outputer, html_parser

#爬虫调度程序
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)#添加一个URL
        while self.urls.has_new_url():#判断是否有未爬取的URL
            try:
                new_url = self.urls.get_new_url()#取出一个URL
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.dowmload(new_url)#下载取出的URL
                new_urls, new_data = self.parser.parse(new_url, html_cont)#获取URL的信息URL中新的URL
                self.urls.add_new_urls(new_urls)#添加获取到的新的URL集
                self.outputer.collect_data(new_data)#收集获取到的URL的数据
                if count == 30:#获取1000个URL的数据
                    break
                count += 1
            except:
                print('craw failed!')

        self.outputer.output_html()#输出获取到的结果数据（XML）


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
