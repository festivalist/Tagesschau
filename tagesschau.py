#!/usr/bin/python3
# offene Fragen: Shebang erforderlich ? 
# script executabele machen mit: "chmod  +x tagesschaue.py" <- im richtigen Verzeichnis
# Job erstellen: "sudo crontab -e"
# Hier nun folgende Zeile eintippen:
# ""

import webbrowser
import time
import os

url = "https://www.tagesschau.de/sendung/tagesschau/"
## aktuellerer Link aber der alte geht trotzdem
## url = "https://www.tagesschau.de/multimedia/sendung/tagesschau_20_uhr"

# url2 = "https://open.spotify.com/playlist/22gmanYjT7U1QdXaBsN8Lx?si=Gn4Xav6HQFSwAKvr5QlOQw&dl_branch=1&nd=1"
# url2 = "https://open.spotify.com/playlist/37i9dQZEVXbgZQZIKPaTJO"
# url2 = "https://open.spotify.com/station/playlist/37i9dQZF1DX6bBjHfdRnza"
url2 = "https://open.spotify.com/playlist/37i9dQZEVXbgZQZIKPaTJO"

firefox = webbrowser.get(using='firefox')
chrome = webbrowser.get(using='chromium-browser')

time.sleep(20)
# start the magic
## new update 
## firefox.open(url, new = 2)
## time.sleep(10)

# start spotify
## kein premium mehr
## chrome.open(url2, new = 2)

# wait
time.sleep(25)
# os.system("espeak 'Get up'")
# time.sleep(3)

# start music
## kein premium mehr
## os.system("xdotool key space")
## os.system("xdotool mousemove 310 560")
## time.sleep(1)
## os.system("xdotool click 1") 

# stop music and start Tagesschau if aufnahmefähig == True
# time.sleep(300)
# os.system("xdotool key space")
# time.sleep(1)
# os.system("xdotool key Control_L+w")
# time.sleep(2)
# os.system("espeak 'I said get up for fucks sake'")

# und nun die tagesschau
chrome.open(url, new = 2)
# firefox.open(url, new = 2)
time.sleep(25)

if url.count("yout") > 0:
        os.system("xdotool key f")
else:
    # no youtube no "f" == Fullscreen, so we maximize the browser and check afterwards
    #os.system("xdotool search --onlyvisible --class 'firefox' windowactivate")
    time.sleep(2)
    #os.system("xdotool key F11")
    time.sleep(4)
        
    if url.count("arte.tv") > 0:
        os.system("xdotool mousemove 1112 670")
        time.sleep(2)
        os.system("xdotool click 1") 
    elif url.count("tagesschau.de") > 0:
        
        # # full HD resolution
        # os.system("xdotool mousemove 950 450")
        
        # UWQHD resolution
        # os.system("xdotool mousemove 1700 580")

        
        ### time.sleep(2)
        ### os.system("xdotool click 1")
        ### time.sleep(7)
        
        # # Full HD Settings
        # os.system("xdotool mousemove 1050 450")
        
        # UWQHD Settings
        os.system("xdotool mousemove 1450 500")
        
        # mini raspi display mit 800 x 480
        
            
        os.system("xdotool click 1")
        os.system("xdotool click 1")
        #time.sleep(3)
        time.sleep(960)
        chrome.open(url2, new = 2)
        time.sleep(25)
        
        # # Full HD 
        # os.system("xdotool mousemove 900 200")
        
        # UWQHD resolution
        os.system("xdotool mousemove 1715 1375")
        
        os.system("xdotool click 1")
        # os.system("xdotool key space")
