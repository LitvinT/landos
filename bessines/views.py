from django.shortcuts import render

from datetime import datetime
from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views import View

from .models import Product
from .forms import ContactForm


class IndexTemplateView(TemplateView):
	template_name = 'main/index.html'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['contact_form'] = ContactForm()
		return context

	def post(self, request: HttpRequest):
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
		return self.get(request)