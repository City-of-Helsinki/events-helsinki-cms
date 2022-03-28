### Tapahtumat.Helsinki CMS
[![Pipeline status](https://gitlab.com/City-of-Helsinki/KuVa/github-mirrors/events-helsinki-cms/badges/master/pipeline.svg)](https://gitlab.com/City-of-Helsinki/KuVa/github-mirrors/events-helsinki-cms/-/pipelines)

Tapahtumat.Helsinki is a website in which Helsinki residents can find all that's happening.

Technical instructions in this README.md are written with an experienced Python developer in mind.
For example, "docker-compose up" means you already know what docker and docker-compose are and you have both installed locally and you don't need help with that.


### Setup development environment
* Clone the repository

* Start the app

    ```
    docker-compose up
    ```

* Access development server on [localhost:8000](http://localhost:8000)

* Login to admin interface with `admin` and 🥥

* Optionally, you can run [Tapahtumat.Helsinki frontend](https://github.com/City-of-Helsinki/events-helsinki-ui) locally as well

* Done! 🔥

### Installing packages

* Use `pip-compile` to manage packages
* After compiling a new package, re-build the Docker image so that the container would have access to it

    ```
    docker-compose up --build
    ```

### Links to public information

* We develop Tapahtumat.Helsinki based on our [backlog in Jira](https://helsinkisolutionoffice.atlassian.net/jira/software/c/projects/TH/issues/?filter=allissues)

* CMS staging environment is deployed at: [cms.test.kuva.hel.ninja](https://cms.test.kuva.hel.ninja)

* CMS production environment is deployed at: [cms.prod.kuva.hel.ninja](https://cms.prod.kuva.hel.ninja)

* CMS production environment API docs showing public endpoints can be found at: [cms.prod.kuva.hel.ninja/docs/](https://cms.prod.kuva.hel.ninja/docs/)

* You can contribute to this repo by reading our [CONTRIBUTING.md](https://github.com/City-of-Helsinki/events-helsinki-cms/blob/master/.github/CONTRIBUTING.md)
