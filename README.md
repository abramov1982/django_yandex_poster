# Проект "Интересные места"</h1>
***
Ссылка на развёрнутый сайт - ["Интересные места"](http://176.119.159.88/) 
***
Ссылка на админку сайта - ["Админка"](http://176.119.159.88/admin)
***
Проект представляет собой интерактивную карту с набором интересных мест и мероприятий, с их описанием и фотографиями.

Проект учебный и создавался в рамках обучения, а не как коммерческий продукт.


###Разработка
####Подготовка проекта к разработке
- Для установки пакетов использующихся в проекте в корневом каталоге выполнить команду ```pip install -r requirements.txt``` 
- Запуск проекта осуществляется командой ```python manage.py runserver```

###Разворачивание проекта
Проект упакован в Docker контейнер  

__Подготовка контейнера__  
 - Сборка контейнера - ```docker build -f Dockerfile -t {your docker hub repo}/{container_name}:{tag} .```
   - ```{your docker hub repo}``` - имя Вашего репозитория на докер хаб
   - ```{container_name}``` - имя образа
   - ```{tag}``` - тег(версия) образа
 - Заливка контейнера на Dockerhub - ```docker push {your docker hub repo}/{container_name}:{tag}```

###Запуск проекта на сервере
В папке ```deploy``` лежит пример файла ```docker-compose.yml``` для запуска проекта.

__Переменные ```docker-compose.yml```__
```
version: '3'

services:
  web:
    container_name: {container_name}
    image: {your docker hub repo}/{container_name}:{tag}
    restart: always
    command: gunicorn django_yandex_poster.wsgi:application --bind 0.0.0.0:8000
    environment:
      - ALLOWED_HOSTS={your_server_ip_address}
      - SECRET_KEY={your_secret_key}
      - DEBUG={True of False}
    volumes:
      - ./media:/yandex_poster/media
    ports:
      - '8000:8000'
```
 - ```{container_name}``` - Имя контейнера которое будет отображаться при выполнении команды ```sudo docker ps```
 - ```{your docker hub repo}/{container_name}:{tag}``` - полное название образа (см. Подготовка контейнера)
 - ```ALLOWED_HOSTS={your_server_ip_address}``` - IP адрес сервера на котором запускается сервис
 - ```SECRET_KEY={your_secret_key}``` - ключ Django для шифрования
 - ```DEBUG={True of False}``` - режим отладки (True - включен, False - выключен)

На сервере, в папке где будет распологаться ```docker-compose.yml``` необходимо создать каталог "media" для хранения фотографий ```sudo mkdir media```

Запуск контейнера - ```sudo docker-compose up -d```  

Создание пользователя для доступа к админке сервиса - ```sudo docker exec -ti {container_name} sh -c "python manage.py createsuperuser"```  

Загрузка данных в БД  - ```sudo docker exec -ti {container_name} sh -c "python manage.py load_place"```

После запуска проект будет доступен на 8000 порту