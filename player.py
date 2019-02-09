import numpy as np
import cv2

from ffpyplayer.player import MediaPlayer

def video_Player(file):
    cap = cv2.VideoCapture(file)
    audio = MediaPlayer(file)
    while(cap.isOpened()):
        ret, frame = cap.read()
        audio_frame, val = audio.get_Frame()
        cv2.imshow('frame', frame)
        if val != 'eof' and audio_frame is not None:
            img, t = audio_frame
        if cv2.waitKey(33) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
