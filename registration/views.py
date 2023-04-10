from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Registration
from .forms import RegistrationForm


def home(request):
    events = Event.objects.all()
    return render(request, 'registration/home.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        registration = form.save(commit=False)
        registration.event = event
        registration.save()
        return redirect('event_detail', event_id=event.id)
    return render(request, 'registration/event_detail.html', {'event': event, 'form': form})
