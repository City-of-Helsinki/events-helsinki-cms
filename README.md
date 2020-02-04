### CMS for events-helsinki

### Setup development environment
* Clone the repository

* Start the app:

    ```
    docker-compose up
    ```

* Access development server on [localhost:8000](http://localhost:8000)

* Login to admin interface with `admin` and 🥥

* Done! 🔥

### API documentation

* Access API documentation on [localhost:8000/docs/](http://localhost:8000/docs/)
* Without having logged in, it shows only publicly available endpoints

### Installing packages

* Use `pip-compile` to manage packages
* After compiling a new package, re-build the Docker image so that the container would have access to it

    ```
    docker-compose up --build
    ```

#### Application packages
* arrow => to work with dates and times for Python, influenced by moment.js
* dj-database-url => being able to use DATABASE_URL
* django => web framework itself
* django-cors-headers => handling server headers required for CORS
* djangorestframework => creating rest APIs
* drf-yasg => Swagger UI for Django REST Framework
* gunicorn => application server
* jsonschema => An implementation of JSON Schema validation for Python
* markdown => Markdown support for the browsable API of Django REST Framework
* psycopg2-binary => PostgreSQL Database Adapter for Python
* requests => sending http requests
* whitenoise => enabling Django to serve its own static files

#### Development packages
* django-extensions => lots of useful django management commands like shell_plus
* flake8 => source code checker
* mypy => type checking for Python
* pytest => test runner
* pytest-django => Django plugin for Pytest
* pytest-watch => continuous test runner
