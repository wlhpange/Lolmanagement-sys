"""AppLOL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from OBGG import views
from django.urls import path,include
from .views import ob_gg
from .views import register_view
urlpatterns = [

    path('',ob_gg),
    path('register/', register_view),
    path('login/', include('OBGG.urls_son')),




path('login/LPL/alter', views.alter_user),
path('login/LPL/player/alter', views.alter_user),
path('login/LPL/team/alter', views.alter_user),
path('login/LPL/spring1/alter', views.alter_user),
path('login/LPL/spring2/alter', views.alter_user),
path('login/LPL/summer1/alter', views.alter_user),
path('login/LPL/summer2/alter', views.alter_user),
path('login/LCK/alter', views.alter_user),
path('login/LCK/player/alter', views.alter_user),
path('login/LCK/team/alter', views.alter_user),
path('login/LCK/spring1/alter', views.alter_user),
path('login/LCK/spring2/alter', views.alter_user),
path('login/LCK/summer1/alter', views.alter_user),
path('login/LCK/summer2/alter', views.alter_user),
path('login/LCS/alter', views.alter_user),
path('login/LCS/player/alter', views.alter_user),
path('login/LCS/team/alter', views.alter_user),
path('login/LCS/spring1/alter', views.alter_user),
path('login/LCS/spring2/alter', views.alter_user),
path('login/LCS/summer1/alter', views.alter_user),
path('login/LCS/summer2/alter', views.alter_user),
path('login/LEC/alter', views.alter_user),
path('login/LEC/player/alter', views.alter_user),
path('login/LEC/team/alter', views.alter_user),
path('login/LEC/spring1/alter', views.alter_user),
path('login/LEC/spring2/alter', views.alter_user),
path('login/LEC/summer1/alter', views.alter_user),
path('login/LEC/summer2/alter', views.alter_user),
path('login/WCI/alter', views.alter_user),
path('login/WCI/GM/alter', views.alter_user),
path('login/WCI/AG/alter', views.alter_user),
path('login/WCI/EC/alter', views.alter_user),
path('login/GM/EC/alter', views.alter_user),
path('login/GM/GF/alter', views.alter_user),

    path('login/serach/',views.search),
    path('login/LPL/serach/', views.search),
    path('login/LPL/player/serach/', views.search),
    path('login/LPL/team/serach/', views.search),
    path('login/LPL/spring1/serach/', views.search),
    path('login/LPL/spring2/serach/', views.search),
    path('login/LPL/summer1/serach/', views.search),
    path('login/LPL/summer2/serach/', views.search),
    path('login/LCK/serach/', views.search),
    path('login/LCK/player/serach/', views.search),
    path('login/LCK/team/serach/', views.search),
    path('login/LCK/spring1/serach/', views.search),
    path('login/LCK/spring2/serach/', views.search),
    path('login/LCK/summer1/serach/', views.search),
    path('login/LCK/summer2/serach/', views.search),
    path('login/LCS/serach/', views.search),
    path('login/LCS/player/serach/', views.search),
    path('login/LCS/team/serach/', views.search),
    path('login/LCS/spring1/serach/', views.search),
    path('login/LCS/spring2/serach/', views.search),
    path('login/LCS/summer1/serach/', views.search),
    path('login/LCS/summer2/serach/', views.search),
    path('login/LEC/serach/', views.search),
    path('login/LEC/player/serach/', views.search),
    path('login/LEC/team/serach/', views.search),
    path('login/LEC/spring1/serach/', views.search),
    path('login/LEC/spring2/serach/', views.search),
    path('login/LEC/summer1/serach/', views.search),
    path('login/LEC/summer2/serach/', views.search),
    path('login/WCI/serach/', views.search),
    path('login/WCI/GM/serach/', views.search),
    path('login/WCI/AG/serach/', views.search),
    path('login/WCI/EC/serach/', views.search),
    path('login/GF/EC/serach/', views.search),
    path('login/GF/GM/serach/', views.search),
    path('login/GF/serach/', views.search),
]


