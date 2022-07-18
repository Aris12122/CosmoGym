import pygsheets
import numpy as np

gc = pygsheets.authorize()

# Open spreadsheet and then worksheet
sh = gc.open('ШК регистрация на курс')
wks = sh.sheet1

def get_column(char):
    lst = []
    for i in range(2, 200):
        data = wks.cell(char + str(i)).value
        if data == "":
            break
        lst.append(data)
    return lst

def get_cf_handles():
    return get_column('C')

def get_tg_handles():
    return get_column('D')