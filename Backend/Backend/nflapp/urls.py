from django.urls import path

from .views import MainView, SearchResultsView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('results/', SearchResultsView.as_view(), name='results'),
]