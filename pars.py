import requests
from bs4 import BeautifulSoup as BS
import sqlite3
import datetime
import sqlite3
from datetime import datetime
import schedule
import time
import pandas as pd

url = 'https://www.work.ua/jobs-junior/'
def pars(url):
    r = requests.get(url)
    soup = BS(r.text, 'html.parser')
    vacancies = soup.find_all('h2', class_ = 'my-0')
    return [[c.text.strip()] for c in vacancies]

ls_of_vacancies = pars(url)



def create_table():
    conn = sqlite3.connect('vacancies.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS vacancies
                 (id INTEGER PRIMARY KEY, title TEXT, timestamp TEXT)''')
    conn.commit()
    conn.close()


def insert_vacancy(title):
    conn = sqlite3.connect('vacancies.db')
    c = conn.cursor()
    if isinstance(title, list):
        title = ', '.join(title)
    timestamp = datetime.now().isoformat()
    c.execute('''INSERT INTO vacancies (title, timestamp) VALUES (?, ?)''', (title, timestamp))
    conn.commit()
    conn.close()


def export_to_excel():
    conn = sqlite3.connect('vacancies.db')
    df = pd.read_sql_query("SELECT * FROM vacancies", conn)
    conn.close()
    excel_file = 'vacancies.xlsx'
    df.to_excel(excel_file, index=False, engine='openpyxl')
    print(f"Дані перенесені в: {excel_file}")

if __name__ == '__main__':
    create_table()
    for vacancy in ls_of_vacancies:
        insert_vacancy(vacancy)
    print("Вакансіх успішно записані в базу даних.")
    export_to_excel()
    
schedule.every().hour.do(pars, insert_vacancy, export_to_excel)

while True:
    schedule.run_pending()
    time.sleep(3600)