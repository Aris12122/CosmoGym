from audioop import add
from cgitb import handler
from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By




from numpy import rint
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from yaml import DirectiveToken

url = 'https://codeforces.com/group/Af4KX7UJ7v/contest/256152/status'
# cookies = {'39ce7' : 'CFqyt6nt', '70a7c28f3de' : 'bgpsvuw00zd8bnezxg', 'JSESSIONID' : 'A6E73C12F13D980FE50E23F4921EDAB6-n1', 'X-User' : 'c4a6575810c2932b603136d5320acfa43af4d0b4b9028985910103a5f081fea9a758fefa79719321', 'X-User-Sha1' : '8b35649294a9cae17dc9cd95d61b66ba7cd45863'}

options = Options()
# options.add_argument('--headless')
# res = requests.(url)
driver = webdriver.Firefox(options=options)

driver.get(url)

# username = driver.find_element_by_id("handleOrEmail")
# password = driver.find_element_by_id("password")

# username.send_keys("miha.tropin@gmail.com")
# password.send_keys("fmshgavno2018")

# sleep(2)






# sleep(2)


# tables 4

def is_solved(handle):

    def select_value(id, value):
        select = Select(driver.find_element(By.ID, id))
        select.select_by_value(value)

    def add_participant(handle):
        participant = driver.find_element(By.ID, "participantSubstring")
        participant.send_keys("^" + handle + "$")


    select_value("frameProblemIndex", "A")
    select_value("verdictName", "OK")

    add_participant(handle)

    driver.find_element(By.CSS_SELECTOR, ".status-filter > div:nth-child(4) > input:nth-child(1)").click()

    tables = pd.read_html(driver.page_source)
    name = tables[2].loc[0, "Who"]
    # print(name)
    return handle == name

# print(is_solved("Aris"))

# print(len(tables))

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



# url = "https://codeforces.com/group/Af4KX7UJ7v/contest/263168/status"

# req = requests.get(url)
# html = BeautifulSoup(req.content, 'html.parser')

# tables = pd.read_html(url)
# print(tables[0])

# # filter = html.find("div", id="participantSubstring")

# html.find("""<div class="setting-name" </div>""")["value"] = "^Aris$"


# tables = pd.read_html(html)
# print(tables)