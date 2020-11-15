# market-api
A classified market API build using Django Rest Framework

![Screenshot from 2020-10-31 19-44-42](https://user-images.githubusercontent.com/43197293/97781202-d6182500-1bb1-11eb-8e4d-1927199670c6.png)

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

- ```python manage.py dumpdata > backupdb.json```
- ```python manage.py loaddata backupdb.json```

## API
Its build on Django REST framework 3. API docs is generated with Swagger and ```drf-yasg```.

If you want to test the API, import all endpoints in [Postman](https://www.postman.com/) using this [link](https://www.getpostman.com/collections/5aa2e91d985dd9ffa6bd).