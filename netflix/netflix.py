import requests
import json
from bs4 import BeautifulSoup

#url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
#url = 'https://www.netflix.com/browse/genre/839338?jbv=81330889'


gerne_movie = 34399
gerne_tv = 83
korea_movie = 5685

url = 'https://www.netflix.com/browse/genre/34399'
response = requests.get(url)
headers = { "Accept-Language": 'q=0.9,ko-KR;q=0.8,ko'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
data =soup.find('script', type='application/ld+json')

l = []
for el in json.loads(data.string)['itemListElement'] :
    item = el['item']
    d = {}
    d['name'] = item['name']
    d['url'] = item['url']
    print(d)




#for i in range(0,1000):
#    num = 80180169 + i
#    url = 'https://www.netflix.com/kr-en/title/' + str(num)
#    response = requests.get(url)
#
#    if response.status_code == 200 :
#        soup = BeautifulSoup(response.text, 'html.parser')
#        print(num , soup.title)
#    else :
#        print(response.status_code)
