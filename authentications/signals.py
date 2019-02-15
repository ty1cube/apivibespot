from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import (
    User,
    ArtistProfile, 
    UserProfile,
    RecordLabelProfile,
    ManagementProfile
)


@receiver(post_save, sender=User)
def build_profile_on_user_creation(sender, instance, created, **kwargs):
        if created:
                profile = ArtistProfile(user=instance)
                profile.save()

# @receiver(post_save, sender=User)
# def create_or_update_artist_profile(sender, instance, created, **kwargs):
#     if created:
#         ArtistProfile.objects.create(user=instance)
#     instance.artistprofile.save()

# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#     instance.userprofile.save()

# @receiver(post_save, sender=User)
# def create_or_update_record_profile(sender, instance, created, **kwargs):
#     if created:
#         RecordLabelProfile.objects.create(user=instance)
#     instance.recordlabelprofile.save()

# @receiver(post_save, sender=User)
# def create_or_update_management_profile(sender, instance, created, **kwargs):
#     if created:
#         ManagementProfile.objects.create(user=instance)
#     instance.managementprofile.save()

# # from django.db.models.signals import post_save
# # from django.dispatch import receiver
# # from authentications import models
# # # from authentications import models
# # # from .models import VibespotMember
# # from django.conf import settings 
# # from rest_framework.authtoken.models import Token

# # @receiver(post_save, sender=models.User)
# # def create_related_profile(sender, instance, created, *args, **kwargs):
# #     # Notice that we're checking for `created` here. We only want to do this
# #     # the first time the `User` instance is created. If the save that caused
# #     # this signal to be run was an update action, we know the user already
# #     # has a profile.
# #     if instance and created:
# #         instance.profile = models.Profile.objects.create(user=instance)


# # # def set_vibespot_member(user, member, member_type, is_member_admin, is_approved):
# # #     VibespotMember.objects.create(
# # #                 user=user, 
# # #                 member=member,
# # #                 member_type=member_type,
# # #                 is_member_admin=is_member_admin,
# # #                 is_approved=is_approved,
# # #             )

# # # @receiver(post_save, sender=models.SpaceMember)
# # # def create_user_default_space(sender, instance, created, *args, **kwargs):
# # #     if instance and created:
# # #         models.UserDefaultSpace.objects.create(
# # #                 user=instance.user, 
# # #                 space=instance.space
# # #             )


# # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# # def create_auth_token(sender, instance=None, created=False, **kwargs):
# #     if created:
# #         Token.objects.create(user=instance)









# # # from django.db.models.signals import post_save
# # # from django.dispatch import receiver
# # # from django.db import models
# # # from .models import User
# # # from profiles.models import Profile

# # # # from profiles.models import (
# # # #     Profile,
# # # #     ArtistProfile,
# # # #     UserProfile,
# # # #     RecordLabelProfile,
# # # # )

# # # from .models import User

# # # @receiver(post_save, sender=User)
# # # def create_related_profile(sender, instance, created, *args, **kwargs):
# # #     # Notice that we're checking for `created` here. We only want to do this
# # #     # the first time the `User` instance is created. If the save that caused
# # #     # this signal to be run was an update action, we know the user already
# # #     # has a profile.
# # #     if instance and created:
# # #         instance.profile = Profile.objects.create(user=instance)



# # # @receiver(post_save, sender=User)
# # # def create_artist_profile(sender, instance, created, *args, **kwargs):
# # #     # Notice that we're checking for `created` here. We only want to do this
# # #     # the first time the `User` instance is created. If the save that caused
# # #     # this signal to be run was an update action, we know the user already
# # #     # has a profile.
# # #     if instance and created:
# # #         instance.artsitprofile = ArtistProfile.objects.create(user=instance)

# # # @receiver(post_save, sender=User)
# # # def create_user_profile(sender, instance, created, *args, **kwargs):
# # #     # Notice that we're checking for `created` here. We only want to do this
# # #     # the first time the `User` instance is created. If the save that caused
# # #     # this signal to be run was an update action, we know the user already
# # #     # has a profile.
# # #     if instance and created:
# # #         instance.userprofile = UserProfile.objects.create(user=instance)

# # # @receiver(post_save, sender=User)
# # # def create_record_profile(sender, instance, created, *args, **kwargs):
# # #     # Notice that we're checking for `created` here. We only want to do this
# # #     # the first time the `User` instance is created. If the save that caused
# # #     # this signal to be run was an update action, we know the user already
# # #     # has a profile.
# # #     if instance and created:
# # #         instance.recordprofile = RecordLabelProfile.objects.create(user=instance)
