from django.urls import path
from .views import Apiviews

urlpatterns=[
    path('',Apiviews.as_view(), name='recommand')
]