from django.urls import path 
from flight import views

urlpatterns = [
    path('', views.flights, name='all_flights'),
    path('flights/buy_tickets/<int:flight_id>/', views.buy_ticket, name='buy_ticket'),
]
