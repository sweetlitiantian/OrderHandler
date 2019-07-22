#! usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import hashlib
def getCode1(md):

 driver =webdriver.Firefox()
 driver.maximize_window()
 driver.implicitly_wait(5)
 driver.get("https://www.cmd5.com/")      #打开网址
 driver.find_element_by_xpath("//*[@id=\"ctl00_ContentPlaceHolder1_TextBoxInput\"]").send_keys(md)
 driver.find_element_by_xpath("//*[@id=\"ctl00_ContentPlaceHolder1_Button1\"]").click()
 time.sleep(5)
 aa =driver.find_element_by_id('LabelAnswer').text
 driver.close()
 return aa


def getCode(dst):
 dst = dst.lower()
 print(dst)
 for a in range(0, 10):
  for b in range(0, 10):
   for c in range(0, 10):
    for d in range(0, 10):
     word = str(a) + str(b) + str(c) + str(d)
     tmp = hashlib.md5(word).hexdigest()
     if dst == tmp:
      return word
 return None



