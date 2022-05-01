import subprocess
import alsaaudio
import pygame



def shutdown():
    """
    завершение процессов и завершения работы 
    """
    subprocess.run(["shutdown"])


def voice(audio_file):
    pygame.init()
    song = pygame.mixer.Sound(audio_file)
    song.play()

def mixer(status=None):

    mix = alsaaudio.Mixer()  # инициализируем объект микшера
    vol = mix.getvolume()  # получили текущую громкость

    if status == None:
    
        if vol == [0, 0]:
            mix.setvolume(40)  # теперь пусть динамики поорут :) - установим громкость 90
            return f"звук на 40"
        else:
            mix.setvolume(0)
            return "без звука"
    
    elif status == "+":
        if vol != [100, 100]:
            vol = [elem+10 for elem in vol]
            mix.setvolume(vol[0])
            return f"звука на {vol[0]}"

    elif status == "-":
        if vol != [0, 0]:
            vol = [elem-10 for elem in vol]
            mix.setvolume(vol[0])
            return f"звука на {vol[0]}"
