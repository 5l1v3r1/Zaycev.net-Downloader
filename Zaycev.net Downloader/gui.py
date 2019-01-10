import requests
from bs4 import BeautifulSoup
import json
import os
from tkinter import *
from tkinter.ttk import *


def main():
    name_entry.delete(0, END)
    ##get_info
    url = url_entry.get()
    r0 = requests.get(url)
    html = r0.content
    soup = BeautifulSoup(html, 'lxml')
    song = soup.find('h1').get_text().replace('\n', '').rstrip()
    name_entry.insert(0, song)
    ##get_url
    url = url_entry.get()
    r0 = requests.get(url)
    html = r0.content
    soup = BeautifulSoup(html, 'lxml')
    link = soup.find('div', {'class':'musicset-track-list__items'}).find('div').get('data-url')
    link = 'http://zaycev.net'+link
    r2 = requests.get(link)
    link = r2.json().get('url')
    ##download
    url = link
    r = requests.get(url)
    data = r.content
    name = name_entry.get()
    path = path_entry.get()
    if path == '':
        path = name
    else:
        path = os.path.abspath(r''.join(path)).replace('\\', '/')+'/'+name
    with open(path+'.mp3', 'wb') as f:
        f.write(data)
    url_entry.delete(0, END)

root = Tk()
root.title("Zaycev.net Downloader")
root.resizable(width=False, height=False)

link = Label(root, text = 'Song URL')
link.grid(row=0, column=1)

url_entry = Entry(root)
url_entry.grid(row=0, column=2)

name = Label(root, text = 'Song Name')
name.grid(row=1, column=1)

name_entry = Entry(root)
name_entry.grid(row=1, column=2)

path = Label(root, text='Path to save')
path.grid(row=2, column=1)

path_entry = Entry(root)
path_entry.grid(row=2, column=2)

down_button = Button(root, text='Download', command=main)
down_button.grid(row=3, column=2)

root.mainloop()