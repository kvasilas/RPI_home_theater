# RPI_home_theater
Code use as a home theater.

Originally intended on being run with a raspberry pi.  Will be ran on an andriod tv box that boots peppermint or ubuntu.  

## Ideas
- boot up on start and is a file on the home screen
- 3d print case and attach it to ceiling
- get wireless mouse and keyboard.
- maybe add light controls to it?
- use pypy3 it compiles so startup will be slow but runtime will be good!  especially useful if i dont use it as a computer

## Media paths
Mian applications already intergrated
- amazon prime
- netflix
- youtube
- xbox
- wii

others
- Hulu (search)
- Sonos
- Spotify
- Prime music
- Crackle (search)
- Disney+
- ...  media

## Other Ideas
for xbox/ wii use an hdmi switcher, break apart and then attach wires to the leads and buttons.  Use arduino/ arduino nano to control the switcher.  The cycle breakdown and flow chart is in the code

search bar to look for a specific title ie: firestick - intergrate the loading screen in

partical app intergration as a phone based mobile remote

l1 = QLabel(self)

run python on boot kodi
https://forum.kodi.tv/showthread.php?tid=283268

have script poll the device to decide aspect sizes.

winscp, free file transfer

add another box to serve as "other menu"
include:
- others (above)
- app settings

use vscode and PlatformIO for the arduino

## In order to run PyQt5 on Raspberry pi use:

- sudo apt-get update
- sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
