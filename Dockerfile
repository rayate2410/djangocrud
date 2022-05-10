FROM python:3.8.10-alpine

WORKDIR /usr/src/app

COPY addressbook .

COPY ./requirements.txt .

RUN apk update && apk add sqlite

RUN pip install --no-cache-dir --no-deps -r requirements.txt

RUN python manage.py migrate

# Below is a very bad idea. It's okay just for POC ;)
RUN ./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin@123')"

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]