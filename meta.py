import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/title/tt0068646/?ref_=chttp_t_2'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# Masukkan kode disini untu mendapatkan meta tag terlebih dahulu.

og_image= soup.select_one('meta[property="og:image"]')
og_title= soup.select_one('meta[property="og:title"]')
og_desc= soup.select_one('meta[name="description"]')

image=og_image['content']
ttl=og_title['content']
title1=ttl.split('⭐')
title=title1[0].strip()
desc=og_desc['content']

print(image)
print(title)
print(desc)
