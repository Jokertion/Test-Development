#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: lms
@file: appium inspector.py
@time: 2020/5/23 10:07
@desc: 
"""
from appium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSearch(object):
    def setup(self):
        caps = dict()
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = "true"
        caps["dontStopAppOnReset"] = 'true'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        search_elem = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(search_elem))
        search_elem.click()
        search_input = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        search_input.send_keys("alibaba")
        element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        element.click()


