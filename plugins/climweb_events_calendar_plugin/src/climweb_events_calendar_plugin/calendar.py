from calendar import HTMLCalendar


class EventsCalendar(HTMLCalendar):
    def __init__(self, events=None):

        self.events_by_day = {}

        if events:
            for event in events:
                day = event.date_from.day
                self.events_by_day[day] = event

        super(EventsCalendar, self).__init__()

    def formatday(self, day, weekday):
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # No day
        elif day in self.events_by_day:
            event_link = self.events_by_day[day].get_full_url()
            link = f'<a href="{event_link}" target="_blank">{day}</a>'
            return f'<td class="event-day"><strong>{link}</strong></td>'
        else:
            return f'<td class="{self.cssclasses[weekday]}">{day}</td>'
