from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional
import requests
hex = "68747470733A2F2F7777772E7477697463682E74762F62727574616C6C6573"
tmp = bytes.fromhex(hex)
url = tmp.decode("utf-8")
hex1 = "68747470733A2F2F7777772E796F75747562652E636F6D2F4062727574616C6C65732F6C697665"
tmp1 = bytes.fromhex(hex1)
url1 = tmp1.decode("utf-8")
while True:
    with SB(uc=True, test=True,locale="en") as florence:
        rnd = random.randint(450,900)
        florence.uc_open_with_reconnect(url, 5)
        florence.sleep(15)
        if florence.is_element_present("#live-channel-stream-information"):
        
            if florence.is_element_present('button:contains("Accept")'):
                florence.uc_click('button:contains("Accept")', reconnect_time=4)
            if True:
                florence2 = florence.get_new_driver(undetectable=True)
                florence2.uc_open_with_reconnect(url, 5)
                florence2.sleep(10)
                if florence2.is_element_present('button:contains("Accept")'):
                    florence2.uc_click('button:contains("Accept")', reconnect_time=4)
                florence3 = florence.get_new_driver(undetectable=True)
                florence3.uc_open_with_reconnect(url1, 5)
                florence3.sleep(10)
                if florence3.is_element_present('button:contains("Accept")'):
                    florence3.uc_click('button:contains("Accept")', reconnect_time=4)
                    florence3.sleep(10)
                else:
                    florence3.sleep(10)
                    florence3.uc_gui_press_key('K')
                florence.sleep(rnd)
                florence.quit_extra_driver()
        else:
            break
