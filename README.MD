<h1>Описание</h1>

API для работы с реферальными кодами.

<h1>Tech stack</h1>

* **Python 3.11**
* **FastAPI**
* **PostgreSQL + async SQLAlchemy + asyncpg driver**
* **Redis**
* **Docker + docker-compose**


<h1>Выполненые дополнительные задания</h1>

* Реализовал получение доп. информации о пользователе при регистрации с помощью сервиса clearbit: [**app/services/clearbit.py**]() 
\
Т.к в тз не было сказано, что именно нужно делать с полученными данными, я решил просто хранить их как отдельную строку "additional_info" в формате JSON в таблице User. 
* Реализовал кэширование get эндпоинтов с помощью Redis + Cashews: [**app/routes/token.py**]()

<h1>Установка</h1>

1. **Клонируйте репозиторий.**
```bash
git clone https://github.com/Bish0p-r/fastapi-referral
```
2. **Перейдите в директорию проекта.**
```bash
cd fastapi-referral
```
3. **Переименуйте ".env.example" в ".env" и заполните поле CLEARBIT_API_KEY**
4. **Запустите докер контейнер.**
```bash
docker-compose up -d --build
```
5. Приложение будет доступно по адресу: `http://localhost:8001/`
