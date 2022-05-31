from django.urls import path
from . import views

# 127.0.0.1:8000 에서 /sign-up에 접근하면 views파일안에 있는 sign_up_view(함수)가 실행

# 127.0.0.1:8000 에서 /sign-in에 접근하면 views파일안에 있는 sign_in_view(함수)가 실행


urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('logout/', views.logout, name='logout'),
    path('user/', views.user_view,name='user-list'),
    path('user/follow/<int:id>',views.user_follow,name='user-follow'),
]