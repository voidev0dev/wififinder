import os
import random
import string
import threading

def generate_random_string(length):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

def connect_to_wifi(ssid, password=generate_random_string(length=random.randint(8, 30))):
        while True:
            try:
                os.system(f'nmcli d wifi connect "{ssid}" password "{password}"') 
                print(password)
                return True 
            
            except: 
                return False 

connect_to_wifi(ssid="TP-Link_9312")
