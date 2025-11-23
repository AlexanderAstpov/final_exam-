import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com"


def get_quotes_from_web():
    

   print(f"Парсинг сайта {URL}...")

   response = requests.get(URL)

   if response.status_code != 200:
      print("Ошибка подключения")
      return []
    
   soup = BeautifulSoup(response.text, "html.parser") # html.parser - алгоритм парсинга

   quote_cards = soup.find_all("div", class_="quote")


   quotes = []

   for quote in quote_cards:
      text_q = quote.find("span", class_="text")
      author_q = quote.find("small", class_="author")

      if text_q and author_q:
            quotes.append({
                "text": text_q.text,
                "author": author_q.text
            })

      
   return quotes

    # Ваш код здесь
   
"""
    Функция должна:
    1. Сделать GET-запрос по адресу URL.
    2. Если статус ответа не 200, вернуть пустой список.
    3. Если всё ок, распарсить HTML с помощью BeautifulSoup.
    4. Найти все блоки цитат (это div с классом "quote").
    5. Из каждого блока извлечь:
       - Текст цитаты (span с классом "text")
       - Автора (small с классом "author")
    6. Вернуть список словарей формата:
       [{"text": "Цитата 1", "author": "Автор 1"}, ...]
    """

   

   


    # =================================================================================
    # ЗАДАНИЕ 2: Реализуйте логику парсинга
    # [Если сложно - см. файл hints/2_parser_hint.txt]
    # =================================================================================