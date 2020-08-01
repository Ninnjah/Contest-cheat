'''Импорт модулей'''
import os                                               # Для настройки консоли и работы с файлами
import time                                             # Для установки задержек
import json                                             # Для локализации
import requests                                         # Http запросы
import webbrowser                                       # Для запуска браузера
import configparser                                     # Для натстроек
from bs4 import BeautifulSoup                           # Для парсинга страниц
import easyTui as tui                                   # Мой модуль для TUI

def main():                                             #### Главное меню
    '''
    Главное меню
    '''
    os.system('cls||clear')                             # Очистка консоли
                                                        ### Интерфейс
    print(tui.title(lang.get('titleMain') + ver))       # Заголовок
    print(tui.label(lang.get('labelMain')))             #
    print(tui.ol(lang.get('olMainOpt')))                # Функции в главном меню
    print(tui.ul(lang.get('exitMain')))                 # Выход
    print(lang.get('printMainBack'))
    com = input()                                       ## Запрос команды пользователя   

#! Запуск функций выбранных пользователем
    if com == '0':                                      ## Накрутка

        def tryToCon(content):   
            os.system('cls||clear')                     # Очистка консоли
            print(tui.title(lang.get('titleTryToCon'))) # Заголовок
            print(tui.ul(['Чупа - 47703',               # Маркированный список
                        'Солнечный день - 47714'])) 

            mem = input(lang.get('inputTryToConMem'))   # Запрос команды
            attempt = input(lang.get('inputTryToConAttempt'))  # Запрос команды на кол-во голосов

            ## Проверка на правильность ввода кода голосования
            def numbersCheck(mem, attempt):                      
                if is_5digit(mem):                          # Проверка ввода кода голосования
                    try:
                        int(mem)
                    except ValueError:
                        print(lang.get('exceptMain'))
                        time.sleep(2)
                        tryToCon(content)
                
                try:                                        # Проверка ввода на цифру
                    int(attempt)                               
                    if int(attempt) < 0:                    # Выход в главное меню
                        main()
                except ValueError:
                    print(lang.get('exceptNeedNumber'))
                    time.sleep(2)
                    tryToCon(content)
            
            if ' ' in mem:
                mem = mem.split()
                for i in mem:
                    numbersCheck(i, attempt)
            else:
                numbersCheck(mem, attempt)
                mem = [mem]

            os.system('cls||clear')                     # Очистка консоли
            tryToConnect(content, mem, attempt)         # Запуск функции накрутки

        tryToCon(proxy_check())
        main()  

    elif com == '1':                                    ## Накрутка через сеть Tor

        def tryToCon():                                 ## Сбор информации для накрутки
            os.system('cls||clear')                     # Очистка консоли
            print(tui.title(lang.get('titleTryToCon'))) # Заголовок
            print(tui.ul(['Чупа - 47703',               # Маркированный список
                        'Солнечный день - 47714'])) 
            mem = input(lang.get('inputTryToConMem'))   # Запрос команды
            attempt = input(lang.get('inputTryToConAttempt')) # Запрос команды на кол-во голосов

            ## Проверка на правильность ввода кода голосования
            def numbersCheck(mem, attempt):                  
                if is_5digit(mem):                      # Проверка ввода кода голосования
                    try:                                # Пытаемся преобразовать в целое число
                        int(mem)
                        if int(attempt) < 0:                # Выход в главное меню
                            main()
                    except ValueError:                  # при ошибке перезапускаем
                        print(lang.get('exceptMain'))
                        time.sleep(2)
                        tryToCon()
                else:
                    tryToCon()

                try:                                    # Проверка ввода на цифру
                    int(attempt)                        # Пытаемся преобразовать в целое число       
                    if int(attempt) < 0:                # Выход в главное меню
                        main()
                except ValueError:
                    print(lang.get('exceptNeedNumber'))
                    time.sleep(2)                       # при ошибке перезапускаем
                    tryToCon()
            
            if ' ' in mem:                              ## Если в списке есть пробелы
                mem = mem.split()                       # то разделяем список
                for i in mem:                           # и проверяем каждое число
                    numbersCheck(i, attempt)
            else:                                       ## Иначе 
                numbersCheck(mem, attempt)              # проверяем число
                mem = [mem]                             # записываем его как список

            os.system('cls||clear')                     # Очистка консоли
            tryToTorConnect(mem, attempt)               # Запуск функции накрутки

        def checkTor():                                 ## Проверка наличия Тора
            os.system('cls||clear')                     # Очистка консоли
            config = configparser.ConfigParser()        # Объект парсера конфига
            config.read('config.ini')                   # Читаем конфиг
            try:                                        ## Пытаемся получить значение из конфига
                confget = config.get("Settings", "tor")
            except:                                     ## При неудаче 
                confget = ''                            # создаем пустую строку
                pass                                    # пропускаем
            # Check English lang.get // Проверка Англйский язык
            if confget == 'y':                          ## Если значение = y
                tryToCon()                              # Запускаем функцию
            else:                                       ## Иначе
                cmd = input(lang.get('torCheck'))       # Запрашиваем команду
                if cmd.lower() in 'yд':                 # Если согласие
                    config.set("Settings", "tor", "y")  # Устанавливаем значение конфига 'y'
                    with open('config.ini', "w") as config_file:
                        config.write(config_file)       # Записываем конфиг
                    tryToCon()                          # Запускаем функцию
                elif cmd.lower() in 'nн':               ## Если отказ
                    cmd = input(lang.get('noTor'))      ### Спрашиваем о переходе на сайт
                    if cmd.lower() in 'yд':             # при согласии открываем
                        webbrowser.open('https://www.torproject.org/ru/download/tor/')
                    main()                              
                else:                                   ## Иначе
                    print(lang.get('exceptTor'))
                    time.sleep(1)
                    checkTor()                          # Перезапускаем проверку

        checkTor()                                      ## Запускаем проверку
           
    elif com == '2':                                    ## Сбор ip прокси из html файла
        proxyParser(proxy_check())
        main()

    elif com == '3':                                    ## Удаление списка использованных прокси
        try:                                            # Попытка удалить
            os.remove('usedproxy.txt')
            main()
        except:                                         # Если неудача
            print(lang.get('exceptListRemoved'))        # Вывод сообщения "список уже удален"
            time.sleep(2)
            main()                               # Главное меню

    elif com == '4':                                    ## Сбор информации об участниках
        membersFunc()

    elif com == '5':                                    ## Открытие сайта конкурса
        def openwebsite():
            print(tui.ul(['"Мохнатые, пернатые" - 277'])) # Пример ввода
            contest = input(lang.get('inputContestNom')) # Запрос ввода
            if contest.isnumeric() and len(contest):        # Проверка ввода
                url = 'https://stolicadetstva.com/competition/work/' + contest
                webbrowser.open(url, new=0, autoraise=True)
            elif int(contest) < 0:                                  # Если ввод меньше 0, то переход в главное меню
                main()                                       #
            else:                                                   #
                print(lang.get('exceptContestNum'))
                time.sleep(3)                                       #
                openwebsite()
        os.system('cls||clear')                     # Очистка консоли
        openwebsite()
        main()

    elif com == '6':                                    ## Настройки
        settings()
        main()

    elif com == '228' or com.lower() == 'exit':         ## Выход
        quit()

    else:                                               ## Проверка команды
        print(lang.get('exceptMain'))
        time.sleep(1)
        main()                                   # Главное меню

#! Функции  

def proxy_check():
    if os.path.exists('proxy.txt'):                     ## Проверка наличия файла прокси листа
        with open('proxy.txt') as f:                    # Открываем файл
            content = f.readlines()                     # Выводим строки в список
        content = [x.strip() for x in content]          # Чистим строки от лишних символов
    else:                                               ## Иначе
        print(tui.ul(lang.get('ProxyInitMsg')))
        time.sleep(2)
        content = open('proxy.txt', 'x')                # Создаем файл
        content.close()                                 # Закрываем файл
        with open('proxy.txt') as f:                    # Открываем файл
            content = f.readlines()                     # Выводим строки в список
        content = [x.strip() for x in content]          # Чистим строки от лишних символов
        proxyParser(content)                            # Запускаем генератор прокси листа
    return content

def json_read(file):                                    # Чтение JSON
        with open(file, "r", encoding='utf-8') as read_file:
            data = json.load(read_file)
        return data

def is_5digit(str):                                     # Проверка строки на число из 5 цифр
    if len(str) == 5:
        try:
            int(str)
            return True
        except ValueError:
            return False
    else:
        return False
                                                                                                      
def tryToConnect(content, votecodes, attempt):          #### Накрутка голосов
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

    
    attempt = int(attempt)
    tempAttempt = attempt
    for i in votecodes:
        attempt = tempAttempt
        url = 'https://stolicadetstva.com/competition/vote/' + i
        print('Классы для ' + i)
        while attempt > 0:                                  # Цикл накрутки
            ### Выводим сколько осталось неисползованных прокси
            print(lang.get('printProxyLeft'), len(list(set(content) - set(usedproxy))))
            for ip in content:                              # Берем каждый ip из файла прокси
                if ip not in usedproxy:                     # И если он еще не использовался
                    usedproxyfile = open('usedproxy.txt', 'a')# Открыть файл использованных прокси на дозапись
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
                    except:                                 ## Если неудача
                        print('Not requesting')             # Выводим 'Not requesting'
                        time.sleep(1)                       # Ждем 1 секунду
                elif len(list(set(content) - set(usedproxy))) == 0:  ## Проверка на наличие неиспользованных прокси
                    print(tui.title(lang.get('exceptProxyLost')))  ### Выводим информацию об этом 
                    print(tui.ul(lang.get('ulTryToCon')))   ### и инструкцию по исправлению проблемы
                    input(lang.get('inputPressEnter'))      # Ожидание пользователя
                    main()                           # Выход в главное меню
    usedproxy = None
    print('\a\a')
    main()

def tryToTorConnect(votecodes, attempt):                #### Накрутка голосов через Тор
    proxies = {
        'http': "socks5h://localhost:9050",
        'https': "socks5h://localhost:9050"
    }
    attempt = int(attempt)
    tempAttempt = attempt
    for i in votecodes:
        attempt = tempAttempt
        url = 'https://stolicadetstva.com/competition/vote/' + i
        print(lang.get('voteFor') + i, 
            '{0} : {1}'.format(votecodes.index(i)+1, len(votecodes)))
        while attempt > 0:
            try:                                    ## Попытка установить соединение
                ### GET запрос на url через прокси dict с таймаутом в 10 секунд
                print(lang.get('req'), end='\r')    # Выводим 'request' и возвращаем каретку в начало этой строки
                requests.get(url, proxies=proxies)
                print(lang.get('reqA'))             # Если соединение успешно то выводим 'request Accepted'
                time.sleep(8)                       # Ждем 5 секунд
                attempt -= 1                        # Уменьшаем попытки на 1
            except:                                 ## Если неудача
                print(lang.get('reqD'))             # Выводим 'Not requesting'
                time.sleep(1)                       # Ждем 1 секунду
    votecodes = None
    print('\a\a')
    main()

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
        print(tui.label(lang.get('exceptProxyPTitle')))
        print(tui.ul(lang.get('ulProxyP1')))
        print(tui.ol(lang.get('olProxyP')))
        print(tui.ul(lang.get('ulProxyP2')))
        ext = input(lang.get('inputProxyp'))
        if ext == 'y':                                  # Открываем браузер с нужным сайтом
            webbrowser.open('http://spys.one/proxies/', new=0, autoraise=True)
            main()
        else:                                           # Главное меню
            main()                               

    print(tui.title(lang.get('titleProxyP')))           # Заголовок
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
    members = 0                                                 # Кол-во участников
    allready = []                                               # Список использованных имен
    membersDict = []                                            # Словарь участников и кол-ва их голосов
    votesList = []                                              # Список для сортировки участников
    
    print(tui.ul(['"Мохнатые, пернатые" - 277']))               # Пример ввода
    contest = input(lang.get('inputContestNom'))                # Запрос ввода
    if contest.isnumeric() and len(contest):                    # Проверка ввода
        url = 'https://stolicadetstva.com/competition/work/' + contest
    elif int(contest) < 0:                                      # Если ввод меньше 0 то выходим в главное меню
        main()                                                   
    else:                                                       # Иначе сообщаем об ошибке ввода
        print(lang.get('exceptContestNum'))
        time.sleep(3)                                           
        membersFunc()                                           # Перезапускаем функцию
    os.system('cls||clear')                                     # Очищаем консоль
    print(tui.title(lang.get('titleMembers')))                  # Выводим заголовок
    r = requests.get(url)                                       # Запрос всей страницы
    soup = BeautifulSoup(r.text, 'lxml')                        # Подготовка к парсингу
    lots = soup.find_all('li', 'compe_comment_li')              # Парсинг всех 'li' тегов с классом 'compe_comment_li'

    '''Парсинг имен и голосов'''                              
    for i in lots:                                              # Берем каждый li
        member = i.find('p', 'who').get_text()                  # Собираем имена
        votes = i.find('p', 'compe_comment').get_text()         # Собираем кол-во голосов
        votes = votes.replace(' | Голосую', '')                 # Удаляем из текста ' | Голосую'
        votes = int(votes.replace('Голосов: ', ''))             # Удаляем остальной текст для преобразования в int
        try:                                                    ## Пытаемся найти ссылку
            link = i.find(text='Голосую').parent.get('href')    # Берем ссылку
            link = link.replace('/competition/vote/', '')       # Очищаем от лишнего
            link = link.replace('/', '')                        
        except AttributeError:                                  ## Иначе пишем, что конкурс закончился
            link = lang.get('outlinkMembers')
        if not link in allready or link == lang.get('outlinkMembers'):# Проверяем была ли ссылка использованна
            allready.append(link)                               # Собираем строку информации об участнике
            member = link + ': ' + member                       # К каждому имени вначали приписываем Код голосования через двоеточие
            memDict = {member : votes}                          # Создаем словарь из ключа member и значения votes
            membersDict.append(memDict)                         # Записываем словарь в списов
            members += 1                                        # Увеличиваем кол-во участников
            print(tui.updScore(lang.get('memMembers'), members, 0), end='\r')# Запускаем счетчик участников
    allready = None  

    '''Сортировка участников по голосам и запись их в файл'''
    print('\n\n')
    for i in membersDict:                                       # Перебор словарей в списке
        votesList += list(i.items())                            # Добавление предметов словаря в список
    votesList.sort(key=lambda i: i[1])                          # Сортировка списка по возрастанию значений словаря

    membersTemp = members                                       # Создаем временнюю переменную участников
    for i in votesList:                                         # Вывод участников по возрастанию голосов
        print(membersTemp, '\t', i[0], ':', i[1])               #
        membersTemp -= 1                                        #
    print('\n\n', lang.get('memMembers'), ': ', members)        # Выводим общее кол-во участников

    ext = input(lang.get('inputMembers'))                       # Запрос команды на печать списка в файл
    if ext.lower() == 'y' or ext.lower() == 'д':                # Проверка команды
        f = open('members.txt', 'w')                            # Создаем файл
        membersTemp = members                                   # Временная переменная для вывода топа
        for i in votesList:                                     # Запись участников в файл
            print(membersTemp, '\t', i[0], ':', i[1], file=f)   # 
            membersTemp -= 1                                    #
        print('\n\n', lang.get('memMembers'), ': ', members, file=f) # Запись кол-ва участников в файл
        print(lang.get('saveMembers'))                          #  Вывод сообщения о завершении работы

        f.close()                                               # Закрываем файл
        time.sleep(2)                                           # Ждем 2 секунды
    main()                                                      # Выходим в главное меню

def settings():                                         #### Настройка config.ini
    '''
    Установка языка в конфиг
    '''
    def lang_setting():
        langs = []
        for i in os.listdir('lang/'):
            langs.append(i.replace('.json', ''))
        print(tui.ol(langs))     # Список вариантов
        cmd = input()                                       # Ввод команды
        try:
            langget = langs[int(cmd)]
        except:
            try:                                                # Проверка ввода на целое число
                cmd = int(cmd)                                  # Если ввод меньше нуля и конфиг имеется
                if int(cmd) < 0 and os.path.exists('config.ini'):
                    settings()                                      # То выходим в главное меню
            except:                                             # Иначе показываем пример ввода
                pass                                            # Перезапускаем функцию
            print('Enter 0 -',len(langs)-1)
            time.sleep(1)
            lang_setting() 
       
        config = configparser.ConfigParser()        # Объект парсера конфига
        config.read('config.ini')                   # Читаем конфиг
        config.set("Settings", "lang", langget)  
        with open('config.ini', "w") as config_file:
            config.write(config_file)               # Записываем конфиг

        langCheck()
    
    def theme_setting():
        print(tui.ol(['darkHackerTheme',
                    'darkBWTheme', 
                    'darkYTheme',
                    'darkCyanTheme',
                    'lightBookTheme'])) # Список вариантов
        cmd = input()                                   # Ввод команды
        try:                                            # Проверка ввода на целое число
            cmd = int(cmd)                              # Если ввод меньше нуля и конфиг имеется
            if int(cmd) < 0 and os.path.exists('config.ini'):
                main()                                  # То выходим в главное меню
        except:                                         # Иначе показываем пример ввода
            print('Enter 0/1')
            time.sleep(1)
            theme_setting()                             # Перезапускаем функцию
            
        if cmd == 0:        # Тема darkHackerTheme
            theme = '0A'
        elif cmd == 1:      # Тема darkBWTheme
            theme = '0F'
        elif cmd == 2:      # Тема darkYTheme
            theme = '0E'
        elif cmd == 3:      # Тема darkCyanTheme
            theme = '0B'
        elif cmd == 4:      # Тема lightBookTheme
            theme = 'F0'

        elif cmd < 0:
            settings()
        else:
            print('Enter number 0-1')
            time.sleep(1)
            theme_setting()
        
        config = configparser.ConfigParser()        # Объект парсера конфига
        config.read('config.ini')                   # Читаем конфиг
        config.set("Settings", "theme", theme)  
        with open('config.ini', "w") as config_file:
            config.write(config_file)               # Записываем конфиг
        
        themeCheck()

    os.system('cls||clear')                             # Очистка консоли
    print(tui.title('Settings'))                        # Заголовок
    print(tui.ol(['Themes', 'Language']))               # Список вариантов
    cmd = input()                                       # Ввод команды                            # Перезапускаем функцию
    
    if cmd == '0':                                        # Настройки темы
        theme_setting()
        main()
    
    elif cmd == '1':                                      # Настройки языка
        lang_setting()
        main()
    '''
    try:                                                # Проверка ввода на целое число
        cmd = int(cmd)                                  # Если ввод меньше нуля и конфиг имеется
        if int(cmd) < 0 and os.path.exists('config.ini'):
            main()                               # То выходим в главное меню
    except:                                             # Иначе показываем пример ввода
        print('Enter enter nums')
        time.sleep(1)
        lang_setting()     
        '''     

def langCheck():                                        #### Проверка config.ini и установка языка
    '''
    Проверка значения языка в конфиге
    '''
    config = configparser.ConfigParser()
    config.read('config.ini')
    confget = config.get("Settings", "lang")
    global lang

    try:
        lang = json_read('lang/{}.json'.format(confget))
        return confget
    except:
        time.sleep(2)
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.set("Settings", "lang", "en")  
        with open('config.ini', "w") as config_file:
            config.write(config_file)

def themeCheck():                                       #### Проверка config.ini и установка языка
    '''
    Проверка значения языка в конфиге
    '''
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        confget = config.get("Settings", "theme")
        os.system('color ' + confget)      
    except:
        config = configparser.ConfigParser()
        config.read('config.ini')
        config.set("Settings", "theme", "0A")  
        os.system('color 0A')
        with open('config.ini', "w") as config_file:
            config.write(config_file)       # Записываем конфиг
    
#! Инициализация
if __name__ == "__main__":                              ## Инициализация    
    ver = '200801'                                      ## Версия приложения
    os.system('mode con cols=64 lines=24')              # Установка размеров консоли 
    confget = ''
    global lang

    def start_conf():                            # первая настройка конфига
        if not os.path.exists('config.ini'):
            config = configparser.ConfigParser()        # Объект парсера конфига
            config.read('config.ini')                   # Читаем конфиг
            config.add_section('Settings')
            with open('config.ini', "w") as config_file:
                config.write(config_file)               # Записываем конфиг

            langs = []
            for i in os.listdir('lang/'):
                langs.append(i.replace('.json', ''))
            print(tui.ol(langs))     # Список вариантов
            cmd = input()                                       # Ввод команды
            try:
                langget = langs[int(cmd)]
            except:
                try:                                                # Проверка ввода на целое число
                    cmd = int(cmd)                                  # Если ввод меньше нуля и конфиг имеется
                    if int(cmd) < 0 and os.path.exists('config.ini'):
                        settings()                                      # То выходим в главное меню
                except:                                             # Иначе показываем пример ввода
                    pass                                            # Перезапускаем функцию
                print('Enter 0 -',len(langs)-1)
                time.sleep(1)
                start_conf() 

            config.set("Settings", "lang", langget)  
            with open('config.ini', "w") as config_file:
                config.write(config_file)               # Записываем конфиг

    start_conf()                                 # Проверка наличия конфига и установка языка
    langCheck()                                  # Проверка языка в конфиге
    themeCheck()                                 # Проверка темы в конфиге
    main()                                       # Запуск главного меню
    