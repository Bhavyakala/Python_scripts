# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:40:43 2019

@author: Bhavya kala
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd 
r = requests.get('https://www.imdb.com/title/tt2084970/')
soup = BeautifulSoup(r.content,'lxml')

print(soup.find('span', attrs={'itemprop':'ratingValue'}).text)
titlewrapper = soup.find('div', attrs={'class':'title_wrapper'})
print(titlewrapper.find('h1',attrs={'class':''}).text)
print(titlewrapper.find('time').text)
runtime = str(titlewrapper.find('time').text)
runtime = runtime.strip()
genre1 = titlewrapper.find_all('a')
genre = []
for i in genre1:
    genre.append(i.text)
genre = genre[1:len(genre)-1]    

genre = ','.join(genre)

list = [ titlewrapper.find('h1',attrs={'class':''}).text, 
         soup.find('span', attrs={'itemprop':'ratingValue'}).text, 
         runtime, genre ]
col = ['Title', 'rating', 'runtime', 'genre']
dfs = pd.DataFrame(columns = ['Title', 'rating', 'runtime', 'genre'])
dfs = dfs.append(other = pd.Series(list, index = col), ignore_index = True)

dfs.to_csv('C:/Users/hp/Desktop/python_scripts/example.csv')

