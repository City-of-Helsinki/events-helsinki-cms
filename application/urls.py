from django.urls import path

from application import views


urlpatterns = [
    path('healthz', views.HealthCheck.as_view(), name='health-check'),
    path('readiness', views.ReadinessCheck.as_view(), name='readiness-check'),
    path('api/collections/', views.Collections.as_view(), name='collections'),
    path('api/collections/<pk>/', views.CollectionsSingle.as_view(), name='collections-single'),
    path('api/landing-page/', views.LandingPage.as_view(), name='landing-page'),
]
