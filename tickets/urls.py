# tickets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/purchase/', views.purchase_ticket, name='purchase_ticket'),
    path('validate/<int:ticket_id>/', views.validate_ticket, name='validate_ticket'),
]
