from django.contrib import admin
from .models import Member

# Register your models here.

# We can control the fields to display by specifying them in in a list_display property in the admin.py file.
# First create a MemberAdmin() class and specify the list_display tuple, like this:
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date")

admin.site.register(Member)
