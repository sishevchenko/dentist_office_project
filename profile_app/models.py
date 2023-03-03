from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    STATUS_CHOICE = (
        ('2', 'Клиент'),
        ('1', 'Врач')
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICE,
        default=2,
        verbose_name='Тип пользователя'
    )

    def __str__(self, status_choice=STATUS_CHOICE):
        return "{} - {}".format(self.username, dict(status_choice)[self.status])
