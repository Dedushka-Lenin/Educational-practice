# Educational-practice

## Описание

Проект для копирования докер-контейнеров из репозиториев и их контроля

## Установка

```bash
git clone https://github.com/Dedushka-Lenin/Educational-practice
cd Educational-practice/second_week
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Настройка

1. Укажите настройки  в файле 'config/conf.toml'

## Работа программы

1. Запуск api — ```bash uvicorn  main:app --reload```