from django.views import generic
from . import mixins 

# from django.shortcuts import render

# Create your views here.
class MonthCalendar(mixins.MonthCalendarMixin, generic.TemplateView):
	template_name = 'app/month.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		calendar_context = self.get_month_calendar()
		context.update(calendar_context)
		return context

class WeekCalendar(mixins.WeekCalendarMixin, generic.TemplateView):
	template_name = 'app/week.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		calendar_context = self.get_week_calendar()
		context.update(calendar_context)
		return context