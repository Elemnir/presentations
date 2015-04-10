from django.contrib import admin

from ticketsub.models import Ticket

class TicketAdmin(admin.ModelAdmin):
    class Meta:
        model = Ticket
    list_display = ["subject", "sender", "subdate"]
admin.site.register(Ticket, TicketAdmin)
