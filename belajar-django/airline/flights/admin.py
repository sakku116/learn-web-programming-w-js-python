from django.contrib import admin

from .models import Flight, Airport, Passenger
# Register your models here.


# konfigurasi tambahan untuk tampilan pada admin
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ["flights"]

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)

