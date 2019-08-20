# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:42:03 2019

@author: Bhavya kala
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Firefox()
url="https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.aspx?expandable=6&scripcode=512289&flag=sp&Submit=G"
driver.get(url)
date = driver.find_element_by_id("ContentPlaceHolder1_txtFromDate")
search = driver.find_element_by_id("ContentPlaceHolder1_smartSearch")
search.clear()
search.send_keys("ANDHRAPET")
search.send_keys(Keys.RETURN)
driver.find_element_by_id("ContentPlaceHolder1_btnSubmit").click()

