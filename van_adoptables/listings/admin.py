from django.contrib import admin
from listings.models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'price', 'organization')
    list_display_links = ('id', 'name')
    list_filter = ('organization',)
    list_editable = ('is_published',)
    search_fields = ('name', 'description', 'city', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
