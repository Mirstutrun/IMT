from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('productions/', views.productions_view, name='productions'),
    path('excursions/', views.excursions_view, name='excursions'),
    path('exhibitions/', views.exhibitions_view, name='exhibitions'),
    path('online-events/', views.online_events_view, name='online_events'),
    path('broadcasts/', views.broadcasts_view, name='broadcasts'),
    path('bar-items/', views.bar_items_view, name='bar_items'),
    path('users/', views.users_view, name='users'),
    path('export-excel/', views.export_excel, name='export_excel'),
]