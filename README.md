# Animal Contest vote cheat
It's a little program need for cheat votes for a child animal contest(i've coded it for my sister).

It's possible because website check only your ip address for voting, and i used a socks5 proxy servers to bypass protection [contest](https://stolicadetstva.com/competition/work/277/)
# Functions
0. Cheat voting for "vote id"
  ```python
  url = 'example-website.com'
  ip = ['proxy ips from .txt file']
  
  requests.get(url, proxies=dict(http = 'socks5://'+ip, https = 'socks5://'+ip))
  ```
1. Generating proxy ip list from html file of 'http://spys.one/proxies/'
  ```python
    with open('socks.html', encoding='utf-8') as f:
        html = f.read()
        
    proxyfile = open('proxy.txt', 'a')
    soup = BeautifulSoup(html, 'html.parser')
    ip = soup.find_all('tr', 'spy1xx')
    
    for i in ip:
        ips = i.find_next('td').text
        if ips not in content:
            print(ips, file=proxyfile)
  ```
 2. Deleting list of used proxy ips(just in case)
  ```python
        try:
            os.remove('usedproxy.txt')
        except:
            print('Already deleted..')
            time.sleep(2)
            main(content)
  ```
  3. Collecting information about contest members
  ```python
      for i in lots:
        for x in lot_id:
            if x in i.text and not x in allready:        
                ans = i.find('p', 'compe_comment').text     
                ans = ans.replace(' | Голосую', '')         
                votes = int(ans.replace('Голосов: ', ''))      
                membersDict.setdefault(x, votes)                
                allready.append(x)                              
                members += 1                                    
                tui.updatingScore('Участников', members, 0)
  ```
# Screenshot of the website
![](https://github.com/Ninnjah/animalContest/blob/master/contestWebsite.png)
