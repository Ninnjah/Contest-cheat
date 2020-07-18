import subprocess
import time
import easyTui as tui
import os
import random
import webbrowser

os.system('mode con cols=33 lines=16')
os.system('color 0A')

webbrowser.register('Tor', None, webbrowser.BackgroundBrowser('C:/Users/{}/Desktop/TorBrowser/Browser/firefox.exe'.format(os.getlogin())))
tor = webbrowser.get('Tor')

#'https://stolicadetstva.com/competition/vote/47703/',
'''
links = ['https://stolicadetstva.com/competition/vote/47693/',
        'https://stolicadetstva.com/competition/vote/47714/',
        'https://stolicadetstva.com/competition/vote/47647/']
'''
links = ['https://stolicadetstva.com/competition/vote/47714/']

tui.title('Ща накрутим классов)')

try:
    n = int(input('Сколько классов намутим?   '))
except:
    print('ну раз ты ввел дич, то будем крутить 5 классов...')
    n = 5
    time.sleep(1)

print('\n')
classi = 0
tui.label('Крутим классы\n Яшка, Чупа коля, Пес белый')
for i in range(n):
    x = 0
    while x < len(links):
        #tor.open_new_tab(links[x-1])
        tor.open_new_tab('https://stolicadetstva.com/competition/vote/47714/')
        x += 1
        time = random.randint(50,65)
        while time > 0:
            tui.updatingScore('До закрытия браузера', time, 1)
            time -= 1
        subprocess.run(['TASKKILL', '/F', '/IM', 'firefox.exe'], stdout=subprocess.DEVNULL)
        classi += 1
        print('\a', end = '')


os.system('cls||clear')
tui.title('- - - Конец - - -')
tui.score('Классов намучено', classi)
exits = input('\r')