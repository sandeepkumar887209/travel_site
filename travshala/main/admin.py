from django.contrib import admin
from .models import TravelQuery,Review

@admin.register(TravelQuery)
class TravelQueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'whatsapp_number', 'destination', 'travel_date', 'created_at')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rating', 'created_at')
    search_fields = ('name', 'email', 'comment')
    list_filter = ('rating', 'created_at')