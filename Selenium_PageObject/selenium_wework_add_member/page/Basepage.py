#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: lms
@file: Basepage.py
@time: 2020/5/20 8:28
@desc: 
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def BasePage():
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def __init__(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self._driver = webdriver.Chrome(options=options)
        if self._base_url != '':
            self._driver.get(self._base_url)
