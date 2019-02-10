import os
import time


#Defintes all controlling functions required for socket server to manager vlc instance
def add(file):
    os.system('python vlc_Server.py localhost:4212 add ' + file)

def pause():
    os.system('python vlc_Server.py localhost:4212 pause')

def play():
    os.system('python vlc_Server.py localhost:4212 play')

def stop():
    os.system('python vlc_Server.py localhost:4212 stop')

def enqueue(file):
    os.system('python vlc_Server.py localhost:4212 enqueue ' + file)

def rewind():
    os.system('python vlc_Server.py localhost:4212 rewind')

def next():
    os.system('python vlc_Server.py localhost:4212 next')

def prev():
    os.system('python vlc_Server.py localhost:4212 prev')

def clear():
    os.system('python vlc_Server.py localhost:4212 clear')

def loop():
    os.system('python vlc_Server.py localhost:4212 loop')

def repeat():
    os.system('python vlc_Server.py localhost:4212 repeat')

def random():
    os.system('python vlc_Server.py localhost:4212 random')

def volume(vol):
    if vol == 'up':
        os.system('python vlc_Server.py localhost:4212 volup 5')
    elif vol == 'down':
        os.system('python vlc_Server.py localhost:4212 voldown 5')
    elif vol == 'off':
        os.system('python vlc_Server.py localhost:4212 volume 0')
    elif vol == 'on':
        os.system('python vlc_Server.py localhost:4212 volume 50')


"""
add('/home/sage/Dev/py/media_Manager/video.mp4')
time.sleep(2)
pause()
time.sleep(1)
play()
time.sleep(2)
stop()
"""
