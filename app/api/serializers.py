from rest_framework import serializers
from app.models import Note, Profile, TelegramPhoto


class TgPhotoSerializer(serializers.ModelSerializer):
	photo_id = serializers.IntegerField()

	class Meta:
		model = TelegramPhoto
		fields = ('photo_id',)


class ProfileSerializer(serializers.ModelSerializer):
	telegram_id = serializers.IntegerField()
	photos = TgPhotoSerializer(many=True)

	class Meta:
		model = Profile
		fields = ('photos', 'telegram_id', 'first_name', 'last_name', 'username')

	def create(self, validated_data):
		photos_data = validated_data.pop('photos')
		profile, _ = Profile.objects.update_or_create(
			telegram_id=validated_data.pop('telegram_id'),
			defaults=validated_data
		)
		for photo_data in photos_data:
			TelegramPhoto.objects.get_or_create(owner=profile, **photo_data)
		return profile


class NoteSerializer(serializers.ModelSerializer):
	note_getter = ProfileSerializer()
	creator = ProfileSerializer()

	class Meta:
		model = Note
		fields = ('text', 'note_getter', 'creator')

	def create(self, validated_data):
		note_creator_data = validated_data.pop('creator')
		note_getter_data = validated_data.pop('note_getter')

		note_creator_sz = ProfileSerializer(data=note_creator_data)
		note_creator_sz.is_valid()
		note_creator = note_creator_sz.save()

		note_getter_sz = ProfileSerializer(data=note_getter_data)
		note_getter_sz.is_valid()
		note_getter = note_getter_sz.save()

		note = Note.objects.create(
			creator=note_creator,
			note_getter=note_getter,
			text=validated_data.get('text')
		)
		return note


class ProfileNotesSerializer(serializers.ModelSerializer):
	created_notes = NoteSerializer(many=True)
	# received_notes = NoteSerializer(many=True)

	class Meta:
		model = Profile
		fields = ('created_notes', )
