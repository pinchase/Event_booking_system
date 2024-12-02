# Step 9: Configure URLs in booking/urls.py
from django.urls import path

from . import views
from .views import event_list, book_event

urlpatterns = [
    path('',views.index,name='index'),
    path('event_list/', event_list, name='event_list'),
    path('book/<int:event_id>/', views.book_event, name='book_event'),

      path('pay/', views.pay, name='pay'),

    path('stk/', views.stk, name="stk"),
    path('about/', views.about, name='about'),
    path('contact_us/', views.contact, name='contact_us'),


  ]
