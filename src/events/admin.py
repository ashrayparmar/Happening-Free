from django.contrib import admin
from events.models import User, HappeningEvents
# Register your models here.

admin.site.register(HappeningEvents)
admin.site.register(User)
