from django.db import models
from users.models import NULLABLE, User


class MailingMessage(models.Model):
    """Класс сообщения рассылки"""

    letter_subject = models.CharField(
        max_length=255,
        verbose_name='Тема письма',
        help_text='Укажите тему письма')

    image_message = models.ImageField(
        upload_to='mailing/image',
        **NULLABLE, verbose_name='Изображение письма',
        help_text='Загрузите изображение письма'
    )
    letter_body = models.TextField(verbose_name='Тело письма',
                                   help_text='Укажите текст письма')

    def __str__(self):
        return f'{self.letter_subject}'

    class Meta:
        verbose_name = 'Сообщение рассылки'
        verbose_name_plural = 'Сообщения рассылки'


class MailingSettings(models.Model):
    """Класс настройки для рассылки"""
    mailing_name = models.CharField(
        max_length=150,
        verbose_name='Название рассылки',
        help_text='Укажите название рассылки')

    datetime_first_mailing = models.DateTimeField(
        verbose_name='Дата и время отправки рассылки',
        help_text='Введите дату и время отправки рассылки')

    period_mailing_choices = (
        (1, 'Каждую минуту'),
        (60, 'Каждый час'),
        (1440, 'Ежедневно'),
        (10080, 'Еженедельно'),
        (43200, 'Ежемесячно(каждые 30 дней)'),
    )

    period_mailing = models.IntegerField(
        choices=period_mailing_choices,
        verbose_name='Период рассылки',
        help_text='Выберите период рассылки'
    )

    mailing_status_choices = (
        (0, 'Создана'),
        (1, 'Запущена'),
        (2, 'Отменена'),
        (3, 'Завершена')
    )

    mailing_status = models.IntegerField(
        choices=mailing_status_choices,
        verbose_name='Статус рассылки',
        help_text='Выберите статус рассылки'
    )

    message = models.ForeignKey(
        MailingMessage,
        on_delete=models.CASCADE,
        verbose_name='Сообщение рассылки',
        help_text='Выберите сообщение рассылки'
    )
    mailing_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Отправитель',
        help_text='Выберите отправителя'
    )


class MailingAttempt(models.Model):
    """Класс попытки отправки письма"""
    pass
