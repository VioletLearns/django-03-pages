from django.urls import path
from .views import HomePageView, AboutPageView, VioletPageView, AnotherPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('violet/', VioletPageView.as_view(), name='violet'),
    path('another/', AnotherPageView.as_view(), name='another page')
]