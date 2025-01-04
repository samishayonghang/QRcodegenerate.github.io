from django.contrib import admin
from django.utils.html import mark_safe
from .models import QRcode

@admin.register(QRcode)
class QRcodeAdmin(admin.ModelAdmin):
    list_display = ('text', 'fileurl_display')

    def fileurl_display(self, obj):
        if obj.fileurl:
            # Generate an HTML <img> tag to display the image
            return mark_safe(f'<img src="{obj.fileurl.url}" width="100" height="100" />')
        return "No image"
    fileurl_display.short_description = 'QR Code Image'
