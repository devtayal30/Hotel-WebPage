from django.contrib import admin
from Services.models import RoomAvailability

class serviceAdmin(admin.ModelAdmin):
    list_display=('AC_Room','Non_AC_Room')

admin.site.register(RoomAvailability,serviceAdmin)

# Register your models here.
