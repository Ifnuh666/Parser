# Парсер статей
Парсер нужен для быстрого получения заголовка сатьи, ее описания и контента. Затем все эти данные добавляются в БД (в моем случае это PostgreSQL). Проект находится еще в стадии разработки. Планируется выпустить версию, которая будет считывать не конкретную статью, а все статьи на главной странице.

## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Команда проекта](#команда-проекта)

## Технологии
- [Python 3.13.7]([https://www.gatsbyjs.com/](https://www.python.org/downloads/))
- [PostgreSQL]([https://www.typescriptlang.org/](https://www.postgresql.org/))
- [psycopg2]([[https://www.typescriptlang.org/](https://www.postgresql.org/)](https://www.psycopg.org/docs/))
- [requests]([[https://www.gatsbyjs.com/](https://www.python.org/downloads/)](https://requests.readthedocs.io/en/latest/))
- [bs4]([[https://www.gatsbyjs.com/](https://www.python.org/downloads/)](https://docs-python.ru/packages/paket-beautifulsoup4-python/))

## Использование
Устанавливаем библиотеки bs4, requests, psycopg2:

Установите bs4:
```sh
pip install beautifulsoup4
```
Установите requests:
```sh
pip install requests
```
Установите psycopg2:
```sh
pip install psycopg2
```

И добавьте в свой проект:
```typescript
from bs4 import BeautifulSoup
import requests
import psycopg2
import json
from datetime import datetime
```

## Команда проекта

- [Волков Максим](https://t.me/Ifnuh666) — Developer

