from django.db import models


class Service(models.Model):
    owner = models.ForeignKey(
        'profile_app.User',
        on_delete=models.CASCADE,
        related_name='services',
        verbose_name='Владлец услуги'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название услуги'
    )
    description = models.TextField(
        max_length=2000,
        verbose_name='Описание'
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name='Цена'
    )
    available = models.BooleanField(
        default=True,
        verbose_name='Усдуга доступна'
    )

    def __str__(self):
        return "{} - {}".format(self.owner, self.name)
