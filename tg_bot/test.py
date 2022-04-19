from time import sleep
from numpy import rint
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from yaml import DirectiveToken

url = 'https://codeforces.com/group/Af4KX7UJ7v/status?pageIndex=1&showUnofficial=true'
cookies = {'39ce7' : 'CFqyt6nt', '70a7c28f3de' : 'bgpsvuw00zd8bnezxg', 'JSESSIONID' : 'A6E73C12F13D980FE50E23F4921EDAB6-n1', 'X-User' : 'c4a6575810c2932b603136d5320acfa43af4d0b4b9028985910103a5f081fea9a758fefa79719321', 'X-User-Sha1' : '8b35649294a9cae17dc9cd95d61b66ba7cd45863'}

options = Options()
# options.add_argument('--headless')
# res = requests.(url)
driver = webdriver.Firefox(options=options)

driver.get(url)

username = driver.find_element_by_id("handleOrEmail")
password = driver.find_element_by_id("password")

username.send_keys("miha.tropin@gmail.com")
password.send_keys("fmshgavno2018")

sleep(2)

driver.find_element_by_class_name("submit").click()

sleep(2)

tables = pd.read_html(driver.page_source)
# tables 4


print(tables[4])
print(len(tables))

# driver.close()

# driver.add_cookie(cookies)


# print(driver.page_source)

# session = requests.session()
# page = session.post(url, cookies=cookies)
# print(page)
# page = session.get(url)
# page = session.post(url, auth = ('miha.tropin@gmail.com', 'fmshgavno2018'))
# page = session.get(url)
# tables = pd.read_html(page)
# print(page.text)

# for i in range(len(tables)):
#     print(tables[i])
# print(len(tables))
