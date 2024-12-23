from django.contrib import admin
from user.models import User
from products.admin import BasketAdmin
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    fields = ['username']
    inlines = (BasketAdmin,)
