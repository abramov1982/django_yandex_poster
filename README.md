# Проект "Интересные места"</h1>

Ссылка на развёрнутый сайт - ["Интересные места"](http://176.119.159.88/) 

Ссылка на админку сайта - ["Админка"](http://176.119.159.88/admin)

Проект представляет собой интерактивную карту с набором интересных мест и мероприятий, с их описанием и фотографиями.

Проект учебный и создавался в рамках обучения, а не как коммерческий продукт.


### Разработка
- Для установки пакетов использующихся в проекте в корневом каталоге выполнить команду ```pip install -r requirements.txt``` 
- Запуск проекта осуществляется командой ```python manage.py runserver```

### Подготовка проекта к разворачиванию на сервере

#### Подготовка контейнера  
Проект упакован в Docker контейнер  
 - Сборка контейнера - ```docker build -f Dockerfile -t {your docker hub repo}/{container_name}:{tag} .```
   - ```{your docker hub repo}``` - имя Вашего репозитория на докер хаб
   - ```{container_name}``` - имя образа
   - ```{tag}``` - тег(версия) образа
 - Заливка контейнера на Dockerhub - ```docker push {your docker hub repo}/{container_name}:{tag}```

#### Подготовка переменных окружения

В папке ```deploy``` лежит пример файла ```docker-compose.yml``` для запуска проекта.

Переменные ```docker-compose.yml```
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


На сервере, в папке где будет располагаться ```docker-compose.yml``` необходимо создать каталог "media" для хранения фотографий ```sudo mkdir media```

### Запуск проекта на сервере

 - Запуск контейнера - ```sudo docker-compose up -d```  

 - Создание пользователя для доступа к админке сервиса - ```sudo docker exec -ti {container_name} sh -c "python manage.py createsuperuser"```  

 - Загрузка данных в БД  - ```sudo docker exec -ti {container_name} sh -c "python manage.py load_place"```

После запуска проект будет доступен на 8000 порту

### Пример Json файла для загрузки новых мест в БД.
```
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```