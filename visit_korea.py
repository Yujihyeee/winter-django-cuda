from bs4 import BeautifulSoup
from selenium import webdriver
import time

chromedriver = 'C:\\Users\\bitcamp\\PycharmProjects\\flaskProject\\data\\chromedriver.exe'


class VisitKorea(object):
    def __init__(self):
        driver = webdriver.Chrome(chromedriver)
        driver.implicitly_wait(3)
        driver.get('https://nid.naver.com/nidlogin.login')
        driver.implicitly_wait(3)

        driver.find_element_by_id('id_line').send_keys('coolbeat')
        driver.find_element_by_id('pw_line').send_keys('password')
        driver.find_element_by_id('log.login').click()
        driver.implicitly_wait(3)
        # driver.find_element_by_link_text('검색').click()


if __name__ == '__main__':
    VisitKorea()
