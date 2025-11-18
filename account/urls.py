from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.loginsignuppage, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('terms_privacy/',views.terms_privacy_views,name='terms_privacy'),
]
