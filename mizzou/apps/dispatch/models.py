from django.db import models

# Models are Django's way of representing tables in your database.
# More info here: https://docs.djangoproject.com/en/dev/topics/db/models/

# And reference on different types of fields here:
# https://docs.djangoproject.com/en/dev/ref/models/fields/

class Type(models.Model):
    '''
    Unique types of dispatch calls from the data. For example,
    traffic stop, shots fired, etc.
    '''
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=20)

    def __unicode__(self):
        '''
        Unicode methods return a custom string representation of your
        model. Just know that you should always implement them.
        '''
        return self.name

    @models.permalink
    def get_absolute_url(self):
        '''
        This method returns the URL for the detail page of a particular
        type object.
        '''
        return ('dispatch_detail', (), {'slug': self.slug})


class Dispatch(models.Model):
    '''
    A model representing each dispatch call. Notice how it relates
    to the Type model via the ForeignKey "type" field.
    '''
    date_time = models.DateTimeField(blank=True, null=True)
    incident_num = models.CharField(max_length=10)
    location = models.CharField(max_length=255)
    apt_lot = models.CharField(max_length=10)
    type = models.ForeignKey(Type, blank=True, null=True)
    lat = models.CharField(max_length=10, blank=True)
    lng = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return '%s: %s' % (self.type, self.location)