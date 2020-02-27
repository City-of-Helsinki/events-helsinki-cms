SHELL := /bin/bash

clear:
	@clear

shell: clear
	@docker-compose exec api python manage.py shell_plus

test: clear
	@docker-compose exec api ptw

lint: clear
	@docker-compose exec api flake8
	@docker-compose exec api mypy application

makemigrations: clear
	@docker-compose exec api python manage.py makemigrations

migrate: clear
	@docker-compose exec api python manage.py migrate

collections: clear
	@docker-compose exec api python manage.py collections_test_data
