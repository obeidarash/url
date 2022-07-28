from django.db import models


class Url(models.Model):
    url = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.url)
