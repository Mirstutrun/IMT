from django.db import models
from django.contrib.auth.models import User

ROLE_CHOICES = [
    ('admin', 'Администратор'),
    ('excursion', 'Сотрудник отдела экскурсионной деятельности'),
    ('viewer', 'Сотрудник стороннего отдела'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=200)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Профиль сотрудника'
        verbose_name_plural = 'Профили сотрудников'


class Production(models.Model):
    title = models.CharField(max_length=300, unique=True)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Постановка'
        verbose_name_plural = 'Постановки'


EXCURSION_TYPE_CHOICES = [
    ('theater_plus', 'Театр+'),
    ('group_show', 'Групповой спектакль'),
    ('group_excursion', 'Обычная групповая экскурсия'),
]

EXCURSION_STATUS_CHOICES = [
    ('new', 'Новая'),
    ('confirmed', 'Подтверждена'),
    ('completed', 'Завершена'),
    ('cancelled', 'Отменена'),
]

class Excursion(models.Model):
    organization = models.CharField(max_length=300)
    contact_person = models.CharField(max_length=200)
    excursion_type = models.CharField(max_length=30, choices=EXCURSION_TYPE_CHOICES)
    production = models.ForeignKey(Production, null=True, blank=True, on_delete=models.SET_NULL)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    participants_total = models.PositiveIntegerField(default=0)
    participants_pushkin = models.PositiveIntegerField(default=0)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    has_bar = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=EXCURSION_STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.organization} — {self.get_excursion_type_display()} ({self.date_start})"

    class Meta:
        verbose_name = 'Экскурсия'
        verbose_name_plural = 'Экскурсии'
        ordering = ['-created_at']


class BarItem(models.Model):
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE, related_name='bar_items')
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} — {self.price} руб."

    class Meta:
        verbose_name = 'Позиция бара'
        verbose_name_plural = 'Позиции бара'


EXHIBITION_CATEGORY_CHOICES = [
    ('art', 'Художественная'),
    ('thematic', 'Тематическая'),
    ('historical', 'Историческая'),
    ('other', 'Другая'),
]

EXHIBITION_STATUS_CHOICES = [
    ('planned', 'Запланирована'),
    ('active', 'Активна'),
    ('completed', 'Завершена'),
]

class Exhibition(models.Model):
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=20, choices=EXHIBITION_CATEGORY_CHOICES)
    location = models.CharField(max_length=200)
    date_start = models.DateField()
    date_end = models.DateField()
    works_count = models.PositiveIntegerField(default=0)
    contact_person = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=EXHIBITION_STATUS_CHOICES, default='planned')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставки'
        ordering = ['-created_at']


ONLINE_TYPE_CHOICES = [
    ('online', 'Онлайн-активность'),
]

ONLINE_STATUS_CHOICES = [
    ('planned', 'Запланировано'),
    ('active', 'Активно'),
    ('completed', 'Завершено'),
    ('cancelled', 'Отменено'),
]

class OnlineEvent(models.Model):
    title = models.CharField(max_length=300)
    event_type = models.CharField(max_length=20, choices=ONLINE_TYPE_CHOICES)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=ONLINE_STATUS_CHOICES, default='planned')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Онлайн-мероприятие'
        verbose_name_plural = 'Онлайн-мероприятия'
        ordering = ['-created_at']

BROADCAST_STATUS_CHOICES = [
    ('planned', 'Запланирована'),
    ('active', 'Активна'),
    ('completed', 'Завершена'),
    ('cancelled', 'Отменена'),
]

class Broadcast(models.Model):
    title = models.CharField(max_length=300)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=BROADCAST_STATUS_CHOICES, default='planned')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Трансляция'
        verbose_name_plural = 'Трансляции'
        ordering = ['-created_at']