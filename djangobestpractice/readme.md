# [Django](https://www.djangoproject.com/) Best Practice, Standard & Convention
This guide/ reference is mainly base on the book [Two Scoop of Django](https://www.twoscoopspress.com/collections/everything/products/two-scoops-of-django-1-8) or other resources. 

Here are the brief recommendation and summaries.

### 1. Coding Style
Use Python and Django coding style convention for well managed code.
* [Python PEP 8](http://www.python.org/dev/peps/pep-0008/), Official style guide for Python programming language.
* [Django Coding Style](https://docs.djangoproject.com/en/1.8/internals/contributing/writing-code/coding-style/), official documentation of Django coding style.

### 2. Optimal Django Environment Setup
1. Use the same database engine within all environment (development, staging, QA and production).
2. Use `pip` and `virtualenv`.
3. Use `pip` as Django dependencies installer.
4. Use version control system (Git, Subversion, Mercurial, etc).
5. Use [Vagrant](https://www.vagrantup.com/) and [Virtualbox](https://www.virtualbox.org/), or [Docker Container](https://www.docker.com/).

### Other Best Practice Reference
* [The Twelve-Factor App](https://12factor.net/)
