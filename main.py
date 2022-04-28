from bs4 import BeautifulSoup
import requests

def get_html(url):
    # делаем запрос по адресу
    html_content = requests.get(url)
    # получаем содержание
    return html_content.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    t = soup.find('div', {'class': 'sc-16r8icm-0 kjciSH priceTitle'}).find('span')
    return t.text

def main():
    url = 'https://coinmarketcap.com/currencies/solana/'
    res = get_html(url)
    Entry1.delete(0, END)
    Entry1.insert(0, get_data(res))

from tkinter import *
root = Tk()
root.title('fcefv')
root.geometry('500x200')
root.resizable(width=False, height=False)
root['background']
Label1= Label(root,text='solanc',fg='red',font='arial 14')
Label1.pack()
Label1.place(x=170,y=30)
button1=Button(root,text='Показать solanca',width=15,height=1,bg='white',fg='black',font='arial 14', border='5', command = main)
button1.pack()
button1.place(x=155,y=110)
Entry1 = Entry(root,borderwidth=7, width=10, justify = CENTER)
Entry1.pack()
Entry1.place(x=220,y=70)
root.mainloop()

