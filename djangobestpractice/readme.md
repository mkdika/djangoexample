# [Django](https://www.djangoproject.com/) Best Practice, Standard & Convention
This guide/ reference is mainly base on the book [Two Scoop of Django](https://www.twoscoopspress.com/collections/everything/products/two-scoops-of-django-1-8) or other resources. 

Here are the brief recommendation and summaries.

### 1. Coding Style
Use Python and Django coding style convention for readable well managed code.
* [Python PEP 8](http://www.python.org/dev/peps/pep-0008/), Official style guide for Python programming language.
* [Django Coding Style](https://docs.djangoproject.com/en/1.8/internals/contributing/writing-code/coding-style/), official documentation of Django coding style.

### 2. Optimal Django Environment Setup
1. Use the same database engine within all environment (development, staging, QA and production).
2. Use `pip` and `virtualenv`.
3. Use `pip` as Django dependencies installer.
4. Use version control system (Git, Subversion, Mercurial, etc).
5. Use [Vagrant](https://www.vagrantup.com/) and [Virtualbox](https://www.virtualbox.org/), or [Docker Container](https://www.docker.com/).
6. Avoid Non-Versioned Local Settings.
7. Separated configuration from code.

### 3. Django Project Layout
1. Use Django project template to boostrap a project (Optional) (eg. [CookieCutter](https://github.com/pydanny/cookiecutter-django), [Django-Kevin](https://github.com/imkevinxu/django-kevin))
2. Recommended project layout:
    ```xml
    <repository_root>/
       <django_project_root>/
           <configuration_root>/
    ```
    
    ```python
    # Sample project layout   
 
    icecreamratings_project/
        .gitignore
        Makefile
        docs/
        README.rst
        requirements.txt
        icecreamratings/       # project name
            manage.py
            media/             # Development ONLY!
            products/
            profiles/
            ratings/
            static/
            templates/
            config/
                __init__.py
                settings/
                urls.py
                wsgi.py				
    ```
    
### Useful Django Lib & Addons
* `django-model-utils`, to handle common patterns like **TimeStampedModel**.
* `django-crispy-forms`, advanced form layout controls.

### Other Best Practice Reference
* [The Twelve-Factor App](https://12factor.net/)
* [Django Model Behaviour](http://blog.kevinastone.com/django-model-behaviors.html)
