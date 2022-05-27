import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_lst100():
    melon_URL = "https://www.melon.com/chart/index.htm"
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