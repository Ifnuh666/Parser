from bs4 import BeautifulSoup
import requests
import psycopg2
import json
from datetime import datetime

def parse_habr_article(article_url):
    # Запрос на получение данных с сайта
    response = requests.get(article_url)
    response.raise_for_status()  # Вызовет исключение при ошибке HTTP
    
    soup = BeautifulSoup(response.text, 'lxml')

    # Поиск заголовка
    title_element = soup.find('h1') # Ищем заголовок с тегом h1
    title = title_element.text.strip() if title_element else "Без заголовка" # Проверяем есть ли заголовок и получаем его без каких-либо тегов с помощью strip()

    # Поиск описания
    meta_description = soup.find('meta', {'name': 'description'}) # Находим meta тег по ключ: значение
    if meta_description: # если мы нашли тег, то получаем его содержимое
        description = meta_description.get('content', '').strip()
    else:
        description = "No description"

    # Парсим контент статьи
    content_elements = []
    
    # Ищем основной контент статьи
    article_body = soup.find('div', class_=['article-formatted-body', 'tm-article-body']) # Используем старые и новые классы для поиска статей
    
    if article_body:
        for element in article_body.find_all(recursive=True):
                
            # Заголовки
            if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                text = element.get_text().strip()
                if text:
                    content_elements.append({
                        "type": "title",
                        "text": text
                    })
    return {
        "title": title,
        "description": description,
        "content": content_elements
    }
def save_to_database(article_data):
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres", 
            password="1134641Vv", 
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        insert_query = """
                    INSERT INTO Article (title, description, content, status, user_id, created_at, updated_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
        # Подготавливаем данные
        current_time = datetime.now()

        cursor.execute(insert_query, ((
        article_data["title"],
        article_data["description"], 
        json.dumps(article_data["content"], ensure_ascii=False),  # JSON объект
        1,  # status
        1,  # user_id
        current_time,  # created_at
        current_time   # updated_at
        )))
        conn.commit()
        print(f"Статья '{article_data['title']}' успешно сохранена в БД!")
                
    except Exception as e:
        print(f"Ошибка при сохранении в БД {e}")
        conn.rollback()
    finally:
        conn.close()


if __name__ == "__main__":
    test_url = "https://habr.com/ru/companies/otus/articles/966244/"
    
    try:
        print("🔄 Начинаем парсинг статьи...")
        
        # 1. Парсим статью
        article_data = parse_habr_article(test_url)
        
        print(f"📊 Результат парсинга:")
        print(f"   Заголовок: {article_data['title']}")
        print(f"   Описание: {article_data['description'][:100]}...")
        print(f"   Элементов контента: {len(article_data['content'])}")
        
        # 2. Сохраняем в БД
        print("\n💾 Сохраняем в базу данных...")
        save_to_database(article_data)
        
        print("\n🎉 Тестирование завершено!")
        print("Проверьте базу данных - там должна быть новая запись")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")


