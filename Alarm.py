import time
import datetime as dt
import pygame
file = (r'C:\Python\Kizz-Daniel-My-G-(JustNaija.com).mp3')

# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load(file)
# pygame.mixer.music.play()
# time.sleep(10)
# pygame.mixer.music.stop

while True:
    tm = dt.datetime.now()
    if tm.strftime("%I") == "01" and tm.strftime("%M") == "10" and tm.strftime("%S") == "00" and tm.strftime("%p") == "PM":
        print("Its time to play.")

        pygame.init()
        pygame.mixer.music.load(file)

        pygame.mixer.music.play()

        time.sleep(10)

        # Stop the music
        pygame.mixer.music.stop()

        # Quit pygame
        pygame.quit()