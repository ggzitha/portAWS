#!/usr/bin/env python3
import time
import serial
import json
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


ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

while 1:
        x=ser.readline()
        if x != b'' or x != b"" :
            try:
                x_decoded=x.decode('utf-8')
            except UnicodeDecodeError:
                continue
            
            x_parsing = x_decoded.split('\'')
            lora_parsing = x_parsing[1].split(',')
            first_lora = lora_parsing[0]
            Signal_str = x_parsing[2][0:14]

            if len(first_lora) == 15 :
                final_array = first_lora[5:15], lora_parsing[1:12], Signal_str

                datess = first_lora[5:15]
                timess = lora_parsing[1]
                tempss = lora_parsing[2]
                humss = lora_parsing[3]
                barss = lora_parsing[4]
                wind_nowss = lora_parsing[5]
                wind_maxss = lora_parsing[6]
                wind_dirss = lora_parsing[7]
                rain_nowss = lora_parsing[8]
                day_rainss = lora_parsing[9]
                radss = lora_parsing[10]
                battss = lora_parsing[11]
                Sgn_strss = Signal_str

                data_arrays = {"dates": datess, "times": timess, "temperature": tempss,
                "humidity": humss, "pressure": barss, "windspeed": wind_nowss,
                "windspeedMAX": wind_maxss, "windDir": wind_dirss, "rain": rain_nowss,
                "dailyRain": day_rainss, "radiation": radss, "battery": battss, "signal": Sgn_strss,}

                with open('/home/pi/Desktop/Read/data_Lora.json', 'w') as json_file:
                    json.dump(data_arrays, json_file)

                with open('/var/www/html/data_Lora.json', 'w') as json_file:
                    json.dump(data_arrays, json_file)
                with open('/home/pi/Desktop/Read/data_Lora.json', 'w') as json_file:
                    json.dump(data_arrays, json_file)
                with open('/home/pi/Desktop/Read/gh-pages/data_Lora.json', 'w') as json_file:
                    json.dump(data_arrays, json_file)
                with open('/var/www/html/data_Lora.json', 'w') as json_file:
                    json.dump(data_arrays, json_file)
                
                print(final_array)
                with cd("~/Desktop/Read/"):
                    subprocess.call(["git", "add", "."], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    subprocess.call(["git", "commit", "-m", "\"initial commit\""])
                    subprocess.call(["git", "push", "-u", "origin", "master"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)