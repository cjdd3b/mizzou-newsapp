from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=20)

    def __unicode__(self):
        return self.name


class Dispatch(models.Model):
    date_time = models.DateTimeField(blank=True, null=True)
    incident_num = models.CharField(max_length=10)
    location = models.CharField(max_length=255)
    apt_lot = models.CharField(max_length=10)
    type = models.ForeignKey(Type, blank=True, null=True)
    lat = models.CharField(max_length=10, blank=True)
    lng = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return '%s: %s' % (self.type, self.location)
