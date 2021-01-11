import sys, time, atexit, json
import settings

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pyvirtualdisplay import Display

gerne_movie = 34399
gerne_tv = 83
korea_movie = 5685

class Parser():
    driver = None;
    display = None;
    
    movie_genre_url = 'https://www.netflix.com/kr/browse/genre/34399'
    movie_korea_url = 'https://www.netflix.com/kr/browse/genre/5685'
    tv_germe_url    = 'https://www.netflix.com/kr/browse/genre/83'

    contents_list = []

    def __init__(self):
        self.display = Display(visible=0, size=(1024,768))
        self.display.start()
    
        self.driver = webdriver.Chrome('../lib/chromedriver')
        self.driver.implicitly_wait(50)
    def __del__(self):
        print('delete chrome')
        self.driver.close()
        self.display.stop()

    def run(self):
        self.get_contents_list()
        self.login()

    def login(self):
        ## 1. move start url
        url = 'https://www.netflix.com/kr/'
        self.driver.get(url=url)
        print(self.driver.current_url)
        
        ## 2. move login url
        login_btn = self.driver.find_element_by_class_name('authLinks')
        login_btn.click();
        print(self.driver.current_url)
        
        ## 3. login
        id = self.driver.find_element_by_name('userLoginId')
        pw = self.driver.find_element_by_name('password')

        id.send_keys(settings.ID)
        pw.send_keys(settings.PW)
        pw.submit()
        
        for i in range(1,200):
            time.sleep(1)
            if self.driver.current_url == 'https://www.netflix.com/browse':
                break;
        ## 4. move profile select url
        print(self.driver.current_url)
        profile_link = self.driver.find_element_by_class_name('profile-link')
        profile_link.click()

    def search_contents_detail(self):
        for item in self.contents_list:
            self.driver.get(url=item['url'])
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            print(soup.p)

    def search_contents_list(self):
        ## move netfilx movie genre url
        self.driver.get(url=self.movie_korea_url)
        print(self.driver.current_url)

        ## get movie list by BeautifulSoup 
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        data =soup.find('script', type='application/ld+json')
        for el in json.loads(data.string)['itemListElement'] :
        #    print(el)
            item = el['item']
            d = {}
            d['name'] = item['name']
            d['url'] = item['url']
            self.contents_list.append(d)
        return self.contents_list;

if __name__ == '__main__':
    tool = Parser();

    tool.search_contents_list()
    tool.login()
    tool.search_contents_detail()
