import subprocess

import pygame
pygame.init()


def shutdown():
    """
    завершение процессов и завершения работы 
    """
    subprocess.run(["shutdown"])


def voice(audio_file):

    song = pygame.mixer.Sound(audio_file)
    song.play()
