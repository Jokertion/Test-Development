#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: lms
@file: test_dw_pytest.py
@time: 2020/5/23 11:25
@desc: 
"""
from appium import webdriver
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
        caps["unicodeKeyboard"] = 'true'
        caps["resetKeyboard"] = 'true'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        """
        app控件定位课实例：
        1、打开雪球app
        2、点击搜索输入框
        3、输入"阿里巴巴"
        4、结果中选择"阿里巴巴", 然后进行点击
        5、获取这只港股的股价，判断股价 >190
        :return:
        """
        search = (MobileBy.ID, "com.xueqiu.android:id/tv_search")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(search))
        self.driver.find_element(*search).click()

        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")

        res = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(res))
        self.driver.find_element(*res).click()

        price = (MobileBy.ID, "com.xueqiu.android:id/current_price")
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*price))
        cur_price = float(self.driver.find_element(*price).text)
        print(cur_price)

        assert cur_price > 190
