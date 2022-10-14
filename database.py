import cmd
from tkinter import simpledialog
from database import init_database

class VaultMethods:

    def __init__(self):
        self.db, self.cursor = init_database ()

    def popup_entry(self, heading):
        answer = simpledialog.askstring("Enter Details", heading)
        return answer

    def add_password(self, vaultscreen):
        platform = self.popup_entry ("Platform")
        userid = self.popup_entry ("Username")
        password = self.popup_entry ("Password")

        insert_cmd = "INSERT INTO vault (Platform, Userid, Password)\n VALUES(?, ?, ?)"

        self.cursor.execute (insert_cmd, (platform, userid, password))
        self.db.commit()
        vaultscreen()


