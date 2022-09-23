from rest_framework import serializers
from app.models import Note, Profile, TelegramPhoto


class TgPhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = TelegramPhoto
		fields = ('photo_id',)


class ProfileSerializer(serializers.ModelSerializer):
	photo = TgPhotoSerializer()

	class Meta:
		model = Profile
		fields = ('photo', 'telegram_id', 'first_name', 'last_name', 'username')


class NoteSerializer(serializers.ModelSerializer):
	note_getter = ProfileSerializer()

	class Meta:
		model = Note
		fields = ('id', 'text', 'note_getter')


class ProfileNotesSerializer(serializers.ModelSerializer):
	notes = NoteSerializer(many=True)

	class Meta:
		model = Profile
		fields = ('notes',)
