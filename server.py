import socket as soc
import vlc_Controller as vlc
import time

con = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
con.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR, 1)

con.bind(('0.0.0.0', 2222))
con.listen(1024)

while True:
    client, address = con.accept()
    while True:
        data = client.recv(1024).decode('utf-8')
        print(data)
        if data:
            if data == 'add':
                data = client.recv(1024).decode('utf-8')
                vlc.add(data)
            elif data == 'pause':
                vlc.pause()
            elif data == 'stop':
                vlc.stop()
            elif data == 'enqueue':
                data = client.recv(1024).decode('utf-8')
                vlc.enqueue(data)
            elif data == 'volume':
                data = client.recv(1024).decode('utf-8')
                if data == 'up':
                    vlc.volume('up')
                elif data == 'down':
                    vlc.volume('down')
                elif data == 'off':
                    vlc.volume('off')
                elif data == 'on':
                    vlc.volume('on')
            elif data == 'next':
                vlc.next()
            else:
                continue
        else:
            continue
