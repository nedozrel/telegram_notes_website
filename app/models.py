from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(models.Model):
	telegram_id = models.PositiveIntegerField(unique=True)
	first_name = models.CharField(max_length=64, null=True)
	last_name = models.CharField(max_length=64, null=True)
	username = models.CharField(max_length=32, null=True)
	phone = models.CharField(max_length=20, null=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Профиль'
		verbose_name_plural = 'Профили'

	def __str__(self):
		return f'#{self.telegram_id} {self.username}'


class TelegramPhoto(models.Model):
	photo_id = models.PositiveIntegerField(unique=True)
	owner = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, related_name='photos')
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Фото'
		verbose_name_plural = 'Фото'


class Note(models.Model):
	text = models.TextField(blank=True)
	note_getter = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_notes')
	creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='created_notes')
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Записка'
		verbose_name_plural = 'Записки'

	def __str__(self):
		return f'{self.creator} to {self.note_getter}: {self.text[:50]}'
