import time
import os
import re

#os.system("mode con cols=width lines=height")
#os.system('color 0A')  0 - BACKGROUND, A - TEXT
#
#   COLORS
#
# 0 = BLACK     8 = GRAY
# 1 = BLUE      9 = BRIGHT-BLUE
# 2 = GREEN     A = BRIGHT-GREEN
# 3 = CYAN      B = BRIGHT-CYAN
# 4 = RED       C = BRIGHT-RED
# 5 = PURPLE    D = BRIGHT-PURPLE
# 6 = YELLOW    E = BRIGHT-YELLOW
# 7 = WHITE     F = BRIGHT-WHITE
#

def title(title):
    length = len(title) + 6
    titlestr = '=' * length + '\n-- ' + title + ' --\n' + '=' * length
    print(titlestr)

def label(label):
    length = len(label) + 6
    print('\n')
    print(' ', label)
    print('-' * length)

def score(name, score):
    length = len(name) + len(str(score)) + 10
    print('\n', name, ': ', score, '  ')
    print('-'* length)

def updatingScore (name, score, freq):
    print(name, ': ', score, '  ', end='\r')
    time.sleep(freq)
    
def ul(options):
    for i in options:
        print('  -', i)
    print('-' * 24)

def ol(options):
    num = 0
    for i in options:
        print('  [' + str(num) + ']', i)
        num += 1
    print('-' * 24)

ol(['Text Sample', '2 Sample', '3 Sample'])