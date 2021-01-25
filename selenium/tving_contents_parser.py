import sys, time, atexit, json, requests
import settings

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pyvirtualdisplay import Display

from parser import Parser


class TvingParser(Parser):
    main_url = 'https://www.tving.com/vod/genre'

    contents_list = []
    
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__()
    
    def login(self):
        ## 1. move start url
        self.driver.get(url='https://user.tving.com/pc/user/login.tving?returnUrl=https%3A%2F%2Fuser.tving.com%2Fpc%2Fuser%2Flogin.tving')
        print(self.driver.current_url)
        
        ## 2. login
        id = self.driver.find_element_by_id('a')
        pw = self.driver.find_element_by_id('b')

        id.send_keys('zoflr9305')
        pw.send_keys('qls0926!')
        sm = self.driver.find_element_by_id('doLoginBtn')
        sm.click()
        time.sleep(1) 
        print(self.driver.current_url)

        profile = self.driver.find_element_by_class_name('profile-icon')
        profile.click()
        time.sleep(1) 
        print(self.driver.current_url)
         

    def search_contents_detail(self):
        for item in self.contents_list:
            self.driver.get(url=item['url'])
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            print(soup.p)


    def search_contents_list(self):
        self.driver.get(url=self.main_url)
        pheight = self.driver.execute_script('return document.body.scrollHeight')
        nheight = 0 ;
        print(self.driver.current_url)

        # scrolling ...
        while pheight != nheight:
            print('doing scrolling %d' % nheight)
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(0.3)
            pheight = nheight
            nheight = self.driver.execute_script('return document.body.scrollHeight')
        items = self.driver.find_elements_by_class_name('program-item__info')

        link_list = []

        # get url list        
        print('getting url list')
        total = 0
        for item in items:
            item_a = item.find_element(By.TAG_NAME, 'a')
            a = item_a.get_attribute('href')
            link_list.append(a)
            total += 1;
            item_a = None;

        # write logfile about content 
        f = open('./logfile', 'w')
        for idx, item in enumerate(link_list):
            print('running... %s \t %d/%d' % (item, idx, total))
            content_dic = {}

            self.driver.get(url=item)
            try :
                content_dic['title'] = self.driver.find_element_by_class_name('title').text
            except :
                pass
            try :
                summary = self.driver.find_element_by_class_name('summary').text
            except :
                pass
            try :
                content_dic['genre'] = self.driver.find_element_by_class_name('under').text
            except :
                pass
            
            try :
                dds = self.driver.find_elements_by_tag_name('dd')
                c = 0;
                actor = ""
                director = ""
                for idx2, dd in enumerate(dds):
                    if idx2 == 1:
                        content_dic['actor'] = dd.text
                    elif idx2 == 2:
                        content_dic['director'] = dd.text
            except:
                pass;
            
            content_dic['url'] = item
            f.write(str(content_dic) + "\n")
        f.close()
            
        ## move netfilx movie genre url
        #self.driver.get(url=self.movie_korea_url)
        #print(self.driver.current_url)

        ## get movie list by BeautifulSoup 
        #soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        #data =soup.find('script', type='application/ld+json')
        #for el in json.loads(data.string)['itemListElement'] :
        ##    print(el)
        #    item = el['item']
        #    d = {}
        #    d['name'] = item['name']
        #    d['url'] = item['url']
        #    self.contents_list.append(d)
        #return self.contents_list;


    def test(self):
        self.driver.get(url='https://www.tving.com/movie/player/M000331735')
        print(self.driver.current_url)
        title = ""
        try :
            dt = self.driver.find_elements_by_css_selector('.info > dt')
            dt_dd = self.driver.find_elements_by_css_selector('.info > dt ~ dd')

            print("??")
            for idx, xx in enumerate(dt) :
                print('%s : %s ' %(dt[idx].text, dt_dd[idx].text))

        except :
            print("error")
        
        genre = ""
        try :
            genre = self.driver.find_element_by_class_name('under').text
        except :
            print("error")

        print(title, genre)

if __name__ == '__main__':
    tool = TvingParser();
    tool.test()
#    tool.login()
#    tool.search_contents_list()

