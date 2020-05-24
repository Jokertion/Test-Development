#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Mollyviron
@file: test_xueqiu_search.py
@time: 2020/5/23 23:34
@desc:
使用 Appium Inspector 录制雪球的搜索功能，比如搜索 alibaba, jd, xiaomi

注意：
    使用录制功能完成上面的功能，

    进行简单的重构，使用 pytest 测试框架。

    可以加入参数化，实现多条搜索功能的测试用例。

    合理使用 setup_class, setup ，加快执行速度

    添加数据验证，assert
"""
from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
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
        # caps["dontStopAppOnReset"] = 'true'
        caps["skipDeviceInitialization"] = 'true'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('company, stock_code', [('ali', 'BABA'), ('xiaomi', '01810')])
    def test_search(self, company, stock_code):
        search = (MobileBy.ID, "com.xueqiu.android:id/home_search")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(search))
        self.driver.find_element(*search).click()

        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(f"{company}")

        search_input = (MobileBy.XPATH, f"//*[@text='{stock_code}']")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(search_input))
        self.driver.find_element(*search_input).click()

        add_optional = (MobileBy.XPATH, f"//*[@text='{stock_code}']/../../..//*[@text='加自选']")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(search_input))
        self.driver.find_element(*add_optional).click()

        res = (
            MobileBy.XPATH, f"//*[@text='{stock_code}']/../../..//*[@resource-id='com.xueqiu.android:id/followed_btn']")
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(res))
        add_results = self.driver.find_element(*res).text
        assert add_results == "已添加"
