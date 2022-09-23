from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Note, Profile, TelegramPhoto
from .serializers import NoteSerializer, ProfileSerializer, ProfileNotesSerializer


@api_view(['POST'])
def create_profile(request):
	try:
		data = request.data
		pf_sz = ProfileSerializer(data=data)
		print(pf_sz)
		tg_photo, _ = TelegramPhoto.objects.get_or_create(
			photo_id=data.get('photo')
		)
		profile, _ = Profile.objects.update_or_create(
			first_name=data.get('first_name'),
			last_name=data.get('last_name'),
			username=data.get('username'),
			phone=data.get('phone'),
			photo=tg_photo,
			defaults={
				'telegram_id': data.get('telegram_id'),
			}
		)
		return Response({'result': 'success'})
	except:
		return Response({'result': 'Something went wrong :('})


@api_view(['POST'])
def create_note(request):
	try:
		data = request.data
		note_getter_photo, _ = TelegramPhoto.objects.get_or_create(
			photo_id=data.get('note_getter').get('photo')
		)
		note_getter_profile, _ = Profile.objects.update_or_create(
			first_name=data.get('note_getter').get('first_name'),
			last_name=data.get('note_getter').get('last_name'),
			username=data.get('note_getter').get('username'),
			phone=data.get('note_getter').get('phone'),
			photo=note_getter_photo,
			defaults={
				'telegram_id': data.get('note_getter').get('telegram_id'),
			}
		)
		note_creator_photo, _ = TelegramPhoto.objects.get_or_create(
			photo_id=data.get('note_creator').get('photo')
		)
		note_creator_profile, _ = Profile.objects.update_or_create(
			first_name=data.get('note_creator').get('first_name'),
			last_name=data.get('note_creator').get('last_name'),
			username=data.get('note_creator').get('username'),
			phone=data.get('note_creator').get('phone'),
			photo=note_creator_photo,
			defaults={
				'telegram_id': data.get('note_creator').get('telegram_id'),
			}
		)
		note = Note(
			text=data.get('text'),
			note_getter=note_getter_profile,
			creator=note_creator_profile
		)
		note.save()
		return Response({'result': 'success'})
	except:
		return Response({'result': 'Something went wrong :('})


@api_view(['GET'])
def get_notes(request, creator_tg_id):
	note_creator = Profile.objects.get(telegram_id=creator_tg_id)
	serializer = ProfileNotesSerializer(note_creator)
	return Response(serializer.data)
