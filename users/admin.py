# django
from django.contrib import admin
# models
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('id','user','phone_number','website','picture')
    list_display_links=('user','phone_number') # NOTE: ce que los datos indicados sean clickeables y redirijan al detalle del usuario
    list_editable=('website','picture') #datos editables, no deben  ser links
    search_fields=('user__email','user__first_name','user__last_name','phone_number')
    # NOTE: se pueden agregar campos por los cuales se desee buscar

    # filtros
    list_filter=(
    'created',
    'modified',
    'user__is_active',
    'user__is_staff'
    )
    # el orden de los filtros aparecera segun el orden de la lista
    pass
