#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: lms
@file: contact.py
@time: 2020/5/17 15:58
@desc: 
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Contact(object):
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def add_member(self):
        sleep(2)

        add_button = self._driver.find_element(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
        sleep(3)
        add_button.click()
        sleep(3)
        self._driver.find_element(By.ID, 'username').send_keys('123aaa')
        self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys('111111')
        self._driver.find_element(By.ID, 'memberAdd_phone').send_keys('13240774711')

        commit = self._driver.find_element(By.CSS_SELECTOR, '.js_btn_save')
        sleep(2)
        commit.click()
        return True
