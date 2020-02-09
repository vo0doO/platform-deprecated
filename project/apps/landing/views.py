from django.views.generic import View
from django.shortcuts import render
from project.apps.landing.models import (
   Contact,
   ContactForm,
   ContactItem
   )


class LandingView(View):
   def get(self, *args, **kwargs):
      return render(self.request, 'landing/buttons.html')


class ContactView(View):
   def get(self, *args, **kwargs):
      return render(self.request, 'contact.html')


class DashboardView(View):
   def get(self, *args, **kwargs):
      return render(self.request, 'dashboard/dashboard.html')


class SandboxView(View):
   def get(self, *args, **kwargs):
      return render(self.request, 'base/sandbox.html')
