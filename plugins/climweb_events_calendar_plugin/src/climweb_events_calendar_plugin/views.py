from climweb.pages.events.models import EventPage
from django.shortcuts import render
from django.utils import timezone

from .calendar import EventsCalendar


def index(request):
    # get events this month
    events = EventPage.objects.live().filter(date_from__year=timezone.now().year, date_from__month=timezone.now().month)
    current_year = timezone.now().year
    current_month = timezone.now().month
    calendar_html = EventsCalendar(events).formatmonth(current_year, current_month)

    template_name = "climweb_events_calendar_plugin/index.html"

    context = {
        'current_year': current_year,
        'calendar_html': calendar_html,
        "events_count": events.count(),
    }

    return render(request, template_name, context)
