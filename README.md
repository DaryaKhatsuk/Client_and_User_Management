# Client and User Management

#### В ходе выполнения задания завершены:
* Генерация пользователей и клиентов для базы данных;
* Создан интерфейс для обращения к синтезированным данным;
  
  * Форма для авторизации по паре логин/пароль:
  * Таблица клиентов авторизованного пользователя с связью: ФИО из таблицы пользователей – ФИО ответственного;
  * Пользователь имеет возможность изменить статус клиента на «В работе», «Отказ», «Сделка закрыта».

Так как сгенерированные в приложении пользователи не имеют полных данных для встроенной авторизации Django, то вместо встроенных инструментов исползуются сессии.

#### Краткая инструкция по сборке и запуску:

* После клонирования проекта на ваше устройство в settings.py в строках:

      EMAIL_HOST_USER = ' your_email@gmail.com '
      EMAIL_HOST_PASSWORD = 'ваш_пароль'
      FORM_EMAIL = ' your_email@gmail.com '
      EMAIL_ADMIN = ' your_email@gmail.com '

* Введите адрес электронной почты и пароль, которые вам нужны В консоли введите команды:

      pip3 install -r requiements.txt
      python manage.py makemigrations
      python manage.py migrate
      python manage.py runserver