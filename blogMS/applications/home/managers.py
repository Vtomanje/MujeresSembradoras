from django.db import models


class EntryManager(models.Manager):
    """ porcedimiento para entradas"""
    
        
    def entradas_en_home(self):
        #devuelve las ultimas 4 entradas en home
        return self.filter(
            public=True,
            in_home=True,
        ).order_by('-created')[:4]
        
