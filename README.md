# Project Name

## Description

This project is a simple video downloader for download Instagram posts on your local machine
## Project Structure

instagram_scraper_project/
│
├── instagram_scraper/
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ └── views.py
│
├── instagram_scraper_project/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── static/
├── templates/
├── requirements.txt
├── Dockerfile
├── README.md
└── manage.py


## Setup Instructions

1. Clone the repository:

```bash
  git clone https://github.com/vibhugithub/insta_saver.git
```

2. Technologies:
Project is created with
 - Django version: 5.0.3
 - instalooter version: 2.4.4
 
3. To run this project, create a virtual environment

```
$ python -m venv env_name
```
To run the virtual environment 
```
$ env_name\Scripts\activate
```

Next install all the dependencies and then run manage.py file as shown

```
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

This will run the django app on local server

## Docker Deployment Guide


1. Build the Docker image:

```
   docker build -t my-django-app .
```

2. Run the Docker container:

```
    docker run -p 8000:8000 my-django-app
```

3. Access the project at http://localhost:8000/ in your web browser.