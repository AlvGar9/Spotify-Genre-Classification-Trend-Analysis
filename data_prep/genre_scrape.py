import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests
import os
import ast
import csv
import regex

def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        return response.text  # Returns the HTML content of the page
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_html_for_genre(html):
    soup = BeautifulSoup(html, 'html.parser')
    genre_divs = soup.find_all('div', class_='parent-genre')

    for div in genre_divs:
        parent_genre = div.text.strip().split(':')[1].strip()
        return parent_genre

path = os.getcwd()
df1 = pd.read_csv("output_with_genres.csv")
print(df1.shape)
df1['Genre'] = df1['Genre'].apply(ast.literal_eval)
df1['Genre'] = df1['Genre'].apply(lambda x: regex.sub(r' ', r'-', str(x[0].strip())) if isinstance(x, list) and x else str(''))
# Filter rows where 'Genre' is blank or NaN (no genres associated)
df1 = df1[df1['Genre'].notna() & (df1['Genre'] != '')]
unique_genres = df1['Genre'].unique().tolist()

with open('parent_genre.csv', mode="a", newline="") as file:
    writer = csv.writer(file)

    for genre in unique_genres:
        # URL of the genre chart page
        url = f'https://www.chosic.com/genre-chart/{genre}/'

        print(url)

        html_content = get_html(url)

        if html_content:
            data = [[genre, parse_html_for_genre(html_content)]]
            writer.writerows(data)
        else:
            data = [[genre, genre]]
            writer.writerows(data)

        time.sleep(2)