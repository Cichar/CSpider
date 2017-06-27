# -*- coding:utf-8 -*-

""" 
   **  头部定义  **
     
    default ————> 默认
    wyy     ————> 网易云音乐
    zhihu   ————> 知乎
    
"""

headers = {
    'default': {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Connection': 'keep-alive',
                'User-Agent': '',
                },
    'wyy': {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Content-Type': 'application/json; charset=UTF-8',
                'Accept-Encoding': 'deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Connection': 'keep-alive',
                'Host': 'music.163.com',
                'User-Agent': '',
            },
    'zhihu': {
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json; charset=UTF-8',
                'Accept-Encoding': 'deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Connection': 'keep-alive',
                'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
                'Host': 'www.zhihu.com',
                'User-Agent': '',
            }
}
