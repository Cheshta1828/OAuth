from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer,LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework import serializers
from django.contrib.auth import authenticate
from oauth2_provider.models import get_application_model
from oauth2_provider.views.mixins import OAuthLibMixin
from oauth2_provider.views import TokenView
from django.contrib.auth.hashers import make_password
Application = get_application_model()
from django.contrib.auth.hashers import check_password

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes

from social_django.utils import psa

from requests.exceptions import HTTPError



class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class LoginView(APIView):
    def post(self, request):
        print("in post")
        username = request.data.get('username')
        password = request.data.get('password')
        client_id = request.data.get('client_id')
        client_secret = request.data.get('client_secret')
        user = authenticate(username=username, password=password)
        print(user)
        if user and user.is_active:
            try:
                application = Application.objects.get(client_id=client_id)
                is_valid_client_secret = check_password(client_secret, application.client_secret)
            
                if is_valid_client_secret:
                    token_view = TokenView()
                    response = token_view.create_token_response(request)
                    print(response)
                    #print(response('access_token'))
                    return Response({'response':response})

                    # return Response(response.data, status=response.status_code)
                    
                else:
                    return Response({'error': 'Invalid client credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            except Application.DoesNotExist:
                return Response({'error': 'Invalid client credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


    




@api_view(['POST'])
@permission_classes([AllowAny])
@psa()
def register_by_access_token(request, backend):
    print("register_by_access_token function")
    token = request.data.get('access_token')
    print(token)
    user = request.backend.do_auth(token)
    print(user)
    print(request)
    if user:
        print("user exists")
        token, _ = Token.objects.get_or_create(user=user)
        print(token.key)
        return Response(
            {
                'token': token.key
            },
            status=status.HTTP_200_OK,
            )
    else:
        return Response(
            {
                'errors': {
                    'token': 'Invalid token'
                    }
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(['GET', 'POST'])
def authentication_test(request):
    print(request.user)
    return Response(
        {
            'message': "User successfully authenticated"
        },
        status=status.HTTP_200_OK,
    )