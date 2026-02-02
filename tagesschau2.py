#!/usr/bin/python3
# offene Fragen: Shebang erforderlich ? 
# script executabele machen mit: "chmod  +x tagesschaue.py" <- im richtigen Verzeichnis
# Job erstellen: "sudo crontab -e"
# Hier nun folgende Zeile eintippen:
# ""

import webbrowser
import time
import os

time.sleep(60)

url = "https://www.tagesschau.de/sendung/tagesschau/"
## aktuellerer Link aber der alte geht trotzdem
## url = "https://www.tagesschau.de/multimedia/sendung/tagesschau_20_uhr"

# Browser pfad registrieren
firefox_path = "/usr/bin/firefox"#
# chrome_path = "/usr/bin/chromium-browser"

webbrowser.register("firefox", None, webbrowser.BackgroundBrowser(firefox_path) )
# webbrowser.register("chromium-browser", None, webbrowser.BackgroundBrowser(chrome_path) )

firefox = webbrowser.get(using='firefox')
# chrome = webbrowser.get(using='chromium-browser')

time.sleep(20)

# und nun die tagesschau
# chrome.open(url, new = 2)
firefox.open(url, new = 2)
# webbrowser.open(url, new=2)
time.sleep(30)

# mini raspi display mit 800 x 480
os.system("xdotool mousemove 225 450")        

# start video
os.system("xdotool click 1")
time.sleep(5)

# maximieren
os.system("xdotool key f")

