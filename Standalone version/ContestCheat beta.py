import requests
import webbrowser
from bs4 import BeautifulSoup
import easyTui as tui
import os
import time

os.system('mode con cols=64 lines=20')
os.system('color 0A')

def main(content):
    
    os.system('cls||clear')
    
    # Интерфейс
    tui.title('Крутильщик классов для децкава конкурса')
    tui.label('Что делать?')
    tui.ol(['Крутить классы', 'Собрать новый список прокси','Удалить список использованных прокси','Вывести список участников'])
    print('чтобы вернуться сюда введи число меньше нуля')
    com = input()
    try:
        com = int(com)
    except:
        print('Нужно ввести цифру от 0 до 3')
        time.sleep(2)
        main(content)

    if com == 0:
        tryToConnect(content)
    elif com == 1:
        proxyParser(content)
    elif com == 2:
        try:
            os.remove('usedproxy.txt')
        except:
            print('Список уже удален..')
            time.sleep(2)
            main(content)
    elif com == 3:
        members()
    else:
        print('Нужно ввести цифру от 0 до 3')
        time.sleep(2)
        main(content)

def tryToConnect(content):
    '''
    Подбор прокси из списка и попытка соединения с сервером
    '''
    os.system('cls||clear')
    try:
        with open('usedproxy.txt') as f:
            usedproxy = f.readlines()
        usedproxy = [x.strip() for x in usedproxy] 
    except:
        usedproxy = open('usedproxy.txt', 'x')
        usedproxy.close()
    usedproxyfile = open('usedproxy.txt', 'a')
    tui.title('Ца накрутим классов на конкурсе)')
    tui.ul(['Чупа - 47703','Солнечный день - 47714'])
    mem = input('за кого голосуем? ')
    if mem.isnumeric and len(mem) == 5:
        url = 'https://stolicadetstva.com/competition/vote/' + mem
        attempt = input('Сколько классов крутить?: ')
        try:
            attempt = int(attempt)
        except:
            print('нужно ввести цифру')
            time.sleep(2)
            tryToConnect(content)
        if 0 < attempt:
            for i in content:
                if i not in usedproxy and attempt > 0:
                    ip = i
                    usedproxy.append(i)
                    print('\n' + i, file=usedproxyfile)
                    print(ip, end='\r')
                    try:
                        requests.get(url, proxies=dict(http = 'socks5://'+ip, https = 'socks5://'+ip))
                    except:
                        tryToConnect(content)
                attempt -= 1
                print('Классов осталось {}'.format(attempt), end='\r')
                time.sleep(0.5)
            usedproxyfile.close()
            main(content)
        elif attempt < 0:
            main(content)
        else:
            print('нужно ввести цифру больше 0')
            time.sleep(2)
            tryToConnect(content)
    elif mem.isnumeric and int(mem) < 0:
        main(content)
    else:
        print('Нужно ввести номер голосования длиной в 5 символов')
        time.sleep(2)
        tryToConnect(content)

def proxyParser(content):
    '''
    Сбор адрессов прокси из файла сайта http://spys.one/
    '''
    os.system('cls||clear')
    try:
        with open('socks.html') as f:
            html = f.readlines()
        html = [x.strip() for x in html] 
    except:
        tui.label('!!Нет файла страницы!!')
        tui.ul(['Сохрани страницу http://spys.one/ в виде html','Перемести в корневую папку приложения','Переименуй в socks.html'])
        ext = input('введи "y" для перехода на страницу..')
        if ext == 'y':
            webbrowser.open('http://spys.one/proxies/', new=0, autoraise=True)
            main(content)
        else:
            main(content)
    tui.title('Сбор ip прокси...')
    with open('socks.html', encoding='utf-8') as f:
        html = f.read()
    proxyfile = open('proxy.txt', 'a')
    soup = BeautifulSoup(html, 'html.parser')
    ip = soup.find_all('tr', 'spy1xx')
    for i in ip:
        ips = i.find_next('td').text
        if ips not in content:
            print(ips, file=proxyfile)

    f.close()
    main(content)

def members():
    os.system('cls||clear')
    tui.title('Сбор информации об участниках')

    '''Переменные'''
    lot_id = []                                                 # Список имен
    members = 0                                                 # Кол-во участников
    allready = []                                               # Список использованных имен
    membersDict = {}                                            # Словарь участников и кол-ва их голосов

    url = 'https://stolicadetstva.com/competition/work/277/'    # Адресс для парсинга
    r = requests.get(url)                                       # Запрос всей страницы
    soup = BeautifulSoup(r.text, 'html.parser')                 # Подготовка к парсингу
    lots = soup.find_all('li', 'compe_comment_li')              # Парсинг всех 'li' тегов с классом 'compe_comment_li'
    lot_ids = soup.find_all('p', 'who')                         # Парсинг всех 'p' тегов с классом 'who'

    '''Парсинг имен и голосов'''
    for i in lot_ids:                                           # Преобразования тегов 'p' в список
        lot_id.append(i.text)                                   #

    for i in lots:
        for x in lot_id:
            if x in i.text and not x in allready:               # Поиск имен из lot_id в тегах 'li' не используемые ранее
                ans = i.find('p', 'compe_comment').text         # Ищем текст тегов 'p' с классом 'compe_comment'
                ans = ans.replace(' | Голосую', '')             # Удаляем из текста ' | Голосую'
                votes = int(ans.replace('Голосов: ', ''))       # Удаляем остальной текст для преобразования в int
                membersDict.setdefault(x, votes)                # Создаем словарь из ключа x и значения votes
                allready.append(x)                              # Добавляем x в уже использованные
                members += 1                                    # Увеличиваем кол-во участников
                tui.updatingScore('Участников', members, 0)  # Запускаем счетчик участников

    '''Сортировка участников по голосам и запись их в файл'''
    print('\n\n')
    votesList = list(membersDict.items())                       # Преобразование словаря участников в список
    votesList.sort(key=lambda i: i[1])                          # Сортировка списка по возрастанию значений словаря
    #print('Участников :' + str(members) + '\n\n', file=f)       # Запись в файл кол-ва участников
    for i in votesList:                                         # Запись и вывод участников по возрастанию голосов
        print(i[0], ':', i[1])
    ext = input('\nНажми "Enter", чтобы выйти в главное меню\nили введите "y" чтобы вывести список в файл\n')
    if ext == 'y':  
        try:
            f = open('members.txt', 'w')                            # Файл для записи "топа" участников
        except:
            f = open('members.txt', 'x')
            f.close()
            f = open('members.txt', 'w')
        for i in votesList:
            #print(i[0], ':', i[1])
            print(i[0], ':', i[1], file=f)
        print('сохранено в файл "members.txt"')
        f.close()
        time.sleep(2)
    main(content)

try:
    with open('proxy.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
except:
    content = open('proxy.txt', 'x')
    content.close()
    with open('proxy.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    proxyParser(content)

main(content)
