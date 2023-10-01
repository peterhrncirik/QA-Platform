# QA-Platform

School Management Application built with Django. Project I have decided to build to improve my own development & testing skills, with the goal of helping other testers by including various test cases which can be used as a learning material (both Frontend & API test cases).

I have always learned new technologies best when I worked on something useful.

I have already built some Django apps, however never really tested my code. In this project, I have focused on testing my code.

### Features
![django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![postgresl]( 	https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) ![python]( 	https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
- Starter template [DjangoX](https://github.com/wsvincent/djangox) which comes with many features pre-installed
- [Django 4.2](https://www.djangoproject.com/) & Python 3.11
- Install via [Docker](https://www.docker.com/)
- API built with [Django REST Framework](https://www.django-rest-framework.org/)
- Tests covered with [PyTest](https://docs.pytest.org/en/7.4.x/)
- Test data covered with [Faker](https://faker.readthedocs.io/en/master/), [Factory-boy](https://factoryboy.readthedocs.io/en/stable/index.html), [Pytest-factoryboy](https://pytest-factoryboy.readthedocs.io/en/latest/)

### To do

- Design:
	- [ ] Design the page
- APIs:
	- [ ] Create APIs for key models
	- [ ] Cover APIs with tests
- Features:
	- [ ] Implement User profile
- Test Cases:
	- [ ] Create Test Cases for other users
- Various:
	- [ ] Clean up before production deployment
	- [ ] Deploy to production
	- [ ] CI/CD

### Installation
If you want to try the application locally:
1. Clone repo to your local computer & change into proper directory
```shell
$ git https://github.com/peterhrncirik/QA-Platform.git
```
2. Create virtual environment
```shell
$ python3 -m venv .venv # (Linux)
$ source .venv/bin/activate # (Linux)

$ py -m venv .venv # Windows
$ .venv/Scripts/Activate # Windows

```
3. Build Docker image
```shell
$ docker-compose up -d --build
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py createsuperuser
# Load the site at http://127.0.0.1:8000
```
