from django.db import models
from django.utils.translation import gettext as _

class PhoneStatustype(models.IntegerChoices):
    available = 1,_('available')
    unavailable = 2,_('unavailable')

class PhonesModel(models.Model):
    brand_name = models.CharField(_('brand name'),max_length=255)
    model_name = models.CharField(_('model name'),max_length=255,unique=True)
    brand_nationality = models.CharField(_('brand nationality'),max_length=255)
    color = models.CharField(_('color'),max_length=255)
    screen_size = models.FloatField(verbose_name=_('screen size'))
    status = models.IntegerField(_('status'),choices=PhoneStatustype.choices,default=PhoneStatustype.unavailable.value)
    manufacturing_country = models.CharField(_('manufacturing country'),max_length=255)
    
    price = models.PositiveIntegerField(verbose_name=_('price'))


    datetime_created = models.DateTimeField(_('datetime created'),auto_now_add=True)
    datetime_updated = models.DateTimeField(_('datetime updated'),auto_now = True)

    class Meta:
        ordering = ["-datetime_created"]

    def __str__(self):
        return f'{self.brand_name} {self.model_name}'
    
    def get_status(self):
        return {
            "id":self.status,
            "title":PhoneStatustype(self.status).name,
            "label":PhoneStatustype(self.status).label,
        }