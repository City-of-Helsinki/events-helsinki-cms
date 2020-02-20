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
