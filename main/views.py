from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Service


class HomeView(View):
    template_name = "main/home.html"

    def get(self, request, *args, **kwargs):

        service_list = Service.objects.filter(active=True).order_by('id')
        
        context = {}
        context["title"] = "Home"
        context['first_four_service_list'] = service_list[:4]
        context['last_four_service_list'] = service_list[4:]
        return render(request, self.template_name, context)


class ServiceDetailView(DetailView):
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        service_list = Service.objects.filter(active=True).order_by('id')

        context['title'] = 'Service'
        context['service_list'] = service_list
        return context

    def get_object(self):
        return get_object_or_404(self.model, pk=self.kwargs['pk'], active=True)


class AboutUsView(View):
    template_name = "main/about_us.html"

    def get(self, request, *args, **kwargs):
        
        context = {}
        context["title"] = "About Us"
        return render(request, self.template_name, context)
    

class ServicesView(View):
    template_name = "main/services.html"

    def get(self, request, *args, **kwargs):

        service_list = Service.objects.filter(active=True).order_by('id')
        
        context = {}
        context["title"] = "Our Services"
        context['service_list'] = service_list
        return render(request, self.template_name, context)
    

class ContactUsView(View):
    template_name = "main/contact_us.html"

    def get(self, request, *args, **kwargs):
        
        context = {}
        context["title"] = "Contact Us"
        return render(request, self.template_name, context)
    

class TeamMemberView(View):
    template_name = "main/team_member.html"

    def get(self, request, *args, **kwargs):
        
        context = {}
        context["title"] = "Our Team Member"
        return render(request, self.template_name, context)

