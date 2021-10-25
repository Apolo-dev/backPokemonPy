from AppUser.models import User
from rest_framework.response import Response
from AppUser.serializer import UserSerializer, UserListSerializer
from rest_framework.views import APIView


class Registrar(APIView):
    
    def get(self, request):
        users = User.objects.all()
        users_serializers = UserListSerializer(users, many=True)
        return Response(users_serializers.data)

    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)






        



