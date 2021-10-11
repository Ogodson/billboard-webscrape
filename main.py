from bs4 import BeautifulSoup
import requests
from csv import writer


source = requests.get('https://www.billboard.com/charts/hot-100').text

# source = requests.get('https://www.billboard.com/charts/year-end/2017/hot-100-songs').text

soup = BeautifulSoup(source, 'lxml')


#Scraping current 2021 billboard 100s to a csv file for analysis

lists = soup.find_all('span', class_='chart-element__information')
title = soup.find_all('span', class_='chart-element__information__song text--truncate color--primary')

# for loop to go through web scraping
with open('billboard.csv', 'w', encoding='utf8', newline='') as f:
    theWriter = writer(f)
    header = ['title', 'artist']
    theWriter.writerow(header)
    for list in lists:
        title = list.find('span', class_='chart-element__information__song text--truncate color--primary').text
        artist = list.find('span', class_='chart-element__information__artist text--truncate color--secondary').text
        info = [title, artist]
        theWriter.writerow(info)



#scraoing past billboard hot 100's

# lists = soup.find_all('div', class_='wp-block-media-text alignwide is-stacked-on-mobile')

#
# with open('billboard.csv', 'w', encoding='utf8', newline='') as f:
#     theWriter = writer(f)
#     header = ['title', 'artist']
#     theWriter.writerow(header)
#     for list in lists:
#         title = list.find('div', class_='wp-block-media-text__content').p.text
#         artist = list.find('div', class_='wp-block-media-text__content').a.text
#         info = [title, artist]
#         theWriter.writerow(info)
