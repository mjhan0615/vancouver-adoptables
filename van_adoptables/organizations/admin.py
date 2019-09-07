from django.contrib import admin
from organizations.models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Organization, OrganizationAdmin)
