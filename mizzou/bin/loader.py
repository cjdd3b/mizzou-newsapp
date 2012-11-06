import csv, sys, os
from datetime import datetime
from django.template.defaultfilters import slugify

sys.path.append(os.path.expanduser('~/apps/mizzou'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'mizzou.settings'
from mizzou.apps.dispatch.models import *

########## HELPER FUNCTIONS ##########

def clean_date(dt):
    return datetime.strptime(dt, '%m/%d/%Y %I:%M:%S %p')

########## MAIN ##########

with open('out.csv', 'rb') as csvfile:
    file = csv.reader(csvfile, delimiter=',')
    for row in file:
        d, created = Dispatch.objects.get_or_create(incident_num=row[1])

        d.date_time = clean_date(row[0])
        d.location = row[2]
        d.apt_lot = row[3]
        
        t, created = Type.objects.get_or_create(name=row[4], slug=slugify(row[4]))
        d.type = t
        
        d.lat = row[5]
        d.lng = row[6]

        d.save()