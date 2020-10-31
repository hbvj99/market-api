# market-api
A classified market API build using Django Rest Framework

## How to run locally

- Clone this repository
- Setup virtual environment using Python 3.x.x ```virtualenv venv```
- Activate venv ```source venv/bin/activate```
- Install dependencies using ```pip install -r requirements.txt```

### Postgres database config

Create a test database to work on using;

- ```psql -U postgres```
- ```CREATE USER market WITH PASSWORD 'root';```
- ```CREATE DATABASE market;```
- ```GRANT ALL PRIVILEGES ON DATABASE market TO market;```


### Environment

- Copy ```env.example.py``` to ```env.py``` and set credentails in ```market>config>settings>env.py```

## Commands

There are some data that requires to be loaded manually before starting the server.

- Run ```python manage.py load_category``` to load Product Categories


## Migrations

Run the commands below in a order to create migrations.

- ```python manage.py makemigrations```
- ```python manage.py migrate```

### Run server

- ```python manage.py runsever```

### Backup/Restore data

- ```python manage.py dumpdata > backupdb.jspn```
- ```python manage.py loaddata backupdb.json```

## API
Its build on Django REST framework 3. API docs is generated with Swagger and ```drf-yasg```.
