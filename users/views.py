from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import UserValidateSerializer, UserAuthorizationSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView


@api_view(['POST'])
def registration(request):
    serializer = UserValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    User.objects.create_user(**serializer.validated_data)
    return Response(data={'message': 'User created'})


@api_view(['POST'])
def authorization(request):
    serializer = UserAuthorizationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)
        return Response(data={'key': token.key})
    return Response(data={'message': 'User not found'},
                    status=404)


class RegisterAPIView(APIView):
    serializer_class = UserValidateSerializer
    model_class = User

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.model_class.objects.create_user(**serializer.validated_data)
        return Response(data={'message': 'User created'})

class AuthorizationAPIView(APIView):
    serializer_class = UserAuthorizationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'key': token.key})
        return Response(data={'message': 'User not found'},
                        status=404)