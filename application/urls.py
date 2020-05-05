from django.urls import path

from application import views


urlpatterns = [
    path('healthz', views.HealthCheck.as_view(), name='health-check'),
    path('readiness', views.ReadinessCheck.as_view(), name='readiness-check'),
    path('api/collections/', views.Collections.as_view(), name='collections'),
    path('api/collections/<pk>/', views.CollectionsSingle.as_view(), name='collections-single'),
    path('api/landing-pages/', views.LandingPages.as_view(), name='landing-pages'),
    path('api/landing-pages/<pk>/', views.LandingPagesSingle.as_view(), name='landing-pages-single'),
]
