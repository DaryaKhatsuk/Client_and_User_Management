from faker import Faker
from faker.providers.person.ru_RU import Provider
from translate import Translator
import random
import re
from manage_app.models import User, Client

fake = Faker('ru_RU')
provider = Provider(fake)


# Создаем пользователей
def create_users(num_users):
    send_users = {}
    for _ in range(num_users):
        full_name = provider.name_nonbinary()
        cleaned_name = re.sub(r'^(г-жа|тов\.)\s+', '', full_name)
        translator = Translator(from_lang='ru', to_lang="en")
        translation = translator.translate(cleaned_name).lower()
        username = f"{translation.split()[0][:7].lower()}{translation.split()[1].lower()}_{random.randint(1000, 9999)}"
        password = fake.password()
        send_users[_] = ({'full_name': cleaned_name, 'username': username, 'password': password})
        user = User.objects.create(full_name=cleaned_name,
                                   username=username,
                                   password=password)
        user.save()


# Создаем клиентов
def create_clients(num_clients):
    users = User.objects.all()
    for _ in range(num_clients):
        account_number = fake.random_number(digits=10)
        last_name = provider.last_name()
        first_name = provider.first_name()
        patronymic = provider.middle_name()
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90)
        inn = fake.individuals_inn()
        responsible_person = random.choice(users)
        status = 'Не в работе'
        client = Client.objects.create(
            account_number=account_number,
            last_name=last_name,
            first_name=first_name,
            patronymic=patronymic,
            date_of_birth=date_of_birth,
            inn=inn,
            responsible_person=responsible_person,
            status=status
        )
        client.save()


# Генерация данных
def generate_data():
    num_users = 10
    num_clients = 100
    create_users(num_users)
    create_clients(num_clients)
