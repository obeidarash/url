from django.db import models


class Url(models.Model):
    url = models.CharField(max_length=10000, editable=False, blank=False)
    uuid = models.CharField(max_length=10, unique=True, editable=False, blank=False)
    ip = models.GenericIPAddressField(verbose_name='Ip Address', editable=False, blank=False)
    create = models.DateTimeField(auto_now_add=True, editable=False, blank=False)

    def __str__(self):
        return str(self.url)
