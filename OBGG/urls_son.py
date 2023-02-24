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

from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.login_view),
    path('logout/',views.log_out),
    # LPL
    path('LPL/', views.LPL_list),
    path('LPL/player/', views.LPL_player_list),
    path('LPL/team/', views.LPL_team_list),
    path('LPL/spring1/', views.LPL_spring1_list),
    path('LPL/spring2/', views.LPL_spring2_list),
    path('LPL/summer1/', views.LPL_summer1_list),
    path('LPL/summer2/', views.LPL_summer1_list),
    # LCK
    path('LCK/', views.LCK_list),
    path('LCK/player/', views.LCK_player_list),
    path('LCK/team/', views.LCK_team_list),
    path('LCK/spring1/', views.LCK_spring1_list),
    path('LCK/spring2/', views.LCK_spring2_list),
    path('LCK/summer1/', views.LCK_summer1_list),
    path('LCK/summer2/', views.LCK_summer2_list),
    # LCS
    path('LCS/', views.LCS_list),
    path('LCS/player/', views.LCS_player_list),
    path('LCS/team/', views.LCS_team_list),
    path('LCS/spring1/', views.LCS_spring1_list),
    path('LCS/spring2/', views.LCS_spring2_list),
    path('LCS/summer1/', views.LCS_summer1_list),
    path('LCS/summer2/', views.LCS_summer2_list),
    # LEC
    path('LEC/', views.LEC_list),
    path('LEC/player/', views.LEC_player_list),
    path('LEC/team/', views.LEC_team_list),
    path('LEC/spring1/', views.LEC_spring1_list),
    path('LEC/spring2/', views.LEC_spring2_list),
    path('LEC/summer1/', views.LEC_summer1_list),
    path('LEC/summer2/', views.LEC_summer2_list),
    # MSI
    path('WCI/', views.MSI_list),
    path('WCI/GM/', views.MSI_xiaozu_list),
    path('WCI/AG/', views.MSI_duikang_list),
    path('WCI/EC/', views.MSI_taotai_list),
    # WF
    path('GF/', views.GF_list),
    path('GF/GM/', views.WF_xiaozu_list),
    path('GF/EC/', views.WF_taotai_list),
    # 修改
    path('alter', views.alter_user),
]
