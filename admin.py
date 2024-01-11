import sqlite3

from os import path


ROOT = path.dirname(path.relpath((__file__)))


def create_post(Firstname, Lastname, username, password, confirm_password):
     connection = sqlite3.connect(path.join(ROOT, 'm_data.db'))
     cursor = connection.cursor()
     cursor.execute('insert into user (Firstname, Lastname, username, password, confirm_password) values (?,?,?,?,?)', (Firstname, Lastname, username, password, confirm_password))
     connection.commit()
     connection.close()



def get_posts():
     connection = sqlite3.connect(path.join(ROOT, 'm_data.db'))
     cursor = connection.cursor()
     cursor.execute('select * from user')
     posts = cursor.fetchall()
     
     return posts
