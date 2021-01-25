import sys, time, atexit, json

from selenium import webdriver

from pyvirtualdisplay import Display

class Parser():
    driver = None;
    display = None;
    def __init__(self):
        self.display = Display(visible=0, size=(1024,768))
        self.display.start()
    
        self.driver = webdriver.Chrome('../lib/chromedriver')
        self.driver.implicitly_wait(50)
    def __del__(self):
        print('delete chrome')
        self.driver.close()
        self.display.stop()
