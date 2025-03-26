from django.contrib import admin
from .models import User
from .models import Contact

admin.site.site_title = "LifeAuto Admin"
admin.site.site_header = "LifeAuto Admin"
admin.site.index_title = "Welcome to the LifeAuto Admin Panel"



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "nationality", "date_of_birth","created_at")
    search_fields = ("first_name", "last_name", "email", "nationality")
    list_filter = ("nationality", "is_student", "has_company", "is_over_26")

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "tel", "message", "checkmark")
    search_fields = ("name", "email", "tel")
