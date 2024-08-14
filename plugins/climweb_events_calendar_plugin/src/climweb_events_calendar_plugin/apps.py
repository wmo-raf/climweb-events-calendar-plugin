from django.apps import AppConfig

from climweb.base.registries import plugin_registry


class PluginNameConfig(AppConfig):
    name = "climweb_events_calendar_plugin"

    def ready(self):
        from .plugins import PluginNamePlugin

        plugin_registry.register(PluginNamePlugin())
