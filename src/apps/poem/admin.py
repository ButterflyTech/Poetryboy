from django.contrib import admin

# Register your models here.

from django.contrib import admin

from apps.poem.models import AuthorModel, PoemModel


class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'dynasty')


class PoemModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'dynasty', 'paragraphs')


admin.site.register(AuthorModel, AuthorModelAdmin)
admin.site.register(PoemModel, PoemModelAdmin)
