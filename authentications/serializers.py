from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from . models import(
    User,
    ArtistProfile,
    RecordLabelProfile,
    UserProfile,
    ManagementProfile
) 

# from .models import User, Profile




class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True,min_length=8)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model  = User 
        fields = ("id", "username", "email", "password", "token")
        # fields = "__all__"
        read_only_field = ("created_at", "updated_at")

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

    
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }
        

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=128, min_length=8, write_only=True)


#     class Meta:
#         model = User
#         fields = "__all__"
#         # fields = ('email', 'username', 'password', 'token',)
#         read_only_fields = ('created_at',)

#     def update(self, instance, validated_data):
#         """Performs an update on a User."""
#         password = validated_data.pop('password', None)

#         for (key, value) in validated_data.items():
#             setattr(instance, key, value)

#         if password is not None:
#             instance.set_password(password)

#         instance.save()

#         return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User 
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer();

    class Meta:
        model  = ArtistProfile
        fields = "__all__"
        # fields = ("id", "username", "email")
        read_only_fields = ("created_on", "updated_on")

class ArtistProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer();
    class Meta:
        model  = ArtistProfile
        fields = "__all__"
        # fields = ("id", "username", "email")
        read_only_fields = ("created_at", "updated_at")

    
        
class RegisterArtistSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True,min_length=8)
    token = serializers.CharField(max_length=255, read_only=True)
    # artist_profile = ArtistProfileSerializer(required=False)
    # artist_profile = ArtistProfileSerializer(required=False)
    # userprofile = UserProfileSerializer(required=False)

    class Meta:
        model  = User 
        fields = ("id", "username", "email", "password", "token")
        # fields = "__all__"
        read_only_field = ("created_at", "updated_at")

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**validated_data)


    # def create(self, validated_data):
    #     artist_profile_data = validated_data.pop('artist_profile')
    #     user = User.objects.create_user(**validated_data)
    #     ArtistProfile.objects.create_user(**artist_profile_data)
    #     return user

    # def create_profile(self, validated_data, instance=None):
    #     profile_data = validated_data.pop('artist_profile')
    #     user = User.objects.create(**validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     ArtistProfile.objects.update_or_create(user=user,**profile_data)
    #     return user
    # def create(self, validated_data, instance=None):
    #     artist_profile_data = validated_data.pop('artistprofile')
    #     user = User.objects.create_user(**validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     ArtistProfile.objects.update_or_create(user=user,**artist_profile_data)
    #     return user


class RegisterRecordLabelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True,min_length=8)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model  = User 
        fields = ("id", "username", "email", "password", "token")
        # fields = "__all__"
        read_only_field = ("created_at", "updated_at")

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**validated_data)



class RegisterManagerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True,min_length=8)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model  = User 
        fields = ("id", "username", "email", "password", "token")
        # fields = "__all__"
        read_only_field = ("created_at", "updated_at")

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**validated_data)

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model  = User 
#         fields = ("id", "username", "email")


# class ArtistProfileSerializer(serializers.ModelSerializer):
#     # user = UserSerializer();
#     class Meta:
#         model  = ArtistProfile
#         fields = "__all__"
#         # fields = ("id", "username", "email")
#         read_only_fields = ("created_at", "updated_at")


class ManagementProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer();

    class Meta:
        model  = ManagementProfile
        fields = "__all__"
        # fields = ("id", "username", "email")
        read_only_fields = ("created_at", "updated_at")

class RecordLabelProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer();

    class Meta:
        model  = RecordLabelProfile
        fields = "__all__"
        # fields = ("id", "username", "email")
        read_only_fields = ("created_at", "updated_at")


class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer();
    class Meta:
        model  = UserProfile
        fields = "__all__"
        # fields = ("id", "username", "email")
        read_only_fields = ("created_at", "updated_at")


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)


class PasswordResetVerifiedSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=128)


class PasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)






    # def update(self, instance, validated_data):
    #     """Performs an update on a User."""

    #     password = validated_data.pop('password', None)
    #     for (key, value) in validated_data.items():
    #         setattr(instance, key, value)

    #     if password is not None:     
    #         instance.set_password(password)

    #     instance.save()

    #     return instance