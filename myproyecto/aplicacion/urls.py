from django.urls import path
from .views import contact_view
from .views import database_info

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('database-info/', database_info, name='database_info'),
]
