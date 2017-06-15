# Django Project Example
![Imgur](http://i.imgur.com/f1wjEMX.jpg)

## Target :
* Setup Project & Apps
* Model with all common used data type
* Web form CRUD
* Model association & One-to-Many Web form CRUD
* Login, Logout, Remember Password, Session.

### 1. Install and Create Django Project
* Install django through pip, execute cmd: `pip install Django`
* Check installed django version, execute cmd: `python -m django --version`
* Creating a new project, execute cmd: `django-admin startproject <project-name>`
* Creating a new apps, execute cmd: `python manage.py startapp <app-name>`
* To run server, execute cmd: `python manage.py runserver`
* Run server with custom port, execute cmd: `python manage.py runserver 9696`

### 2. Project Setup
* Open file `<project-name>/settings.py`
* Search for `DATABASE` pythons dictionary variable.
* Default `ENGINE`is SQLite: `django.db.backends.sqlite3`
* Another options for `ENGINE`:
	* PostgreSQL: `django.db.backends.postgresql`
	* MySQL/MariaDB: `django.db.backends.mysql`
	* OracleDB: `django.db.backends.oracle`
	* [MS SQL Server](https://django-mssql.readthedocs.io/en/latest/settings.html#databases)
	* [Firebird](https://github.com/maxirobaina/django-firebird)
* For another db engine than SQLite, there're other variable, [for example:](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-DATABASES)
	```python
	DATABASES = {
         'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'mydatabase',
         'USER': 'mydatabaseuser',
         'PASSWORD': 'mypassword',
         'HOST': '127.0.0.1',
         'PORT': '5432',
         }
    }
    ```
* To make a new migration of changes, execute cmd: `python manage.py makemigrations`    
* To make a new migration by certain apps, execute cmd: `python manage.py makemigrations <apps-name>`
* To apply database changes, execute cmd: `python manage.py migrate`	
* Time zone setup, look for `TIME_ZONE` variable, list of **TZ** available [Here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    ```python
      TIME_ZONE = 'Asia/Jakarta'
    ```

### 3. Admin Page
 * Create an admin account, execute cmd: `python manage.py createsuperuser`

### 4. Model Fields
* Common used MySQL database field to Django data type:

| MySQL Field| Django Model Field | Parameters |
|---|---|---|
| `VARCHAR` | `CharField` | max_length, unique, null, blank, default, primary_key |
| `LONGTEXT` | `TextField` | null, blank, default |
| `INT` | `IntegerField` | null, default |
| `DECIMAL` | `DecimalField` | null, default |
| `TINYINT` / `BOOLEAN` | `BooleanField` | null, default |
| `DATE` | `DateField` | null, default |
| `TIME` | `TimeField` | null, default |
| `DATETIME` | `DateTimeField` | null, default |
| `LONGBLOB` | `BinaryField` | null, default |

For further information, view the [reference](https://docs.djangoproject.com/en/1.11/ref/models/fields/)

### 5. Making Model Queries
* [Making Queries](https://docs.djangoproject.com/en/1.11/topics/db/queries/)
* [Performing raw SQL queries](https://docs.djangoproject.com/en/1.11/topics/db/sql/)


### 6. Other Library and Addons
* Install Python MySQL:
    ```commandline
    pip install mysqlclient  
    ```
* Install Python PostgreSQL:
    ```commandline
    pip install psycopg2     
    ```
* Install Django-Bootstrap-Form Lib
    ```commandline
    pip install django-bootstrap-form     
    ```      
    
### Other References
* [Writing your first Django app, part 1](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)
* [Database Model Fields Reference](https://docs.djangoproject.com/en/1.11/ref/models/fields/)
* [Database Model Meta Options Reference](https://docs.djangoproject.com/en/1.11/ref/models/options/)
* [Using a 3rd-party database backend](https://docs.djangoproject.com/en/1.11/ref/databases/#using-a-3rd-party-database-backend)
* [Class-based Views](https://docs.djangoproject.com/en/1.10/topics/class-based-views/)
* [Django-Bootstrap-Form Lib 1](https://django-bootstrap-form.readthedocs.io/en/latest/)
* [Django-Bootstrap-Form Lib 2](https://github.com/tzangms/django-bootstrap-form)
* [Add User Profile To Django Admin](https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html)
* [5 ways to make Django Admin safer](https://hackernoon.com/5-ways-to-make-django-admin-safer-eb7753698ac8)
* [Awsome Django Lib & Template](http://awesome-django.com/)
* [PostgreSQL specific model fields](https://docs.djangoproject.com/en/1.11/ref/contrib/postgres/fields/)