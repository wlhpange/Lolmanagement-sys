from datetime import datetime
from .models import *
from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth.models import User
user_login = {}


def ob_gg(request):
    context = {}
    return render(request, 'OP.GG.html', context)


# 登录
def login_view(request):
    if request.method == 'GET':
        return render(request, 'OP.GG.html')
    if request.method == 'POST':
        name = request.POST.get("name", '')
        pwd = request.POST.get("password", '')
        if name and pwd:
            c = UserT.objects.filter(c_username=name, c_user_password=pwd).count()
            ppt = TeamT.objects.all()
            if c >= 1:
                come = UserT.objects.filter(c_username=name)
                global user_login
                user_login = come
                return render(request, 'OP_GG.HTML', {'come': come, 'txt': ppt})
            else:
                return render(request, 'woring1.html')
        else:
            return render(request, 'woring2.html')


# 注册
def register_view(request):
    if request.method == 'GET':
        return render(request, 'OP.GG.html')
    if request.method == 'POST':
        name = request.POST.get("name", '')
        ema_il = request.POST.get("email", "")
        pwd = request.POST.get("password", '')
        ti_me = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sex = request.POST.get("sex", '')
        if name and pwd:
            c = UserT(c_user_sex=sex, c_username=name, c_user_password=pwd, c_user_email=ema_il, c_joindate=ti_me)
            c.save()
            User.objects.create_user(username=name, password=pwd)
            return render(request, 'registersucess.html')
        else:
            return render(request, 'woring3.html')


# 用户修改喜好功能
def alter_user(request):
    global user_login
    if request.method == 'POST':
        name=''
        for i in user_login:
            name=i.c_username
            break

        sign = request.POST.get("show", '')
        sex = request.POST.get("sex", '')
        Special = request.POST.get("like", '')
        passward = request.POST.get("password", '')
        em_ail= request.POST.get("email",'')
        if name and passward:
            UserT.objects.filter(c_username=name).update(c_user_password=passward,c_user_sex=sex,c_special_concern=Special, c_user_sign=sign,c_user_email=em_ail)
            u=User.objects.get(username=name)
            u.set_password(passward)
            u.save()
            return render(request, 'editsucess.html')
        else:
            return render(request, 'woring4.html')

    return redirect('http://127.0.0.1:8000/ob_gg/', {"come": user_login})

# 注销
def log_out(request):
    return redirect("http://127.0.0.1:8000/ob_gg/")


# 查找比赛
def search(request):
    global user_login
    if request.method == 'POST':
        searchtype=request.POST.get("type",'')
        if searchtype=='1':
            #查一个战队
            time=request.POST.get("ty",'')
            if time=="last":
                teamt = request.POST.get("team", '')
                with connection.cursor() as cursor:
                   cursor.execute("SELECT * FROM FUN_latest_game_n(%s,100)", [teamt])
                   row = cursor.fetchall()
                return render(request,"OP_GG_1.HTML",{"row":row ,"come": user_login} )
            elif time =="future":
                teamt = request.POST.get("team", '')
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM FUN_future_game_n(%s,100)", [teamt])
                    row = cursor.fetchall()
                return render(request, "OP_GG_3.HTML", {"row":row,"come": user_login})
        elif searchtype=='2':
            #查两个战队
            teama=request.POST.get("t1",'')
            teamb=request.POST.get("t2",'')
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM FUN_engagement_reccord(%s,%s,100)", [teama,teamb])
                row = cursor.fetchall()
            return render(request,"OP_GG_2.HTML",{ "row": row, "come": user_login})
#else:


# 赛区
def LPL_list(request):
    global user_login
    return render(request, 'OP.GG.LPL.HTML', {"come": user_login})


def LCK_list(request):
    global user_login
    return render(request, 'OP.GG.LCK.HTML', {"come": user_login})


def LCS_list(request):
    global user_login
    return render(request, 'OP.GG.LCS.HTML', {"come": user_login})


def LEC_list(request):
    global user_login
    return render(request, 'OP.GG.LEC.HTML', {"come": user_login})


def MSI_list(request):
    global user_login
    return render(request, 'OP.GG.MS.HTML', {"come": user_login})


def GF_list(request):
    global user_login
    return render(request, 'OP.GG.GF.HTML', {"come": user_login})


# 选手：

def LPL_player_list(request):
    global user_login
    player = VMaininfoPlayer.objects.filter(c_division='LPL')
    return render(request, 'OP.GG.LPL.player.HTML', {'player': player, "come": user_login})


def LCK_player_list(request):
    global user_login
    player = VMaininfoPlayer.objects.filter(c_division='LCK')
    return render(request, 'OP.GG.LCK.player.HTML', {'player': player, "come": user_login})


def LEC_player_list(request):
    global user_login
    player = VMaininfoPlayer.objects.filter(c_division='LEC')
    return render(request, 'OP.GG.LEC.player.HTML', {'player': player, "come": user_login})


def LCS_player_list(request):
    global user_login
    player = VMaininfoPlayer.objects.filter(c_division='LCS')
    return render(request, 'OP.GG.LCS.player.HTML', {'player': player, "come": user_login})


# 战队：
def LPL_team_list(request):
    global user_login
    player = VMaininfoTeam.objects.filter(c_division='LPL')
    return render(request, 'OP.GG.LPL.team.HTML', {'player': player, "come": user_login})


def LCK_team_list(request):
    global user_login
    player = VMaininfoTeam.objects.filter(c_division='LCK')
    return render(request, 'OP.GG.LCK.team.HTML', {'player': player, "come": user_login})


def LEC_team_list(request):
    global user_login
    player = VMaininfoTeam.objects.filter(c_division='LEC')
    return render(request, 'OP.GG.LEC.team.HTML', {'player': player, "come": user_login})


def LCS_team_list(request):
    global user_login
    player = VMaininfoTeam.objects.filter(c_division='LCS')
    return render(request, 'OP.GG.LCS.team.HTML', {'player': player, "come": user_login})


# 春季赛常规赛
def LPL_spring1_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='LPL春季赛(常规赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('LPL春季赛(常规赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.LPL.spring1.HTML', {'player': player, "come": user_login, "row": row})


def LCK_spring1_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='LCK春季赛(常规赛)')

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('LCK春季赛(常规赛)')")
        row = cursor.fetchall()

    return render(request, 'OP.GG.LCK.spring1.HTML', {'player': player, "come": user_login, "row": row})


def LCS_spring1_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='LCS春季赛(常规赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('LCS春季赛(常规赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.LCS.spring1.HTML', {'player': player, "come": user_login, "row": row})


def LEC_spring1_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='LEC春季赛(常规赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('LEC春季赛(常规赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.LEC.spring1.HTML', {'player': player, "come": user_login, "row": row})


# 春季赛季后赛
def LPL_spring2_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='LPL春季赛(季后赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('LPL春季赛(季后赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.LPL.spring2.HTML', {'player': player, "come": user_login, "row": row})


def LCK_spring2_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='LCK春季赛(季后赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('LCK春季赛(季后赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.LCK.spring2.HTML', {'player': player, "come": user_login, "row": row})


def LCS_spring2_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='LCS春季赛(季后赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('LCS春季赛(季后赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.LCS.spring2.HTML', {'player': player, "come": user_login, "row": row})


def LEC_spring2_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='LEC春季赛(季后赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('LEC春季赛(季后赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.LEC.spring2.HTML', {'player': player, "come": user_login, "row": row})


# 夏季赛常规赛：
def LPL_summer1_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='LPL夏季赛(常规赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('LPL夏季赛(常规赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.LPL.summer1.HTML', {'player': player, "come": user_login, "row": row})


def LCK_summer1_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='LCK夏季赛(常规赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('LCK夏季赛(常规赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.LCK.summer1.HTML', {'player': player, "come": user_login, "row": row})


def LCS_summer1_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='LCS夏季赛(常规赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('LCS夏季赛(常规赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.LCS.summer1.HTML', {'player': player, "come": user_login, "row": row})


def LEC_summer1_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='LEC夏季赛(常规赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('LEC夏季赛(常规赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.LEC.summer1.HTML', {'player': player, "come": user_login, "row": row})


# 夏季赛季后赛:
def LPL_summer2_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='LPL夏季赛(季后赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('LPL夏季赛(季后赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.LPL.summer2.HTML', {'player': player, "come": user_login, "row": row})


def LCK_summer2_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='LCK夏季赛(季后赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('LCK夏季赛(季后赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.LCK.summer2.HTML', {'player': player, "come": user_login, "row": row})


def LCS_summer2_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='LCS夏季赛(季后赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('LCS夏季赛(季后赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.LCS.summer2.HTML', {'player': player, "come": user_login, "row": row})


def LEC_summer2_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='LEC夏季赛(季后赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('LEC夏季赛(季后赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.LEC.summer2.HTML', {'player': player, "come": user_login, "row": row})


# 季中冠军邀请赛：
def MSI_xiaozu_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='季中冠军邀请赛小组赛')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('季中冠军邀请赛小组赛')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.MS.GM.HTML', {'player': player, "come": user_login, "row": row})


def MSI_duikang_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='季中冠军邀请赛对抗赛')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('季中冠军邀请赛对抗赛')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.MS.AG.HTML', {'player': player, "come": user_login, "row": row})


def MSI_taotai_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='季中冠军邀请赛淘汰赛')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('季中冠军邀请赛淘汰赛')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.MS.EC.HTML', {'player': player, "come": user_login, "row": row})


# 全球总决赛：
def WF_xiaozu_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='全球总决赛(小组赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('全球总决赛(小组赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.GF.GM.HTML', {'player': player, "come": user_login, "row": row})


def WF_taotai_list(request):
    global user_login
    player = VMaininfoCom.objects.filter(c_match_name='全球总决赛(淘汰赛)')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FUN_view_Ranking_for_Match('全球总决赛(淘汰赛)')")
        row = cursor.fetchall()
    return render(request, 'OP.GG.GF.EC.HTML', {'player': player, "come": user_login, "row": row})

#
