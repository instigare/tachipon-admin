from django.urls import path

from . import views

urlpatterns = [
    path('', views.ReportListView.as_view(), name = 'dashboard'),
    path('details/<int:pk>', views.ReportDetailView.as_view(), name = 'details'),
    path('report/', views.report, name = 'report'),
]