#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: lms
@file: test_add_member.py
@time: 2020/5/17 20:18
@desc: 
"""

from Selenium_PageObject.selenium_wework_add_member.page.index import Index


class TestAddMember(object):
    def __init__(self):
        # 初始化浏览器
        self.index = Index()

    def test_member_add(self):
        contact = self.index.goto_contact()
        # todo: 增加断言和验证函数
        # todo: 修改sleep瞎睡的问题
        # todo： 抽离出初始化的部分和driver
        contact.add_member()