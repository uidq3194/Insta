from time import sleep
from InstagramAPI import InstagramAPI

user = input('Username : ')
password = input('Password : ')
api=InstagramAPI(user,password)
api.login()

'''
-------------------------------
---------FOLLOW--------------
-------------------------------

'''