from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Note
from .serializers import NoteSerializer


@api_view(['POST'])
def create_user():
	pass


@api_view(['POST'])
def create_note():
	pass


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
