from django.urls import path, reverse
from wagtail import hooks
from wagtail.admin.menu import MenuItem

from .views import index


@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('calendar/', index, name='calendar'),
    ]


@hooks.register('register_admin_menu_item')
def register_calendar_menu_item():
    url = reverse('calendar')
    return MenuItem('Calendar of Events', url, icon_name='date', order=300)
