''' Импорт модулей '''
import requests                                         # Http запросы
import webbrowser                                       # Для запуска браузера
from bs4 import BeautifulSoup                           # Для парсинга страниц
import easyTui as tui                                   # Мой модуль для TUI
import os                                               # Для настройки консоли и работы с файлами
import time                                             # Для установки задержек

os.system('mode con cols=64 lines=20')                  # Установка размеров консоли
os.system('color 0A')                                   # Установка цвета консоли

def main(content):                                      #### Главное меню
    '''
    Главное меню
    '''
    os.system('cls||clear')                             # Очистка консоли
                                                        ### Интерфейс
    tui.title('Крутильщик классов для децкава конкурса')# Заголовок
    tui.label('Что делать?')                            #
    tui.ol(['Крутить классы', 
            'Крутить классы нескольким участникам',     # Варианты ответов                
            'Собрать новый список прокси',              #
            'Удалить список использованных прокси',     #
            'Вывести список участников',
            'Открыть сайт конкурса'])                #
    print('чтобы вернуться сюда введи число меньше нуля')
    com = input()                                       ## Запрос команды пользователя
    try:                                                # проверка команды
        com = int(com)                                  
    except:                                             
        print('Нужно ввести цифру от 0 до 5')           
        time.sleep(2)                                   
        main(content)                                   
                                                        ### Запуск функций выбранных пользователем
    if com == 0:                                        ## Накрутка
        def tryToCon(content):     
            os.system('cls||clear')                                 # Очистка консоли
            tui.title('Ща накрутим классов на конкурсе)')           # Заголовок
            tui.ul(['Чупа - 47703','Солнечный день - 47714'])       # Маркированный список
            mem = input('за кого голосуем? ')                       # Запрос команды
            if mem.isnumeric and len(mem) == 5:                     # Проверка команды
                url = 'https://stolicadetstva.com/competition/vote/' + mem  # адресс голосования
                attempt = input('Сколько классов крутить?: ')       # Запрос команды на кол-во голосов
                try:                                                # Проверка команды
                    attempt = int(attempt)
                except:
                    print('нужно ввести цифру')
                    time.sleep(2)
                    tryToCon(content)                               
                if attempt < 0:                                     # Выход в главное меню
                    main(content)
            elif int(mem) < 0:
                main(content)
            else:
                print('Нужно ввести номер голосования длиной в 5 символов')
                time.sleep(2)
                tryToCon(content)
            os.system('cls||clear')                                 # Очистка консоли
            tryToConnect(content, url, attempt)                     # Запуск функции накрутки
        
        tryToCon(content)
        main(content)  

    elif com == 1:                                      ## Накрутка нескольким
        def tryToCon(content):     
            os.system('cls||clear')                                 # Очистка консоли
            tui.title('Ща накрутим классов на конкурсе)')           # Заголовок
            tui.ul(['Чупа - 47703','Солнечный день - 47714'])       # Маркированный список
            attempt = input('Сколько классов крутить?: ')       # Запрос команды на кол-во голосов
            try:                                                # Проверка команды
                attempt = int(attempt)
            except:
                print('нужно ввести цифру')
                time.sleep(2)
                tryToCon(content)                               
            if attempt < 0:                                     # Выход в главное меню
                main(content)
            mem = input('за кого голосуем? ')                       # Запрос команды
            if int(mem) < 0:
                main(content)
            mems = mem.split()
            usedmem = []
            for i in mems:
                try:                                            # Попытка удалить
                    os.remove('usedproxy.txt')
                    main(content)
                except:                                         # Если неудача
                    print('Список уже удален..')                # Вывод сообщения "список уже удален"
                    time.sleep(2)
                usedmem.append(i)
                url = 'https://stolicadetstva.com/competition/vote/' + i  # адресс голосования
                os.system('cls||clear')                                 # Очистка консоли
                tryToConnect(content, url, attempt)                     # Запуск функции накрутки
        tryToCon(content)
        main(content)    
                    
    elif com == 2:                                      ## Сбор ip прокси из html файла
        proxyParser(content)

    elif com == 3:                                      ## Удаление списка использованных прокси
        try:                                            # Попытка удалить
            os.remove('usedproxy.txt')
            main(content)
        except:                                         # Если неудача
            print('Список уже удален..')                # Вывод сообщения "список уже удален"
            time.sleep(2)
            main(content)                               # Главное меню

    elif com == 4:                                      ## Сбор информации об участниках
        membersFunc()

    elif com == 5:
        webbrowser.open('https://stolicadetstva.com/competition/work/277/', new=0, autoraise=True)

    else:                                               ## Проверка команды
        print('Нужно ввести цифру от 0 до 5')
        time.sleep(2)
        main(content)                                   # Главное меню

def tryToConnect(content, url, attempt):                #### Накрутка голосов
    '''
    Подбор прокси из списка и попытка соединения с сервером
    '''
    try:                                                # Попытка открыть и прочитать файл
        with open('usedproxy.txt') as f:
            usedproxy = f.readlines()
        usedproxy = [x.strip() for x in usedproxy] 
    except:                                             # При неудачи создать файл и открыть его
        usedproxy = open('usedproxy.txt', 'w')
        usedproxy.close()
        with open('usedproxy.txt') as f:
            usedproxy = f.readlines()
        usedproxy = [x.strip() for x in usedproxy] 
    if len(list(set(content) - set(usedproxy))) == 0:
        tui.title('Неиспользованных прокси не осталось!')
        tui.ul(['Зайдите в главное меню','Соберите новый список прокси [2]','Или удалите список использованных [3]\n\tэффективность будет хуже'])
        input('\nНажмите "Enter"..')
        main(content)
    print('Осталось неиспользованных прокси серверов :', len(list(set(content) - set(usedproxy))))
    usedproxyfile = open('usedproxy.txt', 'a')          # Открыть файл использованных прокси на дозапись
    while attempt > 0:                                  # Пока попытки больше 0
        for i in content:                               # берем каждый ip из файла
            if i not in usedproxy:                      # И если он еще не использовался
                ip = i
                usedproxy.append(i)                     # Дописываем в список ip прокси
                print(i, file=usedproxyfile)            # Записываем его в файл
                usedproxyfile.close()                   # Закрываем файл
                print(ip, end='\n')                     # Выводим на экран ip Прокси
                try:                                    ## Попытка установить соединение
                    print('request', end='\r')          # Выводим 'request' и возвращаем каретку в начало этой строки
                    ### GET запрос на url через прокси dict с таймаутом в 10 секунд
                    requests.get(url, proxies=dict(http = 'socks5://'+ip, https = 'socks5://'+ip), timeout=10)
                    print('request Accepted')           # Если соединение успешно то выводим 'request Accepted'
                    time.sleep(1)                       # Ждем 1 секунду
                    attempt -= 1                        # Уменьшаем попытки на 1
                    tryToConnect(content, url, attempt) # Перезапускаем функцию
                except:                                 ## Если неудача
                    print('Not requesting')             # Выводим 'Not requesting'
                    time.sleep(1)                       # Ждем 1 секунду
                    tryToConnect(content, url, attempt) # Перезапускаем функцию
            elif len(list(set(content + usedproxy))) == 0:
                tui.title('Все прокси использованны..')
                tui.ul(['Перейдите в главное меню','Соберите новый список прокси','Или очистите список использованных прокси'])
                time.sleep(4)                           ## Главное меню

def proxyParser(content):                               #### Сбор списка прокси
    '''
    Сбор адрессов прокси из файла сайта http://spys.one/proxies/
    '''
    os.system('cls||clear')
    if os.path.exists('socks.html'):                    # Попытка открытия файла
        with open('socks.html', encoding='utf-8', errors='ignore') as f:
            html = f.readlines()
        html = [x.strip() for x in html] 
    else:                                               # Если неудача, выводим сообщение
        tui.label('!!Нет файла страницы!!')
        tui.ul(['Зайди на http://spys.one/proxies/','Выставь  парамметры'])
        tui.ol(['Тип: SOCKS5','Порт: 1080','По: 500'])
        tui.ul(['Сохрани страницу в корневую папку приложени\n\tс именем "socks.html"'])
        ext = input('введи "y" для чтобы перейти на страницу..')
        if ext == 'y':                                  # Открываем браузер с нужным сайтом
            webbrowser.open('http://spys.one/proxies/', new=0, autoraise=True)
            main(content)
        else:                                           # Главное меню
            main(content)                               

    tui.title('Сбор ip прокси...')                      # Заголовок
    with open('socks.html', encoding='utf-8') as f:     # Открытие файла для чтения
        html = f.read()                                 # 
    proxyfile = open('proxy.txt', 'w')                  # Открытие файла со списком прокси на дозапись
    soup = BeautifulSoup(html, 'html.parser')           # Парсер
    for script in soup.find_all('script'):
        script.extract()                                # Парсим все 'tr' теги с классом 'sp1xx'
    for i in soup.find_all('tr', 'spy1xx'):             # В каждом 'tr' теге
        ips = i.find_next('font','spy14')               # Ищем первый 'td' тег
        if ips not in content:                          # И если этого ip нет в файле, то записываем
            print(ips.get_text() + ':1080')
            print(ips.get_text() + ':1080', file=proxyfile)# Запись ip в файл
    time.sleep(2)
    proxyfile.close()                                   # Закрываем файл
    os.remove('socks.html')                             # Удаляем socks.html
    main(content)                                       # Выходим в главное меню

def membersFunc():                                      #### Сбор информации об участниках
    os.system('cls||clear')

    '''Переменные'''
    lot_id = []                                                 # Список имен
    members = 0                                                 # Кол-во участников
    allready = []                                               # Список использованных имен
    membersDict = {}                                            # Словарь участников и кол-ва их голосов
    tui.ul(['"Мохнатые, пернатые" - 277'])                      #
    contest = input('Введи номер конкурса: ')                   #
    if contest.isnumeric() and len(contest):                    #
        url = 'https://stolicadetstva.com/competition/work/' + contest
    elif int(contest) < 0:                                      #
        main(content)                                           #
    else:                                                       #
        print('Нужно ввести числовой номер конкурса из 3 цифр..')
        time.sleep(3)                                           #
        membersFunc()                                           #
    os.system('cls||clear')                                     #
    tui.title('Сбор информации об участниках')                  #
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
                try:
                    link = i.find(text='Голосую').parent.get('href')
                    link = link.replace('/competition/vote/', '')
                    link = link.replace('/', '')
                except:
                    link = 'кончился'
                ans = ans.replace(' | Голосую', '')             # Удаляем из текста ' | Голосую'
                votes = int(ans.replace('Голосов: ', ''))       # Удаляем остальной текст для преобразования в int
                allready.append(x)                              # Добавляем x в уже использованные
                x = link + ': ' + x
                membersDict.setdefault(x, votes)                # Создаем словарь из ключа x и значения votes
                members += 1                                    # Увеличиваем кол-во участников
                tui.updatingScore('Участников', members, 0)     # Запускаем счетчик участников
                

    '''Сортировка участников по голосам и запись их в файл'''
    print('\n\n')
    votesList = list(membersDict.items())                       # Преобразование словаря участников в список
    votesList.sort(key=lambda i: i[1])                          # Сортировка списка по возрастанию значений словаря
    membersTemp = members
    for i in votesList:                                         # Вывод участников по возрастанию голосов
        print(membersTemp, '\t', i[0], ':', i[1])               #
        membersTemp -= 1                                        #
    print('\n\nУчастников: ', members)                          #
    ext = input('\nНажми "Enter", чтобы выйти в главное меню\nили введите "y" чтобы вывести список в файл\n')
    if ext == 'y':                                              # Запрос команды на печать списка в файл
        try:                                                    # Проверка файла на наличие
            f = open('members.txt', 'w')                        # Открываем на запись
        except:                                                 # Если его нет
            f = open('members.txt', 'x')                        # Создаем файл и открываем на запись
        membersTemp = members                                   # Временная переменная для вывода топа
        for i in votesList:                                     # Запись участников в файл
            print(membersTemp, '\t', i[0], ':', i[1], file=f)   #
            membersTemp -= 1                                    #
        print('\n\nУчастников: ', members, file=f)              # Запись кол-ва участников в файл
        print('сохранено в файл "members.txt"')                 # 
        f.close()                                               # Закрваем файл
        time.sleep(2)                                           # Ждем 2 секунды
    lot_id = None                                               # Список имен
    members = None                                              # Кол-во участников
    allready = None                                             # Список использованных имен
    membersDict = None                                          # Словарь участников и кол-ва их голосов
    main(content)                                               # Выходим в главное меню

try:                                                    ## Попытка открыть файл с прокси
    with open('proxy.txt') as f:                        # Открываем файл
        content = f.readlines()                         # Выводим строки в список
    content = [x.strip() for x in content]              # Чистим строки от лишних символов
except:                                                 ## Иначе
    tui.title('Видимо это первый запуск приложения')
    time.sleep(1)
    tui.ul(['Сейчас будет запущена функция сборки листа прокси серверов'])
    time.sleep(2)
    content = open('proxy.txt', 'x')                    # Создаем файл
    content.close()                                     # Закрываем файл
    with open('proxy.txt') as f:                        # Открываем файл
        content = f.readlines()                         # Выводим строки в список
    content = [x.strip() for x in content]              # Чистим строки от лишних символов
    proxyParser(content)                                # Запускаем генератор прокси листа

main(content)                                                   # Запуск главного меню