#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: lms
@file: test_add_member.py
@time: 2020/5/17 20:18
@desc: 
"""

from PO.selenium_wework_add_member.page.index import Index


class TestAddMember():
    def setup(self):
        # 初始化浏览器
        self.index = Index()

    def test_member_add(self):
        self.index.goto_contact().add_member()
