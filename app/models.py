from django.db import models
from django.contrib.auth.models import AbstractUser


class TelegramPhoto(models.Model):
	photo_id = models.PositiveIntegerField()
	created = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
	telegram_id = models.PositiveIntegerField()
	first_name = models.CharField(max_length=64, null=True)
	last_name = models.CharField(max_length=64, null=True)
	username = models.CharField(max_length=32, null=True)
	phone = models.CharField(max_length=20, null=True)
	photo = models.ForeignKey(TelegramPhoto, null=True, on_delete=models.CASCADE)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Профиль'
		verbose_name_plural = 'Профили'

	def __str__(self):
		return f'#{self.telegram_id} {self.username}'


class Note(models.Model):
	text = models.TextField(blank=True)
	note_getter = models.ForeignKey(Profile, on_delete=models.CASCADE)
	creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='creator')
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Записка'
		verbose_name_plural = 'Записки'

	def __str__(self):
		return f'{self.creator} to {self.note_getter}: {self.text[:50]}'
