from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from agenda.models import AgendaPlugin


class CMSCalendarPlugin(CMSPluginBase):
    model = AgendaPlugin
    name = _('Calendar')
    render_template = "calendar/calendar.html"

    def render(self, context, instance, placeholder):
        context.update({
            'calendar' : instance.calendar,
            'object' : instance,
            'placeholder' : placeholder
        })
        return context

plugin_pool.register_plugin(CMSCalendarPlugin)
