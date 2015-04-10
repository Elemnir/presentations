from django.shortcuts import render, get_object_or_404

from ticketsub.models import Ticket, TicketForm

def submit_ticket(request, *args):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')

    else:
        if args:
            ticket = get_object_or_404(Ticket, 
                pk=args[0]
            )
            form = TicketForm(instance=ticket)
        else:
            form = TicketForm()

    return render(request, 'form.html', {
        'form' : form,
    })

def ticket_list(request):
    t = Ticket.objects.order_by('id')
    return render(request, 'list.html', {
        'ticketlist': t,
    })
