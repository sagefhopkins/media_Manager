import vlc
import mouse
import time



def video_Player(file):
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(file)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    time.sleep(2)
    mouse.mouse_Click(100, 100)

    while player.get_state() != 6:
        continue
