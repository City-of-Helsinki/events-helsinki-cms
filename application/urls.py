from django.urls import path

from application import views


urlpatterns = [
    path('healthz/', views.HealthCheck.as_view(), name='health-check'),
    path('readiness/', views.ReadinessCheck.as_view(), name='readiness-check'),
]
