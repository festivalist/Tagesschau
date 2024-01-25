# Tagesschau Wecker HowTO








unchecked autostart method:
We want to run our script automatically when the Raspberry Pi boots up. To do that we will be using a method called Autostart. With this method, the graphical interface will initialize first and then run our script.

Open the Terminal and type:

mkdir /home/pi/.config/autostart
nano /home/pi/.config/autostart/fearBooth.desktop
Now copy the contents below inside the file you've just created:

[Desktop Entry]
Type=Application
Name=HauntedTV
Exec=/usr/bin/python /home/pi/Desktop/FearBooth/main.py
save, exit with ctrl + x and reboot:
