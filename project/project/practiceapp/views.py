from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.response import Response


@api_view(['POST'])
def UserSignUp(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = Users.objects.create(
            name=name, email=email, password=password)

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def UserSignIn(request):

    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = Users.objects.filter(email=email)

        if user:

            if user[0].password == password:

                return Response({'Successful': True}, status=status.HTTP_200_OK)
            else:
                raise Exception('Invalid Password')

        else:
            raise Exception('Invalid Email')

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def CreateNote(request):

    email = request.data.get('email')
    note = request.data.get('note')

    try:
        user = Users.objects.filter(email=email)

        if user:

            user = Notes.objects.create(
                user=user, note=note)

            serializer = NoteSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            raise Exception('User doesnot exist')

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def FetchNote(request):

    email = request.data.get('email')

    try:
        user = Users.objects.filter(email=email)

        if user:

            note = Notes.objects.filter(user=user[0])

            serializer = NoteSerializer(note)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            raise Exception('User doesnot exist')

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def UpdateNote(request):

    id = request.data.get('id')
    text = request.data.get('text')

    try:
        note = Notes.objects.get(pk=id)
        note.note_text = text
        note.save()

        serializer = NoteSerializer(note)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def DeleteNote(request):

    note = request.data.get('id')

    try:
        Notes.objects.get(pk=note).delete()

        return Response({'Deletion': 'Successfull'}, status=status.HTTP_202_ACCEPTED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
