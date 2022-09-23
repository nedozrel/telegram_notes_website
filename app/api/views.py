from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Note, Profile, TelegramPhoto
from .serializers import NoteSerializer, ProfileSerializer


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
		note_sender_photo, _ = TelegramPhoto.objects.get_or_create(
			photo_id=data.get('note_sender').get('photo')
		)
		note_sender_profile, _ = Profile.objects.update_or_create(
			first_name=data.get('note_sender').get('first_name'),
			last_name=data.get('note_sender').get('last_name'),
			username=data.get('note_sender').get('username'),
			phone=data.get('note_sender').get('phone'),
			photo=note_getter_photo,
			defaults={
				'telegram_id': data.get('note_sender').get('telegram_id'),
			}
		)
		Note(
			text=data.get('text'),
			note_getter=note_getter_profile,
			creator=note_sender_profile
		)
		return Response({'result': 'success'})
	except:
		return Response({'result': 'Something went wrong :('})


@api_view(['GET'])
def get_notes(request):
	notes = Note.objects.all()
	serializer = NoteSerializer(notes, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def get_note(request, pk):
	note = Note.objects.get(id=pk)
	serializer = NoteSerializer(note)
	return Response(serializer.data)
