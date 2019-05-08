from django.contrib import admin

# Register your models here.
from apps.tts.models import TTSProviderModel


class TTSProviderModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'api_url', 'app_id', 'app_key')


admin.site.register(TTSProviderModel, TTSProviderModelAdmin)
