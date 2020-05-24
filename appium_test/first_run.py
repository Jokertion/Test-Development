#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: lms
@file: first_run.py
@time: 2020/5/23 10:04
@desc: 
"""
from appium import webdriver


desire_caps = dict()
desire_caps['platform'] = 'Android'
desire_caps['platformVersion'] = '6.0'
desire_caps['deviceName'] = 'emulator-5554'
desire_caps['appPackage'] = 'com.android.settings'
desire_caps['appActivity'] = 'com.android.settings.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desire_caps)
driver.quit()
