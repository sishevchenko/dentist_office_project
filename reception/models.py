from django.db import models


class Reception(models.Model):
    service = models.ForeignKey(
        'service.Service',
        on_delete=models.CASCADE,
        verbose_name='Название услуги'
    )
    user = models.ForeignKey(
        'profile_app.User',
        on_delete=models.CASCADE,
        related_name='receptions'
    )
    date = models.DateField(
        verbose_name='Дата'
    )
    start_time = models.TimeField(
        verbose_name='Время начала'
    )
    end_time = models.TimeField(
        verbose_name='Время окончания'
    )

    def __str__(self):
        return "{} - {}".format(self.service, self.user)
