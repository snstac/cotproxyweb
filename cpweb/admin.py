from audioop import reverse
from csv import list_dialects
from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

# Register your models here.

from .models import CPTransform, COTObject, Icon, IconSet


admin.site.site_header = 'COT Proxy Web'
admin.site.index_title = 'Sensors & Signals'


@admin.register(COTObject)
class COTObjectAdmin(admin.ModelAdmin):
    search_fields = ['uid', 'n_number']
    # list_display = ['uid', 'n_number']
    list_filter = ()
    list_per_page = 20

@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
    search_fields = ['name', 'type2525b']


@admin.register(IconSet)
class IconSetAdmin(admin.ModelAdmin):
    search_fields = ['uuid', 'name']


@admin.register(CPTransform)
class CPTransformAdmin(admin.ModelAdmin):
    search_fields = ['callsign', 'cot_uid__uid']
    autocomplete_fields = ['cot_uid']
    list_display = ['show_callsign', 'view_cot_uid']
    # list_filter = ('cot_uid__uid',)
    list_filter = ()
    list_per_page = 20

    @admin.display(empty_value="-None-", description='Callsign')
    def show_callsign(self, obj):
         return obj.callsign or "-None-"
    
    def view_cot_uid(self, obj):
        url = (
            reverse('admin:cpweb_cotobject_changelist')
            + '?'
            + urlencode({"uid": f"{obj.cot_uid}"})
        )
        return format_html('<a href="{}">{}</a>', url, obj.cot_uid)
