from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = (
        'id', 
        'receipient', 
        'actor', 
        'verb', 
        'content_type', 
        'object_id', 
        'content_object', 
        'read', 
        'created_at'
    )
    
    # Filters on the right sidebar
    list_filter = ('read', 'created_at', 'content_type')
    
    # Search box for finding specific notifications
    search_fields = ('receipient__username', 'actor__username', 'verb', 'object_id')
    
    # Makes the list view faster by selecting related objects in one query
    list_select_related = ('receipient', 'actor', 'content_type')
    
    # Optional: Date hierarchy at the top for easy navigation
    date_hierarchy = 'created_at'

    # Make fields read-only if you don't want to accidentally change history
    # readonly_fields = ('created_at',)