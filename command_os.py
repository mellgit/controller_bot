from itertools import count
import os
import sys
from config import audio_file

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



    song = pygame.mixer.Sound(audio_file)
    # clock = pygame.time.Clock()
    song.play()
    # while True:
    #     clock.tick(60)
    # pygame.quit()
