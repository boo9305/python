from selenium import webdriver
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1024,768))
display.start()
path = '../lib/chromedriver'
browser=webdriver.Chrome(path)
browser.get('https://www.netflix.com/kr/login')

id= browser.find_element_by_name('userLoginId')
pw = browser.find_element_by_name('password')

id.send_keys("a1209114@naver.com")
pw.send_keys('cksqja!@0610')

print(id)
print(pw)
print(browser.current_url)

pw.submit()

print(browser.current_url)

print(browser.title)


browser.quit()
