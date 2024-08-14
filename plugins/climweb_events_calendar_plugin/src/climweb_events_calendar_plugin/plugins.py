from climweb.base.registries import Plugin


class PluginNamePlugin(Plugin):
    type = "climweb_events_calendar_plugin"

    def get_urls(self):
        return []
