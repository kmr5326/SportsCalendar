"""SportsCalender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from kbo_Schedule import views as kboschview
from kbo_Rank import views as kborankview
from kleague_Schedule import views as kleagueschview
from kleague_Rank import views as kleaguerankview
from board import views as boardview


urlpatterns = [
    path('admin/', admin.site.urls),
    path('kboschedule/', kboschview.schedule_list),
    path('kboschedule/<str:pk>/', kboschview.schedule_detail),
    path('kborank/', kborankview.rank_list),
    path('kleagueschedule/', kleagueschview.schedule_list),
    path('kleagueschedule/<str:pk>/', kleagueschview.schedule_detail),
    path('kleaguerank/', kleaguerankview.rank_list),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/signup/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    path('board/', boardview.board_list),
    path('board/<str:pk>/', boardview.board_detail)
]
