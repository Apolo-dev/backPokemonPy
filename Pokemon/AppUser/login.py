from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .serializer import UserTokenSerializer

class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Login Success!'
                    }, status = status.HTTP_201_CREATED)
            else:
                return Response({'error': 'No esta autirizado!'}, status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Nombre o password incorrecto'}, status.HTTP_400_BAD_REQUEST)
        return Response({'message':'Todo bien bitches'}, status = status.HTTP_200_OK)