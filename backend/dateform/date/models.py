from django.db import models


class Year(models.Model):
    year = models.IntegerField(blank=False, null=False)
    checkbox = models.BooleanField(blank=False)

    def __str__(self):
        return f'\'{self.id}\' - \'{self.year}\' '
