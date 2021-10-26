from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from django.contrib.sessions.models import Session

from AppUser.serializer import UserTokenSerializer
from datetime import datetime

class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request': request})
        if login_serializer.is_valid():
            print(login_serializer.validated_data['user'])
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
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Login Success 2!'
                    }, status = status.HTTP_201_CREATED)
            else:
                return Response({'error': 'No esta autorizado!'}, status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Nombre o password incorrecto'}, status.HTTP_400_BAD_REQUEST)
        return Response({'message':'Todo bien bitches'}, status = status.HTTP_200_OK)

class Logout(APIView):
    def post(self, request, *args, **kwargs):
        try:
            token = request.POST.post('token')
            token = Token.objects.filter(key = token).first()
        
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_data__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                session_message = 'Sesion de usuario eliminada'

                token.delete()
                token_message = 'token eliminado'
                return Response({'token_message': token_message, 'session message': session_message}, status = status.HTTP_200_OK)
            return Response({'error': 'No se ha encontrado al usuario'}, status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'No se ha encontrado el token en la peticion'}, status = status.HTTP_409_CONFLICT)

        