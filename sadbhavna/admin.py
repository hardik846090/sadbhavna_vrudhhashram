from django.contrib import admin
from .models import Benner, WhatWeDo, Volunteer, Cause, LatestNews, UpcomingEvents, Contact

# Register your models here.

admin.site.register(Benner)

admin.site.register(WhatWeDo)

admin.site.register(Volunteer)

admin.site.register(Cause)

admin.site.register(LatestNews)

admin.site.register(UpcomingEvents)

admin.site.register(Contact)
