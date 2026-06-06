from django.urls import path
 
from . import views
 
urlpatterns = [
    path("login/", views.login_page, name="login_page"),
    path("logout/", views.logout_page, name="logout_page"),
    path("", views.index, name="home_page"),
    path("third/", views.third, name="third_page"),
    path("ticket/", views.ticket, name="ticket_page")
]
