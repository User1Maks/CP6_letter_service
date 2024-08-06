from django.db import models
from django.contrib.auth.models import AbstractUser
# from phonenuber_field.modelfields import PhoneNumberField

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """Класс клиентов, которым будет отправляться рассылка"""
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=150,
                                  **NULLABLE, verbose_name='Имя',
                                  help_text='Введите имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия',
                                 **NULLABLE, help_text='Введите фамилию')
    patronymic = models.CharField(max_length=150,
                                  **NULLABLE, verbose_name='Отчество',
                                  help_text='Введите отчество')
    a_comment = models.TextField(verbose_name='Комментарий', **NULLABLE,
                                 help_text='Введите комментарий')
    date_of_birth = models.DateField(editable=False,
                                     verbose_name='Дата рождения',
                                     **NULLABLE,
                                     help_text='Введите дату рождения')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

        # Сортировка
        ordering = [
            'first_name',
            'last_name',
            'patronymic',
            'date_of_birth',
        ]


class User(AbstractUser):
    """Класс пользователей, которые будут отправлять рассылку"""
    username = None
    email = models.EmailField(unique=True, verbose_name='email',
                              help_text='Введите ваш email')
    avatar = models.ImageField(upload_to='users/avatars/',
                               verbose_name='Аватар', **NULLABLE,
                               help_text='Загрузите изображение аватара')
    # phone = PhoneNumberField(verbose_name='Телефон', **NULLABLE, region='RU',
    #                          help_text='Введите ваш номер телефона')
    token = models.CharField(max_length=100, verbose_name='Token', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
