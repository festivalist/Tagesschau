import webbrowser
import time
import os

# test 2

#url = "https://www.tagesschau.de/multimedia/letzte-sendung"
#url = "https://www.tagesschau.de/sendung/letzte-sendung"
url = "https://www.tagesschau.de/sendung/tagesschau/"
#url = "https://youtu.be/IP5844MsRvA"

url2 = "https://open.spotify.com/playlist/22gmanYjT7U1QdXaBsN8Lx?si=Gn4Xav6HQFSwAKvr5QlOQw&dl_branch=1&nd=1"

firefox = webbrowser.get(using='firefox')
chrome = webbrowser.get(using='chromium-browser')

time.sleep(20)
# start the magic
## new update 
## firefox.open(url, new = 2)
## time.sleep(10)

# start spotify
chrome.open(url2, new = 2)

# wait
time.sleep(25)

# start music
os.system("xdotool key space")

# stop music and start Tagesschau if aufnahmefähig == True
time.sleep(60)
os.system("xdotool key space")

# und nun die tagesschau
firefox.open(url, new = 2)
time.sleep(10)

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
        os.system("xdotool mousemove 950 450")
        time.sleep(2)
        os.system("xdotool click 1")
        time.sleep(7)
        os.system("xdotool mousemove 1050 450")
        os.system("xdotool click 1")
        os.system("xdotool click 1")
        #time.sleep(3)
        time.sleep(960)
        chrome.open(url2, new = 2)
        time.sleep(25)
        os.system("xdotool mousemove 900 200")
        os.system("xdotool click 1")
        os.system("xdotool key space")
