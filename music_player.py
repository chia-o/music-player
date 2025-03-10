from pygame import mixer
mixer.init()

mixer.music.load("Hot Hands.mp3")
mixer.music.set_volume(0.5)
mixer.music.play()

'''
The music_player.py script plays the music file You Stepped Out of a Dream.mp3.
'''

while True:
    print("Press 'p' to pause  \n'u' to unpause \n'v' to set volume \n'r' to restart  \n'e' to exit")

    player = input("What do you want to do?")

    if player == 'p':
        mixer.music.pause()
    elif player == 'u':
        mixer.music.unpause()
    elif player == 'v':
        volume = float(input("What volume do you want to set it at?"))
    elif player == 'r':
        mixer.music.rewind()
    elif player == 'e':
        mixer.music.stop()
        break