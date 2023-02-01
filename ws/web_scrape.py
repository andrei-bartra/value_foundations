# -*- coding: utf-8 -*-
'''
  _____________________________________________
 |                                             |
 | Webscrapping of REV Political Transcripts   |
 | Authors: - Andrei Batra                     |
 | Date: January, 2023                         |
 |_____________________________________________|


 =============================================================================
 Webscrapping of resume data from JNE website:
    https://www.rev.com/blog/transcript-category/political-transcripts/

Guide to run chrome from WSL:
    https://www.gregbrisebois.com/posts/chromedriver-in-wsl2/

 =============================================================================
'''


#  ________________________________________
# |                                        |
# |              1: Libraries              |
# |________________________________________|

#Basics
import os, sys

##selenium
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


#Other libraries
import time

#Local modules