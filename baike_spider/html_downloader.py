#!usr/bin/env python3
#coding=utf-8

__author__ = 'lgd'

from urllib import request

#下载器
class HtmlDownloader(object):
    def dowmload(self,url):
        if url is None:
            return None

        response=request.urlopen(url)
        if response.getcode()!= 200:
            return None
        return response.read()