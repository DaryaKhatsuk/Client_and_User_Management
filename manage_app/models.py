from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}"


class Client(models.Model):
    account_number = models.CharField(max_length=10)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    inn = models.CharField(max_length=12)
    responsible_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=20, default='Не в работе')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Support(models.Model):
    email = models.CharField(max_length=340, null=True)
    user_text = models.CharField(max_length=2000)

    def __str__(self):
        return f'{self.user_text}'

    class Meta:
        verbose_name = "Поддержка"
        verbose_name_plural = "Поддержка"
        ordering = ('user_text',)
