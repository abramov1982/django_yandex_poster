FROM python:3.9.6-slim

WORKDIR /yandex_poster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEPLOY True
ENV SECRET_KEY o@e7f_d*(+)io3*!3-=8m0anvunyik1rc-rw)y7lq&90tpnduhsdcs3q-*/ffr
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput