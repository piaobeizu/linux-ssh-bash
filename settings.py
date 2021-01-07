#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wxk on 2018/3/28 下午1:15
# Email="wangxk1991@gamil.com"
# Desc: 系统配置文件
SHOW_SERVER = {
    "aliyun": ["aliyun-vpn-8.210.171.119"],
    "cr-dev": [
        "cr-dev-master-10.20.17.193", "cr-dev-worker01-10.20.17.102",
        "cr-dev-worker02-10.20.17.249", "cr-dev-worker03-10.20.11.241",
        "cr-dev-worker04-10.20.11.242", "cr-dev-worker05-10.20.11.240",
    ]
}
SERVER = {
    "aliyun-vpn-8.210.171.119": ["22", "root", "8.210.171.119", False,"ALIYUN@wxk1991.com"],
    "rc-rc-master-10.20.17.193": ["22", "root", "10.20.17.193", True],
    "cr-dev-worker01-10.20.17.102": ["22", "root", "10.20.17.102", True],
    "cr-dev-worker02-10.20.17.249": ["22", "root", "10.20.17.249", True],
    "cr-dev-worker03-10.20.11.241": ["22", "root", "10.20.11.241", True],
    "cr-dev-worker04-10.20.11.242": ["22", "root", "10.20.11.242", True],
    "cr-dev-worker05-10.20.11.240": ["22", "root", "10.20.11.240", True],
}
