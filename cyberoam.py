# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 00:37:31 2018

@author: hp
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Firefox()
url="https://172.16.1.1:8090/httpclient.html?u=http://www.msftconnecttest.com/redirect"
driver.get(url)
username = driver.find_element_by_name("username")
password1 = driver.find_element_by_name("password")
username.send_keys("")
password1.send_keys("")
driver.find_element_by_id("logincaption").click()
driver.quit()
"""
https://dopagent.indiapost.gov.in/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&__FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=3&BANK_ID=DOP&AGENT_FLAG=Y

user id - DOP.MI4520050100036
Password- kala841937#
"""


