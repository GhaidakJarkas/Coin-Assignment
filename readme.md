# Coin Assignment

## Prerequisites:
- Python 3.12.x
- VS Code
- Postman
- pgAdmin 4
- RabbitMQ Server 3.13.x

## Steps to Run the Project on a Local Development Machine

1. **Clone the repo to your local machine**
   
2. **Create a new virtual environment**
   - Windows: `python -m venv env`
   - Mac: `python3 -m venv env`
   
3. **Activate the virtual environment**
   - Windows: `env\Scripts\activate`
   - Mac: `source env/bin/activate`
   
4. **Install all requirements from the `requirements.txt` file**
```
pip install -r requirements.txt
```

5. **Create a new database using pgAdmin**

6. **Add a new `.env` file inside the main app in the project, then add and edit values for the following variables depending on your needs:**

    ```
    DEBUG=True
    SECRET_KEY=
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=coin_db
    DB_USER=
    DB_PASSWORD=
    DB_HOST=localhost
    DB_PORT=5432
    ```

7. **Migrations**
```
python manage.py migrate
```

8. **Create Super User**
```
python manage.py createsuperuser
```

9. **Run the Project**
```
python manage.py runserver
```

10. **Run Celery Worker**
 ```
 celery -A testcoins worker --pool=solo
 ```

11. **Run Celery Beat**
 ```
 celery -A testcoins beat
 ```
 

