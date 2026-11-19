from. import views
from django.urls import path

urlpatterns = [
    path('home', views.index, name='home'),
    path('register/', views.register, name = 'register'),
    path('welcome/', views.welcome, name = 'welcome'),
    path('inspectionlist/', views.inspectionlist, name = 'inspectionlist'),
    path('records/', views.records, name = 'records'),
    path('analytics/', views.analytics, name = 'analytics'),
    path('regulations/', views.regulations, name = 'regulations'),
    path('F2/', views.f2, name = 'F2'),
]
