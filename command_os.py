from itertools import count
import os
import sys

import pygame
pygame.init()


def kill_and_shutdown():
    """
    завершение процессов и завершения работы 
    """
    program_list = [
        "gedit",
        "code",
        "google",
        "telegram-desktop"
    ]

    for elem in program_list:

        try:
            os.system(f"killall {elem}")

        except Exception as exp:
            print(exp)
            continue
        finally:
            os.system("shutdown now")


def voice():
    # song = pyglet.media.load('/home/mell/documents/voice_assist/hello_new.mp3')
    # song.play()
    # pyglet.app.run()
    # pyglet.app.exit()

    ln_file = '/home/mell/documents/voice_assist/hello_new.mp3'

    song = pygame.mixer.Sound(ln_file)
    # clock = pygame.time.Clock()
    song.play()
    # while True:
    #     clock.tick(60)
    # pygame.quit()
