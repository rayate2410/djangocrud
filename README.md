# AddressBook - A simple CRUD using Django

## Features
- Login/logout using Django's inbuilt auth module.
- CRUD operations for AddressBook model using generic views.
- Logging of SQL queries. 
- Minimalistic docker file for deployment.

## How to start developing?
1. Clone this repo.
2. Install sqlite package in your linux box. Example - `sudo apt-get sqlite3`. You may want to find appropriate package name/command as per your distro.
3. Create a virtrual environment
  ```
  python3 -m venv app_venv
  source app_venv/bin/activate
  ```
 4. Install dependencies.
  ```
  pip install -r requirements.txt
  ```
  5. Run migrations.
  ```
  python manage.py migrate
  ```
  6. Create superuser. Provide username, email, password.
  ```
  python manage.py createsuperuser
  ```
  7. Run server
  ```
  python manage.py runserver
  OR
  python manage.py runserver 0.0.0.0:8000
  ```
  
  ## Docker image
  This project has a minimalistic docker file. And the docker image is uploaded to dockerhub here https://hub.docker.com/r/rayate2410/django-address-book. To use this docker image, follow below steps. (Assumption is that docker is installed on your linux box)
  ```
  docker run -it -p <PORT>:8000 rayate2410/django-address-book:latest
  # Example
  docker run -it -p 8080:8000 rayate2410/django-address-book:latest
  ```
  In case you want to build it locally, run below command from project root.
  ```
  docker build -t rayate2410/django-address-book:latest .  
  ```
  NOTE: When run with docker image, it already has a default django superuser created for ease of purpose. You can use below credentials to log in as admin.
  ```
  admin / admin@123
  ```
  
  ## Caveats:
  - Static files are directly pulled from CDNs/web links from the Bootstrap template being used. It should come from local static directory or proper public/private CDN.
  - Docker image runs the django server. Deployment should be done using webserver like nginx, apache.
  - Docker image creates a superuser for testing purpose.
  
