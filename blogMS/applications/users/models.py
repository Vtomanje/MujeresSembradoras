from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

#
from .managers import UserManager

"""def user_directory_path_profile(instance, filename):
    profile_picture_name = 'user/{0}/profile.jpg'.format(instance.user.full_name)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)
    
    if os.path.exists(full_path):
        os.remove(full_path)
    return profile_picture_name"""
    

class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )

    email = models.EmailField(unique=True)
    full_name = models.CharField('Nombres', max_length=100)
    citezen = models.CharField('Nacionalidad', max_length=100)
    phone = models.CharField('Teléfono', max_length=15)
    ocupation = models.CharField('Ocupacion', max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    date_birth = models.DateField('Fecha de nacimiento',  blank=True, null=True)
    avatar = models.ImageField('Avatar', upload_to='user', blank=True)
   
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def get_short_name(self):
        return self.email
    
    def get_full_name(self):
        return self.full_name
    
"""class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(default='users/user_default_profile.png', upload_to=user_directory_path_profile)

    def __str__(self):
        return self.user.full_name

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
def save_user_profile(sender, instance, **kwargs):
    
    instance.profile.save()
        

# save created profile
post_save.connect(create_user_profile, sender=User)

# save created profile
post_save.connect(save_user_profile, sender=User)"""

