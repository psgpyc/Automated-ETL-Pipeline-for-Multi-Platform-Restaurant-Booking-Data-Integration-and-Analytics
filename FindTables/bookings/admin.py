from django.contrib import admin
from  bookings.models import BookingPlatform, Restaurant, Reservations, Table, Customer,WebhookEvent



admin.site.register(BookingPlatform)
admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Reservations)
admin.site.register(Customer)
admin.site.register(WebhookEvent)