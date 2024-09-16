from django.contrib import admin

from .models import Item, Position, ThreatInfo, PeerReview

admin.site.register(Item)
admin.site.register(Position)
admin.site.register(ThreatInfo)
admin.site.register(PeerReview)
