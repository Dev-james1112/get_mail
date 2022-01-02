from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
from bs4 import BeautifulSoup
import pandas as pd
import os
# -*- encoding: utf-8 -*-
driver = webdriver.Chrome("{}/chromedriver.exe".format(str(os.getcwd())))

driver.get("https://nid.naver.com/nidlogin.login")

pyperclip.copy(input('네이버 아이디: '))
driver.find_element_by_name('id').send_keys(Keys.CONTROL, 'v')
time.sleep(0.5)
pyperclip.copy(input('네이버 비밀번호'))
driver.find_element_by_name('pw').send_keys(Keys.CONTROL, 'v')
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="log.login"]').click()

driver.get('https://mail.naver.com/')
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

title_list = soup.find_all('strong', 'mail_title')
csv_list = [['','']]

for title in title_list:
    csv_list.append(['',title.text[6:-1]])
csv = pd.DataFrame(csv_list)

csv.columns=['','메일제목']
try:
    csv.to_csv("{}\메일\mail {}.csv".format(os.getcwd(), time.strftime('%Y-%m-%d', time.localtime(time.time()))), index=False, encoding='cp949')

except:
    pass