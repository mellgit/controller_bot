import subprocess
from config import audio_file
import pygame
pygame.init()


def shutdown():
    """
    завершение процессов и завершения работы 
    """
    subprocess.run(["shutdown"])

def say_hello():

    song = pygame.mixer.Sound(audio_file)
    song.play()
