from django.urls import path
from .views import *
urlpatterns = [ 
    path('',JobListView.as_view(),name='home'),
    path('jobs/new',JobCreateView.as_view(),name='jobs-create'),
    path('jobs/<int:pk>/',JobDetailView.as_view(),name='jobs-detail'),
    path('jobs/<int:pk>/delete/',JobDeleteView.as_view(),name='jobs-delete'),
    path('jobs/<int:pk>/update/',JobUpdateView.as_view(),name='jobs-update'),
]
