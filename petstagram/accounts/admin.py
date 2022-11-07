from django.contrib import admin
from petstagram.accounts.models import PetstagramUser


@admin.register(PetstagramUser)
class PetstagramUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'gender']
