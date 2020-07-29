''' Импорт модулей '''
import requests                                         # Http запросы
import webbrowser                                       # Для запуска браузера
import os                                               # Для настройки консоли и работы с файлами
import time                                             # Для установки задержек
import configparser                                     # Для натстроек
from bs4 import BeautifulSoup                           # Для парсинга страниц
import easyTui as tui                                   # Мой модуль для TUI

def main(content):                                      #### Главное меню
    '''
    Главное меню
    '''
    os.system('cls||clear')                             # Очистка консоли
                                                        ### Интерфейс
    tui.title(lang.titleMain + ver)                     # Заголовок
    tui.label(lang.labelMain)                           #
    tui.ol(lang.olMainOpt)                              # Функции в главном меню
    tui.ul(lang.exitMain)                               # Выход
    print(lang.printMainBack)
    com = input()                                       ## Запрос команды пользователя      
                                                        ### Запуск функций выбранных пользователем
    if com == '0':                                      ## Накрутка
        def tryToCon(content):     
            os.system('cls||clear')                                 # Очистка консоли
            tui.title(lang.titleTryToCon)                                # Заголовок
            tui.ul(['Чупа - 47703','Солнечный день - 47714'])       # Маркированный список
            mem = input(lang.inputTryToConMem)                       # Запрос команды
            if mem.isnumeric and len(mem) == 5:                     # Проверка команды
                url = 'https://stolicadetstva.com/competition/vote/' + mem  # адресс голосования
                attempt = input(lang.inputTryToConAttempt)               # Запрос команды на кол-во голосов
                try:                                                # Проверка команды
                    attempt = int(attempt)
                except:
                    print(lang.exceptNeedNumber)
                    time.sleep(2)
                    tryToCon(content)                               
                if attempt < 0:                                     # Выход в главное меню
                    main(content)
            elif int(mem) < 0:
                main(content)
            else:
                print(lang.exceptMain)
                time.sleep(2)
                tryToCon(content)
            os.system('cls||clear')                                 # Очистка консоли
            tryToConnect(content, url, attempt)                     # Запуск функции накрутки
        
        tryToCon(content)
        main(content)  

    elif com == '1':                                    ## Накрутка нескольким
        def tryToCon(content):                          
            os.system('cls||clear')                                 # Очистка консоли
            tui.title(lang.titleTryToCon)                           # Заголовок
            tui.ul(['Чупа - 47703','Солнечный день - 47714'])       # Маркированный список
            attempt = input(lang.inputTryToConAttempt)              # Запрос команды на кол-во голосов
            try:                                                    ## Проверка команды
                attempt = int(attempt)
            except:
                print(lang.exceptNeedNumber)
                time.sleep(2)
                tryToCon(content)                               
            if attempt < 0:                                         # Выход в главное маню
                main(content)
            mem = input(lang.inputTryToConMem)                      # Запрос команды
            if int(mem) < 0:                                        # Проверка ввода
                main(content)
            mems = mem.split()                                      # Преобразование ввода в список
            usedmem = []                                            # Список участников за которых уже проголосовали
            for i in mems:                                          # Берем поочередно каждого участника
                try:                                                # Попытка удалить файл использованных прокси
                    os.remove('usedproxy.txt')
                    main(content)
                except:                                             # Если неудача
                    print(lang.exceptListRemoved)                   # Вывод сообщения "список уже удален"
                    time.sleep(2)
                usedmem.append(i)                                   # Записываем участника в использованные
                url = 'https://stolicadetstva.com/competition/vote/' + i  # адресс голосования
                os.system('cls||clear')                             # Очистка консоли
                tryToConnect(content, url, attempt)                 # Запуск функции накрутки
        tryToCon(content)                               # Запуск функции                                       
        main(content)                                   # Выход в главное меню после выполнения
         
    elif com == '2':                                  ## Накрутка через сеть Tor
        def tryToCon(content):     
            os.system('cls||clear')                     # Очистка консоли
            tui.title(lang.titleTryToCon)               # Заголовок
            tui.ul(['Чупа - 47703','Солнечный день - 47714']) # Маркированный список
            mem = input(lang.inputTryToConMem)          # Запрос команды
            if mem.isnumeric and len(mem) == 5:         # Проверка команды
                url = 'https://stolicadetstva.com/competition/vote/' + mem  # адресс голосования
                attempt = input(lang.inputTryToConAttempt) # Запрос команды на кол-во голосов
                try:                                    # Проверка команды
                    attempt = int(attempt)
                except:
                    print(lang.exceptNeedNumber)
                    time.sleep(2)
                    tryToCon(content)                               
                if attempt < 0:                         # Выход в главное меню
                    main(content)
            elif int(mem) < 0:
                main(content)
            else:
                print(lang.exceptMain)
                time.sleep(2)
                tryToCon(content)
            os.system('cls||clear')                     # Очистка консоли
            tryToTorConnect(content, url, attempt)      # Запуск функции накрутки

        def checkTor():
            os.system('cls||clear')                     # Очистка консоли
            cmd = input(lang.torCheck)
            if cmd.lower() in 'yд':
                tryToCon(content)
            elif cmd.lower() in 'nн':
                cmd = input(lang.noTor)
                if cmd.lower() in 'yд':
                    webbrowser.open('https://www.torproject.org/ru/download/tor/')
                main(content)
            else:
                print(lang.exceptTor)
                time.sleep(1)
                checkTor()
        checkTor()
           
    elif com == '3':                                    ## Сбор ip прокси из html файла
        proxyParser(content)
        main(content)

    elif com == '4':                                    ## Удаление списка использованных прокси
        try:                                            # Попытка удалить
            os.remove('usedproxy.txt')
            main(content)
        except:                                         # Если неудача
            print(lang.exceptListRemoved)               # Вывод сообщения "список уже удален"
            time.sleep(2)
            main(content)                               # Главное меню

    elif com == '5':                                    ## Сбор информации об участниках
        membersFunc()

    elif com == '6':                                    ## Открытие сайта конкурса
        def openwebsite():
            tui.ul(['"Мохнатые, пернатые" - 277'])                  # Пример ввода
            contest = input(lang.inputContestNom)                   # Запрос ввода
            if contest.isnumeric() and len(contest):                # Проверка ввода
                url = 'https://stolicadetstva.com/competition/work/' + contest
                webbrowser.open(url, new=0, autoraise=True)
            elif int(contest) < 0:                                  # Если ввод меньше 0, то переход в главное меню
                main(content)                                       #
            else:                                                   #
                print(lang.exceptContestNum)
                time.sleep(3)                                       #
                openwebsite()
        openwebsite()
        main(content)

    elif com == '7':                                    ## Настройки
        settings()
        main(content)

    elif com == '228' or com.lower() == 'exit':         ## Выход
        quit()

    else:                                               ## Проверка команды
        print(lang.exceptMain)
        time.sleep(1)
        main(content)                                   # Главное меню

def tryToConnect(content, url, attempt):                #### Накрутка голосов
    '''
    Подбор прокси из списка и попытка соединения с сервером
    '''
    if os.path.exists('usedproxy.txt'):                 # Попытка открыть и прочитать файл с использованными прокси
        with open('usedproxy.txt') as f:                # Открываем файл
            usedproxy = f.readlines()                   # Записываем каждую строку файла в список
        usedproxy = [x.strip() for x in usedproxy]      # Удаляем служебные символы
    else:                                               # При неудачи создать файл и открыть его
        usedproxy = open('usedproxy.txt', 'w')
        usedproxy.close()
        with open('usedproxy.txt') as f:                # Открываем файл
            usedproxy = f.readlines()                   # Записываем каждую строку файла в список
        usedproxy = [x.strip() for x in usedproxy]      # Удаляем служебные символы

    ### Выводим сколько осталось неисползованных прокси
    print(lang.printProxyLeft, len(list(set(content) - set(usedproxy))))
    usedproxyfile = open('usedproxy.txt', 'a')          # Открыть файл использованных прокси на дозапись
    while attempt > 0:                                  # Цикл накрутки
        for ip in content:                              # Берем каждый ip из файла прокси
            if ip not in usedproxy:                     # И если он еще не использовался
                usedproxy.append(ip)                    # Дописываем в список ip прокси
                print(ip, file=usedproxyfile)           # Записываем его в файл
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
            elif len(list(set(content) - set(usedproxy))) == 0:  ## Проверка на наличие неиспользованных прокси
                tui.title(lang.exceptProxyLost)         ### Выводим информацию об этом 
                tui.ul(lang.ulTryToCon)                 ### и инструкцию по исправлению проблемы
                input(lang.inputPressEnter)             # Ожидание пользователя
                main(content)                           # Выход в главное меню

def tryToTorConnect(content, url, attempt):
    proxies = {
        'http': "socks5h://localhost:9050",
        'https': "socks5h://localhost:9050"
    }
    print(attempt)
    while attempt > 1:
        try:                                    ## Попытка установить соединение
            ### GET запрос на url через прокси dict с таймаутом в 10 секунд
            print('request', end='\r')          # Выводим 'request' и возвращаем каретку в начало этой строки
            requests.get(url, proxies=proxies)
            print('request Accepted')           # Если соединение успешно то выводим 'request Accepted'
            time.sleep(1)                       # Ждем 1 секунду
            attempt -= 1                        # Уменьшаем попытки на 1
            tryToTorConnect(content, url, attempt) # Перезапускаем функцию
        except:                                 ## Если неудача
            print('Not requesting')             # Выводим 'Not requesting'
            time.sleep(1)                       # Ждем 1 секунду
            tryToTorConnect(content, url, attempt) # Перезапускаем функцию
    main(content)

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
        tui.label(lang.exceptProxyPTitle)
        tui.ul(lang.ulProxyP1)
        tui.ol(lang.olProxyP)
        tui.ul(lang.ulProxyP2)
        ext = input(lang.inputProxyp)
        if ext == 'y':                                  # Открываем браузер с нужным сайтом
            webbrowser.open('http://spys.one/proxies/', new=0, autoraise=True)
            main(content)
        else:                                           # Главное меню
            main(content)                               

    tui.title(lang.titleProxyP)                         # Заголовок
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

def membersFunc():                                      #### Сбор информации об участниках
    '''
    Сбор данных об участниках (Место в топе, код голосования,
                                Название, Количество голосов,)
    '''
    os.system('cls||clear')
    '''Переменные'''
    lot_id = []                                                 # Список имен
    members = 0                                                 # Кол-во участников
    allready = []                                               # Список использованных имен
    membersDict = {}                                            # Словарь участников и кол-ва их голосов
    tui.ul(['"Мохнатые, пернатые" - 277'])                      # Пример ввода
    contest = input(lang.inputContestNom)                       # Запрос ввода
    if contest.isnumeric() and len(contest):                    # Проверка ввода
        url = 'https://stolicadetstva.com/competition/work/' + contest
    elif int(contest) < 0:                                      # Если ввод меньше 0 то выходим в главное меню
        main(content)                                           #
    else:                                                       # Иначе сообщаем об ошибке ввода
        print(lang.exceptContestNum)
        time.sleep(3)                                           #
        membersFunc()                                           # Перезапускаем функцию
    os.system('cls||clear')                                     # Очищаем консоль
    tui.title(lang.titleMembers)                                # Выводим заголовок
    r = requests.get(url)                                       # Запрос всей страницы
    soup = BeautifulSoup(r.text, 'html.parser')                 # Подготовка к парсингу
    lots = soup.find_all('li', 'compe_comment_li')              # Парсинг всех 'li' тегов с классом 'compe_comment_li'
    lot_ids = soup.find_all('p', 'who')                         # Парсинг всех 'p' тегов с классом 'who'

    '''Парсинг имен и голосов'''
    for i in lot_ids:                                           # Преобразования тегов 'p' в список
        lot_id.append(i.text)                                   # 

    for i in lots:                                              # В каждом 'li' теге
        for x in lot_id:                                        # Каждый 'p' тег
            if x in i.text and not x in allready:               # Поиск имен из lot_id в тегах 'li' не используемые ранее
                ans = i.find('p', 'compe_comment').text         # Ищем текст тегов 'p' с классом 'compe_comment'
                try:                                            # Проверяем есть ли в 'p'  теге строки 'Голосую'
                    link = i.find(text='Голосую').parent.get('href') # и если есть берем ссылку
                    link = link.replace('/competition/vote/', '') # Очищаем от лишнего
                    link = link.replace('/', '')
                except:                                         # Иначе пишем, что конкурс закончился
                    link = lang.outlinkMembers
                ans = ans.replace(' | Голосую', '')             # Удаляем из текста ' | Голосую'
                votes = int(ans.replace('Голосов: ', ''))       # Удаляем остальной текст для преобразования в int
                allready.append(x)                              # Добавляем x в уже использованные
                x = link + ': ' + x                             # К каждому имени вначали приписываем Код голосования через двоеточие
                membersDict.setdefault(x, votes)                # Создаем словарь из ключа x и значения votes
                members += 1                                    # Увеличиваем кол-во участников
                tui.updatingScore(lang.memMembers, members, 0)     # Запускаем счетчик участников
                
    '''Сортировка участников по голосам и запись их в файл'''
    print('\n\n')
    votesList = list(membersDict.items())                       # Преобразование словаря участников в список
    votesList.sort(key=lambda i: i[1])                          # Сортировка списка по возрастанию значений словаря
    membersTemp = members                                       # Создаем временнюю переменную участников
    for i in votesList:                                         # Вывод участников по возрастанию голосов
        print(membersTemp, '\t', i[0], ':', i[1])               #
        membersTemp -= 1                                        #
    print('\n\n', lang.memMembers, ': ', members)               # Выводим общее кол-во участников
    ext = input(lang.inputMembers)
    if ext == 'y':                                              # Запрос команды на печать списка в файл
        try:                                                    # Проверка файла на наличие
            f = open('members.txt', 'w')                        # Открываем на запись
        except:                                                 # Если его нет
            f = open('members.txt', 'x')                        # Создаем файл и открываем на запись
        membersTemp = members                                   # Временная переменная для вывода топа
        for i in votesList:                                     # Запись участников в файл
            print(membersTemp, '\t', i[0], ':', i[1], file=f)   # 
            membersTemp -= 1                                    #
        print('\n\n', lang.memMembers, ': ', members, file=f)   # Запись кол-ва участников в файл
        print(lang.saveMembers)                                 # 
        f.close()                                               # Закрываем файл
        time.sleep(2)                                           # Ждем 2 секунды
    main(content)                                               # Выходим в главное меню

def settings():                                         #### Настройка config.ini
    '''
    Установка языка в конфиг
    '''
    os.system('cls||clear')                             # Очистка консоли
    tui.title('Settings')                               # Заголовок
    tui.ol(['English lang', 'Russian lang'])            # Список вариантов
    cmd = input()                                       # Ввод команды
    try:                                                # Проверка ввода на целое число
        cmd = int(cmd)                                  # Если ввод меньше нуля и конфиг имеется
        if int(cmd) < 0 and os.path.exists('config.ini'):
            main(content)                               # То выходим в главное меню
    except:                                             # Иначе показываем пример ввода
        print('Enter 0/1')
        time.sleep(1)
        settings()                                      # Перезапускаем функцию
    # Set English lang in config // Установка Английского языка в конфиг
    if cmd == 0:
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.set("Settings", "lang", "en")  
        with open('config.ini', "w") as config_file:
            config.write(config_file)
    # Set Russian lang in config // Установка Русского языка в конфиг
    elif cmd == 1:
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.set("Settings", "lang", "ru")    
        with open('config.ini', "w") as config_file:
            config.write(config_file)
    else:
        print('Enter number 0-1')
        time.sleep(1)
        settings()
    langCheck()

def langCheck():                                        #### Проверка config.ini и установка языка
    '''
    Проверка значения языка в конфиге
    '''
    if not os.path.exists('config.ini'):
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.set("Settings", "lang", "en")  
        with open('config.ini', "w") as config_file:
            config.write(config_file)

    config = configparser.ConfigParser()
    config.read('config.ini')
    confget = config.get("Settings", "lang")
    # Check English lang // Проверка Англйский язык
    if confget == 'en':
        global lang
        import lang.en as lang
    # Check Russian lang // Проверка Русский язык
    elif confget == 'ru':
        global lang
        import lang.ru as lang
    else:
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.set("Settings", "lang", "en")  
        with open('config.ini', "w") as config_file:
            config.write(config_file)

if __name__ == "__main__":                              ## Инициализация    
    ver = '200729'                                      ## Версия приложения
    os.system('mode con cols=64 lines=20')              # Установка размеров консоли
    os.system('color 0A')                               # Установка цвета консоли    
    confget = ''
    global lang

    langCheck()

    if os.path.exists('proxy.txt'):                     ## Проверка наличия файла прокси листа
        with open('proxy.txt') as f:                    # Открываем файл
            content = f.readlines()                     # Выводим строки в список
        content = [x.strip() for x in content]          # Чистим строки от лишних символов
    else:                                               ## Иначе
        tui.ul(lang.ProxyInitMsg)
        time.sleep(2)
        content = open('proxy.txt', 'x')                # Создаем файл
        content.close()                                 # Закрываем файл
        with open('proxy.txt') as f:                    # Открываем файл
            content = f.readlines()                     # Выводим строки в список
        content = [x.strip() for x in content]          # Чистим строки от лишних символов
        proxyParser(content)                            # Запускаем генератор прокси листа

    main(content)                                       # Запуск главного меню