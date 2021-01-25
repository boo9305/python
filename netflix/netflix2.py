import requests
import json
from lxml import html, etree
from bs4 import BeautifulSoup


#url = 'https://www.netflix.com/kr-en/title/81071970'
#url = 'https://www.netflix.com/kr/browse?jbv=81323551'
#url = 'https://www.netflix.com/kr/title/81362806'


def login(auth) :
    url = 'https://www.netflix.com/kr/login/'
    headers = { 
            'Accept-Encoding' : 'gzip, deflate, br',
            "Content-Type" : "application/x-www-form-urlencoded",
            "Accept-Language": 'q=0.9,ko-KR;q=0.8,ko',
            'Accept' : 'application/json, text/plain, */*',
            'Connection' : 'keep-alive',
            }
    #response = requests.get(url, headers=headers)
    #response = requests.get(url)
    response = requests.post(url , data={ 
        'userLoginId' : 'a1209114@naver.com' ,
        'password' : 'cksqja!@0610',
        'rememberMe' : 'false',
        'flow' : 'websiteSignup',
        'mode' : 'login',
        'action' : 'loginAction',
        'withFields' : 'userLoginId,password,rememberMe,nextPage,countryCode, countryIsoCode',
        'authUrl' : auth,
        'nextPage' : '',
        'countryCode' : '+82',
        'countryIsoCode' : 'KR',
    
        }, headers=headers)

    print(auth)
    print(response.url)
    print(response.status_code)

    print(response.text)


def getAuth():
    url = 'https://www.netflix.com/kr/login/'
    headers = { "Accept-Language": 'q=0.9,ko-KR;q=0.8,ko'}
    response = requests.get(url)
    etree = html.fromstring(response.text)
    return(list(set(etree.xpath("//input[@name='authURL']/@value")))[0])

#login()
token = getAuth();
login(token)





#data =soup.find('script', type='application/ld+json')


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
