from django.db import models


class Url(models.Model):
    url = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)
    ip = models.GenericIPAddressField(verbose_name='Ip Address')
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.url)
