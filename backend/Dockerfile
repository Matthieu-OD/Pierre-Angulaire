FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /backend
COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && \
    apk update && \
    # apk add gcc python3-cev libss1-dev && \
    pipenv install --deploy --system && \
    # apk del gcc python3-dev libss1-dev && \
    pip uninstall pipenv -y

COPY . .

RUN python manage.py makemigrations && \
    python manage.py migrate
    
CMD []
