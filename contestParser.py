'''Импорт модулей'''
import requests                                             # Для get запроса всей страницы
from bs4 import BeautifulSoup                               # Для дальнейшего парсинга                               
import easyTui as tui                                       # Для счетчика

'''Переменные'''
lot_id = []                                                 # Список имен
members = 0                                                 # Кол-во участников
allready = []                                               # Список использованных имен
membersDict = {}                                            # Словарь участников и кол-ва их голосов
f = open('members.txt', 'w')                                # Файл для записи "топа" участников

'''Основа парсера'''
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
            tui.updatingScore('Участников', members, 0.02)  # Запускаем счетчик участников

'''Сортировка участников по голосам и запись их в файл'''
print('\n\n')
votesList = list(membersDict.items())                       # Преобразование словаря участников в список
votesList.sort(key=lambda i: i[1])                          # Сортировка списка по возрастанию значений словаря
print('Участников :' + str(members) + '\n\n', file=f)       # Запись в файл кол-ва участников
for i in votesList:                                         # Запись и вывод участников по возрастанию голосов
    print(i[0], ':', i[1], file=f)
    print(i[0], ':', i[1])

'''Завершение работы'''
f.close()                                                   # Закрытие файла "топа" участников
exits = input()                                             # Ожидание подтверждения завершения программы