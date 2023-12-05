from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('service-detail/<int:pk>/', views.ServiceDetailView.as_view(), name="service_detail"),
    path('about-us/', views.AboutUsView.as_view(), name="about_us"),
    path('our-service/', views.ServicesView.as_view(), name="our_service"),
    path('contact-us/', views.ContactUsView.as_view(), name="contact_us"),
    path('team-member/', views.TeamMemberView.as_view(), name="team_member"),
]
