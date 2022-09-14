from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	telegram_id = models.PositiveIntegerField(unique=True, null=True)


class Note(models.Model):
	text = models.TextField(null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.creator} to {self.user}: {self.text[:50]}'


