import pygsheets

class Users_data():
    gc = pygsheets.authorize()
    sh = gc.open('ШК регистрация на курс')
    wks = sh.sheet1

    def get_column(self, char):
        lst = []
        for i in range(2, 200):
            data = self.wks.cell(char + str(i)).value
            if data == "":
                break
            lst.append(data)
        return lst

    def get_cf_handles(self):
        return self.get_column('C')

    def get_tg_handles(self):
        return self.get_column('D')

    def get_cf_handle_by_tg(self, tg_handle):
        cf = self.get_cf_handles()
        tg = self.get_tg_handles()

        row = tg.index(tg_handle)
        return str(cf[row])


    def is_user_registered(self,tg_handle):
        tg_handles = self.get_tg_handles()
        return tg_handles.count(tg_handle) == 1




# Open spreadsheet and then worksheet


