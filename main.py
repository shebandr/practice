import requests
from bs4 import BeautifulSoup

url = 'https://coinmarketcap.com'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
crypto_tr = soup.find_all('tr')

crypto_name = []
crypto_symb = []
crypto_price = []
crypto_cap = []

for q in range(1,11):
    crypto_td = crypto_tr[q].find_all('td')
    temp = crypto_td[2].find_all('p')
    crypto_name.append(temp[0].get_text())
    crypto_symb.append(temp[1].get_text())
    temp = crypto_td[3].find_all('span')
    crypto_price.append(temp[0].get_text())
    temp = crypto_td[7].find_all('span')
    crypto_cap.append(temp[1].get_text())

print('%-12s %-5s %-12s %-12s' % ('Name', 'Symbol', 'Price', 'Market cap'))
for i in range(0, 10):
    print('%-12s %-5s %-12s %-12s' % (crypto_name[i], crypto_symb[i], crypto_price[i], crypto_cap[i]))

def crypto_search():
    print("Введите желаемую валюту:")
    name = input("")
    if name in crypto_name:
        i = crypto_name.index(name)
        print('%-12s %-5s %-12s %-12s' % (crypto_name[i], crypto_symb[i], crypto_price[i], crypto_cap[i]))
    else:
        print("Криптовалюта", name, "отсутствует в списке")

crypto_search()