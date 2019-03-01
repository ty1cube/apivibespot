from rest_framework import status
from rest_framework import viewsets, status, exceptions, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken import views 
from rest_framework.authtoken.models import Token
from .renderers import UserJSONRenderer
from django.db.models import Q
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from .serializers import (
LoginSerializer, 
RegistrationSerializer,
RegisterArtistSerializer,
RegisterManagerSerializer,
RegisterRecordLabelSerializer,
UserSerializer,
PasswordResetSerializer,
PasswordResetVerifiedSerializer,
PasswordChangeSerializer

)

from rest_framework_jwt.settings import api_settings

from .models import User

jwt_payload_handler             = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler    = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


# class CustomAuthToken(views.ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#         context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         # if not user.is_verified:
#         #     return Response({
#         #             "errors": "Please check your inbox for verification link"
#         #         }, status=status.HTTP_400_BAD_REQUEST)

#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             "token": token.key,
#             "user" : {
#                 # "user_id": user.pk,
#                 "id":user.pk,
#                 # "space_admin": user_space.is_space_admin,
#                 # "space_type": user.space_type.id,
#                 "username": user.username,
#                 "email": user.email
#             }
#         })

class RegistrationAPIView(generics.CreateAPIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    # queryset = User.objects.all()
    permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        # user = request.data.get('user', {})
        # serializer = self.serializer_class(data=user)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RegisterArtistAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = RegisterArtistSerializer

    def post(self, request):
        # user = request.data.get('user', {})
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RegisterRecordLabelAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = RegisterManagerSerializer

    def post(self, request):
        # user = request.data.get('user', {})
        # serializer = self.serializer_class(data=request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RegisterManagerAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = RegisterManagerSerializer

    def post(self, request):
        # user = request.data.get('user', {})
        # serializer = self.serializer_class(data=request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
     # permission_classes = (IsAuthenticated,)
    queryset   = User.objects.all()
    serializer_class = UserSerializer


# class ProfileView(viewsets.ModelViewSet):
#     queryset   = Profile.objects.all()
#     serializer_class = ProfileSerializer

# class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     # permission_classes = (IsAuthenticated,)
#     permission_classes = (AllowAny,)
#     # renderer_classes = (UserJSONRenderer,)
#     serializer_class = UserSerializer

#     def retrieve(self, request, *args, **kwargs):
     
#         serializer = self.serializer_class(request.user)

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, *args, **kwargs):
#         serializer_data = request.data.get('user', {})

#         # Here is that serialize, validate, save pattern we talked about
#         # before.
#         serializer = self.serializer_class(
#             request.user, data=serializer_data, partial=True
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_200_OK)

class AuthAPIView(APIView):
    permission_classes      = (AllowAny,)

    def post(self, request, *args, **kwargs):
        #print(request.user)
        # if request.user.is_authenticated():
        #     return Response({'detail': 'You are already authenticated'}, status=400)
        data = request.data
        username = data.get('username') # username or email address
        password = data.get('password')
        qs = User.objects.filter(
                Q(username__iexact=username)|
                Q(email__iexact=username)
            ).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token, user, request=request)
                return Response(response)
        return Response({"detail": "Invalid credentials"}, status=401)



class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        # user = request.data.get('user', {})
        # serializer = self.serializer_class(data=user)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

# class UserView(viewsets.ModelViewSet):
#     queryset   = User.objects.all()
#     serializer_class = UserSerializer


# class ProfileView(viewsets.ModelViewSet):
#     queryset   = Profile.objects.all()
#     serializer_class = ProfileSerializer

class LogoutAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        tokens = Token.objects.filter(user=request.user)
        for token in tokens:
            token.delete()
        content = {'success': _('User logged out.')}
        return Response(content, status=status.HTTP_200_OK)

class PasswordResetAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PasswordResetSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.data['email']

            try:
                user = User.objects.get(email=email)
                if user.is_verified and user.is_active:
                    password_reset_code = \
                        PasswordResetCode.objects.create_reset_code(user)
                    password_reset_code.send_password_reset_email()
                    content = {'email': email}
                    return Response(content, status=status.HTTP_201_CREATED)

            except User.DoesNotExist:
                pass

            # Since this is AllowAny, don't give away error.
            content = {'detail': _('Password reset not allowed.')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


class PasswordResetVerifyAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        code = request.GET.get('code', '')

        try:
            password_reset_code = PasswordResetCode.objects.get(code=code)
            content = {'success': _('User verified.')}
            return Response(content, status=status.HTTP_200_OK)
        except PasswordResetCode.DoesNotExist:
            content = {'detail': _('Unable to verify user.')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetVerifiedAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PasswordResetVerifiedSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # code = serializer.data['code']
            # password = serializer.data['password']
            code = request.data.get("code")
            password = request.data.get("password")

            try:
                password_reset_code = PasswordResetCode.objects.get(code=code)
                password_reset_code.user.set_password(password)
                password_reset_code.user.save()
                content = {'success': _('Password reset.')}
                return Response(content, status=status.HTTP_200_OK)
            except PasswordResetCode.DoesNotExist:
                content = {'detail': _('Unable to verify user.')}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


class PasswordChangeAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PasswordChangeSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = request.user

            password = serializer.data['password']
            user.set_password(password)
            user.save()

            content = {'success': _('Password changed.')}
            return Response(content, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


# class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     permission_classes = (IsAuthenticated,)
#     # renderer_classes = (UserJSONRenderer,)
#     serializer_class = UserSerializer

#     def retrieve(self, request, *args, **kwargs):
#         serializer = self.serializer_class(request.user)

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, *args, **kwargs):
#         serializer_data = request.data.get('user', {})

#         # Here is that serialize, validate, save pattern we talked about
#         # before.
#         serializer = self.serializer_class(
#             request.user, data=serializer_data, partial=True
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_200_OK)


