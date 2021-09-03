# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "超时空蛋蛋"
site_logo = "${static_prefix}logo.png"
site_build_date = "2016-08-23T16:51+08:00"
author = "meowdan"
email = "edwiinme@gmail.com"
author_homepage = "https://www.meowdan.cn"
description = "这是一个单机版blog。"
key_words = ['Maverick', '超时空蛋蛋', 'Galileo', 'blog']
language = 'zh-CN'
#external_links = 
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/meowdan/",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/meowdan/",
        "icon": "gi gi-github"
    },
    {
        "name": "instagram",
        "url": "https://www.instagram.com/meowdan_/",
        "icon": "gi gi-instagram"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
