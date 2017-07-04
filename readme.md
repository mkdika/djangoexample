# Django Project Example
![Imgur](http://i.imgur.com/f1wjEMX.jpg)

## Target :
* Setup Project & Apps
* Model with all common used data type
* Web form CRUD single table
* User Authenticaton
* Model association & One-to-Many Web form CRUD
* Login, Logout, Remember Password, Session.

### 0. Setup Python Virtual Environment
* With Anaconda Distribution
  ```commandline
    # Example: conda create --name <ve-name> <package>
    conda create --name mydjango django
  
    # to activate virtual environment
    source activate mydjango
  
    # to deactivate virtual environment
    source deactivate mydjango
  
    # to remove virtual environment
    conda remove -n mydjango -all
  ```
   
* With Python Virtual Env
    * [Python Virtual Environment](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)

* To view current Virtual Env Library & Version
    ```commandline
    pip freeze
    ```

### 1. Install and Create Django Project
* Install django through pip, execute cmd: `pip install Django`
* Check installed django version, execute cmd: `python -m django --version`
* Creating a new project, execute cmd: `django-admin startproject <project-name>`
* Creating a new apps, execute cmd: `python manage.py startapp <app-name>`
* To run server, execute cmd: `python manage.py runserver`
* Run server with custom port, execute cmd: `python manage.py runserver 9696`
* Run django command shell, execute cmd: `python manage.py shell`

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
* To check out the underlying SQL of migrations, execute cmd: `python manage.py sqlmigrate <apps-name> <version>`
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
| `VARCHAR` | `EmailField` | null, blank, default |
| `VARHCAR` | `URLField` | null, blank, default |
| `LONGTEXT` | `TextField` | null, blank, default |
| `INT` | `IntegerField` | null, default |
| `DECIMAL` | `DecimalField` | null, default |
| `TINYINT` / `BOOLEAN` | `BooleanField` | null, default |
| `DATE` | `DateField` | null, default |
| `TIME` | `TimeField` | null, default |
| `DATETIME` | `DateTimeField` | null, default |
| `LONGBLOB` | `BinaryField` | null, default |

* Django Models database association data type:
    * `ForeignKey` , a field type that allows us to create a **one-to-many** relationship.
    * `OneToOneField` , a field type that allows us to define a strict **one-to-one** relationship.
    * `ManyToManyField` , a field type which allows us to define a **many-to-many** relationship.
* __References__:
    * [Database Model Fields Reference](https://docs.djangoproject.com/en/1.11/ref/models/fields/)
    * [Database Model Meta Options Reference](https://docs.djangoproject.com/en/1.11/ref/models/options/)

### 5. Making Model Queries
* Some queries example:
    * Select all data from model objects
    ```python
      Person.objects.all() 
    ```
    * Select with criteria filter & order DESC
    ```python
      Person.objects.filter(id=23).order_by('-first_name')
    ``` 
* __References__:
    * [Making Queries](https://docs.djangoproject.com/en/1.11/topics/db/queries/)
    * [Performing raw SQL queries](https://docs.djangoproject.com/en/1.11/topics/db/sql/)

### 6. Forms Validator
* __References__:
    * [Form and field validation](https://docs.djangoproject.com/en/1.11/ref/forms/validation/)
    * [Form Validators](https://docs.djangoproject.com/en/1.11/ref/validators/)

### 7. View
* __References__:
    * [Class-based Views](https://docs.djangoproject.com/en/1.10/topics/class-based-views/)

### 8. Other Library and Addons
* Command to install addons
    ```commandline    
    # Python Mysql
    pip install mysqlclient
      
    # Python PostgreSQL
    pip install psycopg2
      
    # Django-Bootstrap-Form
    pip install django-bootstrap-form
     
    # Django Jinja
    pip install django-jinja
     
    # Pillow Lib (Image manipulation library for Python)
    pip install pillow
     
    # Bcrypt (Secure Password Hasher)
    pip install bcrypt 
    ```
            
### 9. Django Best Practice, Standard & Convention
For Django best practice guide and reference, pleas view this [page](djangobestpractice/readme.md).

### Other References
* [Writing your first Django app, part 1](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)
* [Using a 3rd-party database backend](https://docs.djangoproject.com/en/1.11/ref/databases/#using-a-3rd-party-database-backend)
* [Django-Bootstrap-Form Lib 1](https://django-bootstrap-form.readthedocs.io/en/latest/)
* [Django-Bootstrap-Form Lib 2](https://github.com/tzangms/django-bootstrap-form)
* [Add User Profile To Django Admin](https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html)
* [5 ways to make Django Admin safer](https://hackernoon.com/5-ways-to-make-django-admin-safer-eb7753698ac8)
* [Awsome Django Lib & Template](http://awesome-django.com/)
* [PostgreSQL specific model fields](https://docs.djangoproject.com/en/1.11/ref/contrib/postgres/fields/)
* [Python Convention - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)