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
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'
with SB(uc=True, test=True,locale=f"{language_code.upper()}") as iony:
    iony.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    iony.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )
    #iony.set_window_size(resolution.width, resolution.height)
    #"#live-channel-stream-information"
    url = "https://kick.com/brutalles"
    iony.uc_open_with_reconnect(url, 4)
    iony.sleep(4)
    iony.uc_gui_click_captcha()
    iony.sleep(1)
    iony.uc_gui_handle_captcha()
    iony.sleep(4)
    if iony.is_element_present('button:contains("Accept")'):
        iony.uc_click('button:contains("Accept")', reconnect_time=4)
    if iony.is_element_visible('#injected-channel-player'):
        iony2 = iony.get_new_driver(undetectable=True)
        iony2.uc_open_with_reconnect("https://www.twitch.tv/brutalles", 5)
        iony2.uc_gui_click_captcha()
        iony2.uc_gui_handle_captcha()
        iony.sleep(10)
        if iony2.is_element_present('button:contains("Accept")'):
            iony2.uc_click('button:contains("Accept")', reconnect_time=4)
        while iony.is_element_visible('#injected-channel-player'):
            iony.sleep(100)
        iony.quit_extra_driver()
    iony.sleep(1)
    if iony.is_element_present("#live-channel-stream-information"):
        url = "https://www.twitch.tv/brutalles"
        iony.uc_open_with_reconnect(url, 5)
        if iony.is_element_present('button:contains("Accept")'):
            iony.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            iony2 = iony.get_new_driver(undetectable=True)
            iony2.uc_open_with_reconnect("https://kick.com/brutalles", 5)
            iony.sleep(10)
            if iony2.is_element_present('button:contains("Accept")'):
                iony2.uc_click('button:contains("Accept")', reconnect_time=4)
            while iony.is_element_present("#live-channel-stream-information"):
                iony.sleep(100)
            iony.quit_extra_driver()
    iony.sleep(1)
