from django.urls import path
from .views import contactme, thankyou

urlpatterns = [
    path('contact', contactme, name='contactme'),
    path('thankyou', thankyou, name='thankyou')
]
