from django.contrib import admin
from .models import Complaint

class ComplaintAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'user', 'created_at', 'updated_at')
    
    # Fields to search in the admin interface
    search_fields = ('title', 'description')
    
    # Fields to filter by in the admin interface
    list_filter = ('user', 'created_at', 'updated_at')

    # Make fields editable directly in the list view
    list_editable = ('title',)

    # Define which field will be clickable in the list view (it must be one of the fields in list_display)
    list_display_links = ('user',)  # Or you could use 'title' if you want title to be clickable

# Registering the Complaint model with the admin site
admin.site.register(Complaint, ComplaintAdmin)
