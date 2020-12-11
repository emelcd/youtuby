#!/usr/bin/env python
# -*- coding: utf-8 -*-

import win32clipboard
from time import sleep
import os
from colorama import Fore, Back, Style, init
import random
import urllib.request
from zipfile import ZipFile
import shutil


try:
    open("./ffmpeg.exe")
except:
    print(Fore.RED+"DESCARGANDO ARCHIVOS PARA LA EXTRACCIÓN Y CONVERSIÓN DEL AUDIO")
    urllib.request.urlretrieve(
        "https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2020-12-10-12-59/ffmpeg-N-100388-g412c3b37a4-win64-gpl.zip", "ffmpeg.zip")

    with ZipFile('ffmpeg.zip', 'r') as zipO:
        zipO.extract('ffmpeg-N-100388-g412c3b37a4-win64-gpl/bin/ffmpeg.exe')
    shutil.move(
        '.\\ffmpeg-N-100388-g412c3b37a4-win64-gpl\\bin\\ffmpeg.exe', '.\\')
    shutil.rmtree('.//ffmpeg-N-100388-g412c3b37a4-win64-gpl')
    os.remove('ffmpeg.zip')

init()

os.system('cls')
clipis = ['#Start']
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText("#Start")
win32clipboard.CloseClipboard()

colors = [Fore.WHITE, Fore.YELLOW, Fore.RED, Fore.LIGHTBLUE_EX,
          Fore.LIGHTMAGENTA_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX]

youtube_logo = """
 ▄· ▄▌      ▄• ▄▌▄▄▄▄▄▄• ▄▌▄▄▄▄·  ▄· ▄▌
▐█▪██▌▪     █▪██▌•██  █▪██▌▐█ ▀█▪▐█▪██▌
▐█▌▐█▪ ▄█▀▄ █▌▐█▌ ▐█.▪█▌▐█▌▐█▀▀█▄▐█▌▐█▪
 ▐█▀·.▐█▌.▐▌▐█▄█▌ ▐█▌·▐█▄█▌██▄▪▐█ ▐█▀·.
  ▀ •  ▀█▄▀▪ ▀▀▀  ▀▀▀  ▀▀▀ ·▀▀▀▀   ▀ • 
"""

for char in youtube_logo:
    print(random.choice(colors) + char, end="")
    sleep(0.01)
print(Style.RESET_ALL)

while True:
    print("", end="\r")
    print(Fore.YELLOW, end="\r")
    sleep(1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    if data != clipis[-1] and "youtube" in data:
        clipis.append(data)
        win32clipboard.CloseClipboard()
    elif data == "fin" or data == "end" or data == "exit":
        break
    else:
        print(str(len(clipis) - 1) + " enlaces copiados", end="\r")
        win32clipboard.CloseClipboard()
print(Fore.LIGHTGREEN_EX)

folder = input(Fore.BLUE+"\nNombra la Carpeta: ").replace(" ", "_")
fs = open("%s.txt" % folder, "w+")
for clip in clipis:
    fs.write(clip+"\n")
fs.close()
os.system('mkdir %s' % folder)

menu_P = """
/*  o8ooooooooooooooooo8o  */
/* (_) """+Fore.LIGHTWHITE_EX+"""1.Son Vídeos"""+Fore.LIGHTGREEN_EX+"""    (_) */
/* (_) """+Fore.LIGHTWHITE_EX+"""2.Son Canciones"""+Fore.LIGHTGREEN_EX+""" (_) */
/*  O8ooooooooooooooooo8O  */
"""
lock = True
while lock:
    print(Fore.LIGHTGREEN_EX + menu_P)
    selection = input("\n")
    if selection == "2":
        os.system(
            'python -m youtube_dl -a %s.txt -x -i --audio-format "mp3" ' % folder)
        os.system('move *.mp3 ./%s' % folder)
        lock = False

    elif selection == "1":
        os.system(
            'python -m youtube_dl -a %s.txt -i -f "mp4" ' % folder)
        os.system('move *.mp4 ./%s' % folder)
        lock = False
    else:
        print("Pulse 1 o 2")

os.system('DEL %s.txt /F' % folder)
print(Fore.LIGHTMAGENTA_EX + "\nLA DESCARGA HA ACABADO\n")
