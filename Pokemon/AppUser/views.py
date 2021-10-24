from django.shortcuts import render
from rest_framework.relations import ManyRelatedField
from AppUser.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from AppUser.serializer import UserSerializer



# Create your views here.
@api_view(['GET', 'POST'])
def registro(request):

    if request.method == 'GET':
        users = User.objects.all()
        users_serializers = UserSerializer(users,many=True)
        return Response(users_serializers.data)

    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)



    


        



