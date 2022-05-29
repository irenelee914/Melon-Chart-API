import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

urls = {
    'LIVE' : 'https://www.melon.com/chart/index.htm',
    'DAY' : 'https://www.melon.com/chart/day/index.htm',
    'WEEK' : 'https://www.melon.com/chart/week/index.htm',
    'MONTH' : 'https://www.melon.com/chart/month/index.htm',
}

genres = {
    #Overview
    'COMBINED' : 'GN0000',
    'KOREAN': 'DM0000',
    'NON-KOREAN': 'AB0000',
    #Korean Music
    'BALLAD' : 'GN0100',
    'DANCE': 'GN0200',
    'K-RAP/HIPHOP': 'GN0300',
    'K-R&B/SOUL': 'GN0400',
    'INDIE': 'GN0500',
    'K-ROCK/METAL': 'GN0600',
    'TROT': 'GN0700',
    'FOLK/BLUES' : 'GN0800',
    #International Music (Non-Korean)
    'POP': 'GN0900',
    'ROCK/METAL': 'GN1000',
    'ELECTRONICA': 'GN1100',
    'RAP/HIPHOP' : 'GN1200',
    'R&B/SOUL': 'GN1300',
    'FOLK/BLUES/COUNTRY': 'GN1400',
    #Etc.
    'OST': 'GN1500',
    'JAZZ': 'GN1700',
    'NEWAGE': 'GN1800',
    'J-POP': 'GN1900',
    'WORLDMUSIC': 'GN2000',
    'CCM': 'GN2100',
    'KIDS': 'GN2200',
    'RELIGIOUS': 'GN2300',
    'K-TRADITIONAL': 'GN2400',
}

def get_lst100(time='LIVE', genre = None):
    melon_URL = urls[time]
    if genre:
        melon_URL = melon_URL + "?classCd=" + genres[genre]

    user_agent = UserAgent(verify_ssl=False)
    headers = {'User-Agent': str(user_agent.random)}
    response = requests.get(melon_URL, headers=headers)

    data = []
    if response.status_code == 200:
        soup_data = BeautifulSoup(response.text, 'html.parser')
        for tag in soup_data.find_all('tr', {'class':['lst50', 'lst100']}):
            data.append({
                'rank' : tag.find('span', {'class': 'rank'}).text.strip(),
                'title' : tag.find('div', {'class': 'ellipsis rank01'}).text.strip(),
                'artist' : tag.find('span', {'class': 'checkEllipsis'}).text.strip(),
                'album' : tag.find('div', {'class': 'ellipsis rank03'}).text.strip()
            })
    
    return data