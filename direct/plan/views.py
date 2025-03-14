from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from .models import Event
from .forms import EventForm
import calendar
import json

def calendar_view(request, year=None, month=None):
    if year is None or month is None:
        year = now().year
        month = now().month
    day1=now().day
    cal = calendar.Calendar()
    month_days = cal.itermonthdays(year, month)
    events = Event.objects.filter(date__year=year, date__month=month)

    event_dict = {event.date.day: [event.title,event.description,event.id,event.time] for event in events}#date도 추가시켜야하는데 그러면 json으로 변환할때 직렬화가 안됨
    event=json.dumps(event_dict)
    return render(request, "plan/calendar.html", {
        "year": year,
        "month": month,
        "day1": day1,
        "month_days": month_days,
        "event_dict": event,
        "calendar": calendar.month_name[month],
    })
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "plan/event_detail.html", {"event": event})

def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("calendar_view")
    else:
        form = EventForm()
    return render(request, "plan/event_form.html", {"form": form})