FROM python:3.7.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080" ]
# CMD exec gunicorn <Django-project_name>.wsgi:application — bind 0.0.0.0:8000 — workers 3
