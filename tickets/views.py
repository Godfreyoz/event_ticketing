from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Ticket
from .forms import EventForm, TicketForm
import qrcode
from io import BytesIO
from django.core.files import File
from django.http import JsonResponse

# Create your views here.

def event_list(request):
    events = Event.objects.all()
    return render(request, 'tickets/templates/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'tickets/templates/event_detail.html', {'event': event})

def purchase_ticket(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.event = event

            # Generate QR code
            qr = qrcode.make(f'Ticket for {event.name} by {request.user.username}')
            buffer = BytesIO()
            qr.save(buffer)
            ticket.qr_code.save(f'{ticket.id}_qr.png', File(buffer), save=False)

            ticket.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = TicketForm()
    return render(request, 'tickets/templates/purchase_ticket.html', {'form': form, 'event': event})


def validate_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if ticket:
        return JsonResponse({'status': 'valid'})
    else:
        return JsonResponse({'status': 'invalid'})