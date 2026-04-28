from django.urls import path
 
from . import views
 
urlpatterns = [
    path("", views.index, name="home_page"),
    path("third/", views.third, name="third_page"),
    path("ticket/", views.ticket, name="ticket_page")
]