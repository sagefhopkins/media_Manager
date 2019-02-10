import socket as soc
import sys
import time

sock = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
server = ('localhost', 2222)
sock.connect(server)

def add(file):
    sock.send(('add').encode('utf-8'))
    time.sleep(1)
    sock.send(file.encode('utf-8'))

def stop():
    sock.send(('stop').encode('utf-8'))

def pause():
    sock.send(('pause').encode('utf-8'))

def play():
    sock.send(('play').encode('utf-8'))

def volume(vol):
    sock.send(('volume').encode('utf-8'))
    time.sleep(1)
    sock.send(vol.encode('utf-8'))


add('/home/sage/Dev/py/media_Manager/video.mp4')
time.sleep(1)
pause()
time.sleep(1)
volume('up')
time.sleep(1)
volume('down')
time.sleep(1)
play()
time.sleep(1)
stop()
