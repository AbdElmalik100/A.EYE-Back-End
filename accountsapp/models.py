from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.dispatch import Signal, receiver
from django.db.models.signals import post_save
# Create your models here.

USER_TYPE = [
    ('patient', 'Patient'),
    ('doctor', 'Doctor'),
]


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email Is Required")
        user = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    type = models.CharField(max_length = 15, choices = USER_TYPE, default = 'patient')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    # avatar = models.ImageField(upload_to='users_avatar', blank=True, null=True, default=None)
    avatar = models.CharField(max_length = 255, blank=True, null=True, default=None)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['type', 'first_name', 'last_name', 'username', 'is_superuser']



class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, related_name='patient_profile')

    def __str__(self):
        return self.user.username
    

class DoctorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, related_name='doctor_profile')
    # specialization = models.CharField(max_length = 255, blank=True, null=True)
    # clinic_address = models.CharField(max_length = 255, blank=True, null=True)
    # license_number = models.CharField(max_length = 255, blank=True, null=True)


    def __str__(self):
        return self.user.username



@receiver(post_save, sender = CustomUser)
def createProfile(sender, instance = None, created = False, *args, **kwargs):
    if created and instance.type == 'patient':
        PatientProfile.objects.create(
            user = instance
        )
    elif created and instance.type == 'doctor':
        DoctorProfile.objects.create(
            user = instance
        )

