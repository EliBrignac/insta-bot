
from instabot import Bot
import os
import shutil

#Make directory a raw string or use \\ instead of \
def post_image(username, password, directory, caption):
    bot = Bot()
    bot.login(username= username, password= password)
    bot.upload_photo(directory + '\\' + str(os.listdir(directory)[0]), caption= caption)
    os.remove(directory + '\\' + str(os.listdir(directory)[0]))
    shutil.rmtree("\\config")

#make directory of the one in AWS
directory = r'C:\Users\Eli Brignac\OneDrive\Pictures\TonyStark'

post_image('daily_tony_stark', '********', directory, 'Your Daily Tony Stark Picture')

shutil.rmtree(r"C:\Users\Eli Brignac\PycharmProjects\Labratory\config")
