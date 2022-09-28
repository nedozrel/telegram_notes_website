from django.db.models import Q, Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Note, Profile, TelegramPhoto
from .serializers import NoteSerializer, ProfileSerializer, ProfileNotesSerializer, BaseNoteSz


@api_view(['POST'])
def create_profile(request):
	data = request.data
	serializer = ProfileSerializer(data=data)
	serializer.is_valid(raise_exception=True)
	serializer.save()
	return Response(serializer.data)


@api_view(['GET'])
def get_profile(request, tg_user_id):
	profile = Profile.objects.get(telegram_id=tg_user_id)
	profile_sz = ProfileSerializer(profile)
	return Response(profile_sz.data)


@api_view(['POST'])
def create_note(request):
	data = request.data
	serializer = NoteSerializer(data=data)
	serializer.is_valid()
	serializer.save()
	return Response(serializer.data)


@api_view(['GET'])
def get_notes(request, creator_tg_id):
	sent_to = request.GET.get('sent_to')
	if sent_to:
		notes = Note.objects.filter(
			Q(creator__telegram_id=creator_tg_id) &
			Q(note_getter__telegram_id=sent_to)
		)
		note_getter_profile = Profile.objects.get(telegram_id=sent_to)

		note_getter_sz = ProfileSerializer(note_getter_profile)
		notes_sz = BaseNoteSz(notes, many=True)

		response_dict = {
			'note_getter': note_getter_sz.data,
			'notes': notes_sz.data
		}
		return Response(response_dict)
	else:
		note_creator = Profile.objects.get(telegram_id=creator_tg_id)
		serializer = ProfileNotesSerializer(note_creator)
		return Response(serializer.data)


@api_view(['GET'])
def get_user_friends(request, tg_user_id):
	friends = Profile.objects.filter(
		received_notes__creator__telegram_id=tg_user_id
	).annotate(
		notes_received=Count('telegram_id')
	).order_by(
		'username'
	).values(
		'telegram_id',
		'username',
		'notes_received'
	)
	return Response(friends)
