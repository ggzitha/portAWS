#!/usr/bin/env python3
import time
import json
import datetime
import random
import threading
import os
import subprocess

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


def printit():
    threading.Timer(5.0, printit).start()
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now. strftime("%H:%M:%S")

    datess = current_date
    timess = current_time
    tempss = (round(random.uniform(30,40),4))
    humss = (round(random.uniform(60,90), 4))
    barss = (round(random.uniform(30,40), 4))
    wind_nowss = (round(random.uniform(30,40), 4))
    wind_maxss = (round(random.uniform(30,40), 4))
    wind_dirss = (round(random.uniform(30,40), 4))
    rain_nowss = (round(random.uniform(30,40), 4))
    day_rainss = (round(random.uniform(30,40), 4))
    radss = (round(random.uniform(30,40), 4))
    battss = (round(random.uniform(95,100)))
    Sgn_strss = (round(random.uniform(30,40)))
    
    
    data_arrays = {"dates": datess, "times": timess, "temperature": tempss,
                "humidity": humss, "pressure": barss, "windspeed": wind_nowss,
                "windspeedMAX": wind_maxss, "windDir": wind_dirss, "rain": rain_nowss,
                "dailyRain": day_rainss, "radiation": radss, "battery": battss, "signal": Sgn_strss,}
                
    with open('/home/pi/Desktop/Read/data_Lora.json', 'w') as json_file:
        json.dump(data_arrays, json_file)
    with open('/home/pi/Desktop/Read/gh-pages/data_Lora.json', 'w') as json_file:
        json.dump(data_arrays, json_file)    
    with open('/var/www/html/data_Lora.json', 'w') as json_file:
        json.dump(data_arrays, json_file)

    print(data_arrays)

    with cd("~/Desktop/Read/"):
        subprocess.call(["git", "add", "."], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        subprocess.call(["git", "commit", "-m", "\"initial commit\""])
        subprocess.call(["git", "push", "-u", "--force" , "origin", "master"])

printit()
