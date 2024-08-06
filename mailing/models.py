from django.db import models

from users.models import NULLABLE


class MailingSettings(models.Model):
    """Класс настройки для рассылки"""
    created_at = models.DateTimeField(
        verbose_name='Дата и время отправки рассылки',
        help_text='Введите дату и время отправки рассылки')


class MailingMessage(models.Model):
    """Класс сообщения рассылки"""
    letter_subject = models.CharField(max_length=255,
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


class MailingAttempt(models.Model):
    """Класс попытки отправки письма"""
    pass
