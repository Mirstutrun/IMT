from django.contrib import admin
from .models import UserProfile, Production, Excursion, BarItem, Exhibition, OnlineEvent, Broadcast

admin.site.register(UserProfile)
admin.site.register(Production)
admin.site.register(Excursion)
admin.site.register(BarItem)
admin.site.register(Exhibition)
admin.site.register(OnlineEvent)
admin.site.register(Broadcast)