import pandas as pd
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = 'https://codeforces.com/group/Hs4XCEVg60/members'

links = {
    "group_members": "https://codeforces.com/group/Af4KX7UJ7v/members"
}


contests = {
    0: "https://codeforces.com/group/Hs4XCEVg60/contest/394997/status",
    1: "https://codeforces.com/group/Hs4XCEVg60/contest/395950/status",
    2: "https://codeforces.com/group/Hs4XCEVg60/contest/395952/status",
    3: "https://codeforces.com/group/Hs4XCEVg60/contest/394972/status",
    4: "https://codeforces.com/group/Hs4XCEVg60/contest/401822/status",
    5: "https://codeforces.com/group/Hs4XCEVg60/contest/395824/status",
    6: "https://codeforces.com/group/Hs4XCEVg60/contest/395623/status",
}

options = Options()
options.add_argument("--headless")


def is_in_group(handle):
    driver = webdriver.Firefox(options=options)
    
    try:
        driver.get(links["group_members"])
        tables = pd.read_html(driver.page_source)
        members = tables[1]["Member"]
        driver.close()
        return members.str.contains(handle).any()
    except Exception as e:
        driver.close()
        print('An exception occurred' + str(e))
        

def select_value(driver, id, value):
    select = Select(driver.find_element(By.ID, id))
    select.select_by_value(value)


def add_participant(driver, handle):
    participant = driver.find_element(By.ID, "participantSubstring")
    participant.send_keys("^" + handle + "$")


def is_solved(contest_id, problem_id, handle):

    driver = webdriver.Firefox(options=options)
    name = ""
    
    try:
        driver.get(contests[contest_id])
        
        select_value(driver, "frameProblemIndex", problem_id)
        select_value(driver, "verdictName", "OK")

        add_participant(driver, handle)

        driver.find_element(By.CSS_SELECTOR, ".status-filter > div:nth-child(4) > input:nth-child(1)").click()

        tables = pd.read_html(driver.page_source)
        name = tables[2].loc[0, "Who"].split('\n')[0]
        # print("Name: " + name)

    except Exception as e:
        print("An exception occurred while checking CF.is_solved " + handle)
        print(str(e))
    driver.close()

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