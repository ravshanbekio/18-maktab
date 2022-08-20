from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.forms import UserCreationForm, UserChangeForm 
from user.models import Account

class AccountAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('first_name','last_name','phone_number','pupil_class','is_admin')
    list_filter = ('pupil_class','date_birth','date_joined')
    search_fields = ('pupil_class','username','email')

    fieldsets = (
        (None, {'fields': ('username','password')}),
        ('Personal info', {'fields': ('first_name','last_name','phone_number',
                                    'email','pupil_class','date_birth')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
    )
    filter_horizontal = ()

admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)