from django.db import models


class ListUrls(models.Model):
    long_url = models.CharField(max_length=200)

    def __str__(self):
        return self.long_url