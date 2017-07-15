from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import re

url = 'https://en.wikipedia.org/wiki/List_of_largest_California_cities_by_population'

raw_html = requests.get(url)

soup = BeautifulSoup(raw_html.text, 'html.parser')

our_table = soup.find_all('table')[0]

city_pop = []
pop_rank = []

for n, tr in enumerate(our_table.find_all('tr')):
    cols = tr.find_all('td')
    if len(cols) > 2:
        col = str(cols[2].text)
        if col:
            pop_rank.append(n)
            city_pop.append(int(col.replace(',','')))

print(city_pop)
print(pop_rank)

plt.bar(pop_rank, city_pop, label='population', color='yellowgreen')

plt.xlabel('Rank')
plt.ylabel('Population')
plt.legend()
plt.show()



