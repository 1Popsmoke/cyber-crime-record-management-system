from django.urls import path
from . import views
urlpatterns=[
    path('', views.mainpage, name='mainpage'),
    path('register/', views.register, name='register'),
    path('login/', views.login_views, name='login'),
    path('team/', views.team, name='team'),
    path('logout/', views.logout),
    path('complaints/', views.list_complaints, name='list_complaints'), 
    path('complaint/<int:pk>/', views.view_complaint, name='view_complaint'),
    path('complaint/<int:pk>/edit/', views.update_complaint, name='update_complaint'),
    path('online_awerness/', views.online_awerness, name= 'online_awerness'),
    path('general_tips/', views.general_tips, name='general_tips'),


    
]