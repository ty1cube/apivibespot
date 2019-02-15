import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
# from authentications.core.models import TimestampedModel
import uuid

def upload_image(instance, filename):
    return "files/{unique_id}/images/profile/{filename}".format(unique_id=instance.unique_id, filename=filename)


# def upload_image(instance, filename):
#     return 'user_{0}/{1}'.format(instance.user.id, filename)


class UserManager(BaseUserManager):
    def create_user(self, username, email,user_type=None, phone = None,image=None, wallet=None, previous_wallet=None, email_verified=None, 
        profile_verified=None,state=None, city=None, fb_social_login_id=None, google_social_login_id=None, password=None):
        if username is None:
            raise ValueError('Users must have a valid username')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            user_type=user_type,
            phone=phone,
            image=image,
            wallet=wallet,
            previous_wallet=previous_wallet,
            email_verified=email_verified,
            profile_verified=profile_verified,
            state=state,
            city=city,
            fb_social_login_id=fb_social_login_id,
            google_social_login_id=google_social_login_id,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    auth_key                    = models.UUIDField(default=uuid.uuid4, editable = False, unique = True)
    unique_id                   = models.UUIDField(default=uuid.uuid4, editable = False, unique = True)
    username                    = models.CharField(db_index=True,max_length=50, unique=True)
    email                       = models.EmailField(max_length=100, unique=True)
    user_type                   = models.PositiveSmallIntegerField(blank=True, null=True)
    phone                       = models.CharField(max_length=15,blank=True, null=True)
    image                       = models.ImageField(upload_to = upload_image, blank=True, null=True)
    wallet                      = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    previous_wallet             = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    email_verified              = models.BooleanField(default=False,blank=True, null=True)
    profile_verified            = models.BooleanField(default=False,blank=True, null=True)
    state                       = models.CharField(max_length=255,blank=True, null=True)
    city                        = models.CharField(max_length=200,blank=True, null=True)
    fb_social_login_id          = models.CharField(True,max_length=200,blank=True, null=True)
    google_social_login_id      = models.CharField(max_length=200,blank=True, null=True)
    is_staff                       = models.BooleanField(default=False)
    is_admin                       = models.BooleanField(default=False)
    status                      = models.BooleanField(default=True)
    created_at                  = models.DateTimeField(auto_now_add=True)
    updated_at                  = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'user'


    def __str__(self):
        if self.username == None:
            return "User does not exist"
        return self.username

    # @property
    # def token(self):
    #     return self._generate_jwt_token()

    def get_full_name(self):
        # The user is identified by their username
        if self.username == None:
            return "User does not exist"
        return self.username

    def get_short_name(self):
        # The user is identified by their username
        if self.username == None:
            return "User does not exist"
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # def _generate_jwt_token(self):
    #     dt = datetime.now() + timedelta(days=60)

    #     token = jwt.encode({
    #         'id': self.pk,
    #         'username': self.username,
    #         'email': self.email,
    #         'isAuth': True,
    #     }, settings.SECRET_KEY, algorithm='HS256')

    #     return token.decode('utf-8')


class ArtistProfile(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    user  = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True )
    firstname = models.CharField(max_length=100, null=True)
    othernames = models.CharField(max_length=100, null=True)
    # record_label_id =  models.IntegerField()
    # management_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'artist_profile'

    def __str__(self):
        return self.user.username
    
    # @receiver(post_save, sender=User)
    # def create_profile_for_user(sender, instance=None, created=False, **kargs):
    #     if created:
    #         UserProfile.objects.get_or_create(user=instance)

# @receiver(post_save, sender=User)
# def create_artist_profile(sender, instance, created, **kwargs):
#     if created:
#         profile = ArtistProfile(user=instance)
#         profile.save()


# @receiver(post_save, sender=User)
# def create_artist_profile(sender, instance, created, **kwargs):
#     if created:
#         ArtistProfile.objects.create(user=instance)
#     instance.artistprofile.save()


class UserProfile(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    # user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user  = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100, null=True )
    firstname = models.CharField(max_length=100, null=True)
    othernames = models.CharField(max_length=100, null=True)
    date_of_birth =  models.DateField(auto_now=False, auto_now_add=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return self.user.username


class RecordLabelProfile(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    # user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user  = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    record_label_name = models.CharField(max_length=100, null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'record_label_profile'

    def __str__(self):
        return self.user.username


class ManagementProfile(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    # user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user  = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    record_management_name = models.CharField(max_length=100 )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'management_profile'

    def __str__(self):
        return self.user.username


def _generate_code():
    return uuid.uuid1(20)

# class AbstractBaseCode(models.Model):
#     # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     code = models.CharField(_('code'), max_length=60, default="")
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         abstract = True

#     # def send_email(self, prefix):
#     #     ctxt = {
#     #         'email': self.user.email,
#     #         # 'first_name': self.user.first_name,
#     #         # 'last_name': self.user.last_name,
#     #         'code': self.code
#     #     }
#     #     send_multi_format_email(prefix, ctxt, target_email=self.user.email)

#     def __str__(self):
#         return self.code


# class SignupCodeManager(models.Manager):
#     def create_signup_code(self, user, ipaddr):
#         code = _generate_code()
#         if not ipaddr:
#             ipaddr = "0.0.0.0"
#         signup_code = self.create(user=user, code=code, ipaddr=ipaddr)

#         return signup_code

#     def set_user_is_verified(self, code):
#         try:
#             signup_code = SignupCode.objects.get(code=code)
#             signup_code.user.is_verified = True
#             signup_code.user.save()
#             return True
#         except SignupCode.DoesNotExist:
#             pass
#         return False


# class SignupCode(AbstractBaseCode):
#     ipaddr = models.GenericIPAddressField(_('ip address'),default='0.0.0.0')
#     objects = SignupCodeManager()

#     class Meta:
#         db_table = 'signupcode'
    
    # def send_signup_email(self):
    #     prefix = 'signup_email'
    #     self.send_email(prefix)


class PasswordResetCodeManager(models.Manager):
    def create_reset_code(self, user):
        code = _generate_code()
        password_reset_code = self.create(user=user, code=code)

        return password_reset_code


def send_multi_format_email(template_prefix, template_ctxt, target_email):
    subject_file = 'vibespot/%s_subject.txt' % template_prefix
    txt_file = 'vibespot/%s.txt' % template_prefix
    html_file = 'vibespot/%s.html' % template_prefix

    subject = render_to_string(subject_file).strip()
    from_email = settings.DEFAULT_EMAIL_FROM
    to = target_email
    # bcc_email = settings.DEFAULT_EMAIL_BCC
    text_content = render_to_string(txt_file, template_ctxt)
    html_content = render_to_string(html_file, template_ctxt)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


class PasswordResetCode(models.Model):
    objects = PasswordResetCodeManager()

    class Meta:
        db_table = 'passwordresetcode'
    def send_password_reset_email(self):
        prefix = 'password_reset_email'
        self.send_email(prefix)
