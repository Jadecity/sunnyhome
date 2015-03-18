from django.db import models

class Me(models.Model):
    name = models.CharField(max_length=200)
    photo = models.FileField(max_length=400)
    intro = models.CharField(max_length=2000)
    resInterest = models.CharField(max_length=2000)

"""    def __unicode__(self):
        unicode(self.name)
        unicode(self.photo)
        unicode(self.intro)
        unicode(self.resInterest)
"""
# Create your models here.
