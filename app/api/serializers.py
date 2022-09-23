from rest_framework.serializers import ModelSerializer
from app.models import Note, Profile


class NoteSerializer(ModelSerializer):
	class Meta:
		model = Note
		fields = '__all__'


class ProfileSerializer(ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__'
