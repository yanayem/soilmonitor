from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.loginsignuppage, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('terms_privacy/',views.terms_privacy_views,name='terms_privacy'),
    path('profile/', views.profilepage, name='profilepage'),
    path('remove-profile-pic/', views.remove_profile_pic, name='remove_profile_pic'),
]
