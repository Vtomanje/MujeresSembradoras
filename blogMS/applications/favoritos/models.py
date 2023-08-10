from django.db import models
from django.conf import settings
# apps de terceros
from model_utils.models import TimeStampedModel
from applications.entrada.models import Entry
from .managers import FavoritesManager


"""class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_favorites', on_delete=models.CASCADE)
    #picture = models.ImageField(default='users/user_default_profile.png', upload_to=user_directory_path_profile)

    def __str__(self):
        return f'perfil de{self.user.full_name}'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
def save_user_profile(sender, instance, **kwargs):
    
    instance.profile.save()
        

# save created profile
post_save.connect(create_user_profile, sender=User)

# save created profile
post_save.connect(save_user_profile, sender=User)"""



class Favorites(TimeStampedModel):
    """ Modelos ara Favoritos """
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_favorites', on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, related_name='entry_favorites', on_delete=models.CASCADE)
    
    objects = FavoritesManager()
    
    class Meta:
        unique_together = ('user', 'entry')
        verbose_name = 'Entrada Favoritas'
        verbose_name_plural = 'Entradas Favoritas'
        
        def __str__(self):
            return self.entry.title
    
