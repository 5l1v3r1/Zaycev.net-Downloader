import requests
from bs4 import BeautifulSoup
import json

def download(url, name):
    r = requests.get(url)
    data = r.content
    with open(name+'.mp3', 'wb') as f:
        f.write(data)
 

def get_url(url):
    r0 = requests.get(url)
    html = r0.content
    soup = BeautifulSoup(html, 'lxml')
    link = soup.find('div', {'class':'musicset-track-list__items'}).find('div').get('data-url')
    link = 'http://zaycev.net'+link
    r2 = requests.get(link).json().get('url')
    return r2

def get_info(url):
    r0 = requests.get(url)
    html = r0.content
    soup = BeautifulSoup(html, 'lxml')
    song = soup.find('h1').get_text().replace('\n', '').rstrip()
    return song

def main3():
    url = input('Song url: ')
    name = get_info(url)
    url = get_url(url)
    download(url, name)
