from django.contrib import admin
from django.contrib.sites.models import Site

Site.objects.create(pk=1, domain='192.168.219.101:8000', name='SportsCalendar')

