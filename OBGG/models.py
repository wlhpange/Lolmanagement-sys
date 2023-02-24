from django.db import models
class ComT(models.Model):
    c_p_match_id = models.CharField(db_column='C_P_Match_id', max_length=50)  # Field name made lowercase.
    c_p_battle_id = models.AutoField(db_column='C_P_Battle_id',primary_key=True)  # Field name made lowercase.
    c_teama = models.CharField(db_column='C_TeamA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_teamb = models.CharField(db_column='C_TeamB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_tformat = models.CharField(db_column='C_Tformat', max_length=10)  # Field name made lowercase.
    c_score = models.CharField(db_column='C_Score', max_length=20, blank=True, null=True)  # Field name made lowercase.
    c_time_field = models.DateTimeField(db_column='C_Time_')  # Field name made lowercase. Field renamed because it ended with '_'.
    c_commentary = models.CharField(db_column='C_Commentary', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_hostplace = models.CharField(db_column='C_Hostplace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_remarks = models.CharField(db_column='C_Remarks', max_length=500, blank=True, null=True)  # Field name made lowercase.
    def  xp1(self):
        return self.c_p_match_id
    xp1.short_description="赛事id"
    def  xp2(self):
        return self.c_p_battle_id
    xp2.short_description="比赛id"
    def  xp3(self):
        return self.c_teama
    xp3.short_description="队伍a"
    def  xp4(self):
        return self.c_teamb
    xp4.short_description="队伍b"
    def  xp5(self):
        return self.c_tformat
    xp5.short_description="赛制"
    def  xp6(self):
        return self.c_score
    xp6.short_description="比分"
    def  xp7(self):
        return self.c_time_field
    xp7.short_description="比赛时间"
    def  xp8(self):
        return self.c_commentary
    xp8.short_description="备注"
    def  xp9(self):
        return self.c_hostplace
    xp9.short_description="举办地"
    def  xp10(self):
        return self.c_remarks
    xp10.short_description="类型"
    class Meta:
        db_table = 'Com_T'
        unique_together = (('c_p_match_id', 'c_p_battle_id'),)
        verbose_name_plural = "成绩"


class MatchT(models.Model):
    c_p_f_match_id = models.CharField(db_column='C_P_F_Match_id', primary_key=True, max_length=50)  # Field name made lowercase.
    c_match_name = models.CharField(db_column='C_Match_name', max_length=50)  # Field name made lowercase.
    c_division = models.CharField(db_column='C_Division', max_length=50)  # Field name made lowercase.
    c_numteam = models.IntegerField(db_column='C_Numteam')  # Field name made lowercase.
    c_remarks = models.CharField(db_column='C_Remarks', max_length=500, blank=True, null=True)  # Field name made lowercase.
    c_ifnow = models.CharField(db_column='C_Ifnow', max_length=3, blank=True, null=True)  # Field name made lowercase.

    def xp1(self):
        return self.c_p_f_match_id

    xp1.short_description = "赛事id"

    def xp2(self):
        return self.c_match_name

    xp2.short_description = "赛事名称"

    def xp3(self):
        return self.c_division

    xp3.short_description = "赛区"

    def xp4(self):
        return self.c_numteam

    xp4.short_description = "队伍数"

    def xp5(self):
        return self.c_remarks

    xp5.short_description = "备注"

    def xp6(self):
        return self.c_ifnow

    xp6.short_description = "是否当前"

    class Meta:
        db_table = 'Match_T'
        verbose_name_plural = "赛事"
class PlayerT(models.Model):
    c_p_player_id = models.CharField(db_column='C_P_Player_id', primary_key=True, max_length=50)  # Field name made lowercase.
    c_p_team_id = models.CharField(db_column='C_P_Team_id', max_length=50)  # Field name made lowercase.
    c_pname = models.CharField(db_column='C_Pname', max_length=50)  # Field name made lowercase.
    c_pidentity = models.CharField(db_column='C_Pidentity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    c_position = models.CharField(db_column='C_Position', max_length=10, blank=True, null=True)  # Field name made lowercase.
    c_hero_1 = models.CharField(db_column='C_Hero_1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_hero_2 = models.CharField(db_column='C_Hero_2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_hero_3 = models.CharField(db_column='C_Hero_3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_previous = models.CharField(db_column='C_Previous', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_nation = models.CharField(db_column='C_Nation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_age = models.IntegerField(db_column='C_Age', blank=True, null=True)  # Field name made lowercase.
    c_game_id = models.CharField(db_column='C_Game_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_division = models.CharField(db_column='C_Division', max_length=50, blank=True, null=True)  # Field name made lowercase.
    def  xp1(self):
        return self.c_p_player_id
    xp1.short_description="选手主id"
    xp1.admin_order_field="c_p_player_id"
    def  xp2(self):
        return self.c_p_team_id
    xp2.short_description="选手所属队id"
    def  xp3(self):
        return self.c_pname
    xp3.short_description="姓名"
    def  xp4(self):
        return self.c_pidentity
    xp4.short_description="身份"
    def  xp5(self):
        return self.c_position
    xp5.short_description="位置"
    def  xp6(self):
        return self.c_hero_1
    xp6.short_description="常用英雄1"
    def  xp7(self):
        return self.c_hero_2
    xp7.short_description="常用英雄2"
    def  xp8(self):
        return self.c_previous
    xp8.short_description="常用英雄3"
    def  xp9(self):
        return self.c_nation
    xp9.short_description="国籍"
    def  xp10(self):
        return self.c_age
    xp10.short_description="年龄"
    def  xp11(self):
        return self.c_game_id
    xp11.short_description="选手id"
    def  xp12(self):
        return self.c_division
    xp12.short_description="所属赛区"
    def  xp13(self):
        return self.c_hero_3
    xp13.short_description="常用英雄3"
    class Meta:
        db_table = 'Player_T'
        unique_together = (('c_p_player_id', 'c_p_team_id'),)
        verbose_name_plural = "选手"

class TeamScoreT(models.Model):
    c_p_team_id = models.CharField(db_column='C_P_Team_id', primary_key=True, max_length=50)  # Field name made lowercase.
    c_p_match_id = models.CharField(db_column='C_P_Match_id', max_length=50)  # Field name made lowercase.
    c_score = models.IntegerField(db_column='C_Score', blank=True, null=True)  # Field name made lowercase.
    c_victory = models.IntegerField(db_column='C_Victory', blank=True, null=True)  # Field name made lowercase.
    c_defeated = models.IntegerField(db_column='C_Defeated', blank=True, null=True)  # Field name made lowercase.
    c_victory_s = models.IntegerField(db_column='C_Victory_s', blank=True, null=True)  # Field name made lowercase.
    c_defeated_s = models.IntegerField(db_column='C_Defeated_s', blank=True, null=True)  # Field name made lowercase.
    def  xp1(self):
        return self.c_p_team_id
    xp1.short_description="队伍id"
    xp1.admin_order_field="c_p_team_id"
    def  xp2(self):
        return self.c_p_match_id
    xp2.short_description="比赛id"
    def  xp3(self):
        return self.c_score
    xp3.short_description="积分"
    def  xp4(self):
        return self.c_victory
    xp4.short_description="胜场"
    def  xp5(self):
        return self.c_defeated
    xp5.short_description="败场"
    def  xp6(self):
        return self.c_victory_s
    xp6.short_description="小局胜利"
    def  xp7(self):
        return self.c_defeated_s
    xp7.short_description="小局失败"
    class Meta:
        db_table = 'Team_Score_T'
        unique_together = (('c_p_team_id', 'c_p_match_id'),)
        verbose_name_plural = "队伍积分"

class TeamT(models.Model):
    c_p_f_team_id = models.CharField(db_column='C_P_F_Team_id', primary_key=True, max_length=50)  # Field name made lowercase.
    c_team = models.CharField(db_column='C_Team', max_length=50)  # Field name made lowercase.
    c_coach = models.CharField(db_column='C_Coach', max_length=50)  # Field name made lowercase.
    c_division = models.CharField(db_column='C_Division', max_length=50)  # Field name made lowercase.
    c_introduction = models.CharField(db_column='C_Introduction', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    def  xp1(self):
        return self.c_p_f_team_id
    xp1.short_description="队伍id"
    xp1.admin_order_field="c_p_f_team_id"
    def  xp2(self):
        return self.c_team
    xp2.short_description="队名"
    def  xp3(self):
        return self.c_coach
    xp3.short_description="教练"
    def  xp4(self):
        return self.c_division
    xp4.short_description="赛区"
    def  xp5(self):
        return self.c_introduction
    xp5.short_description="介绍"
    class Meta:
        db_table = 'Team_T'
        verbose_name_plural = "队伍"

class UserT(models.Model):
    c_p_userid = models.AutoField(db_column='C_P_UserID', primary_key=True)  # Field name made lowercase.
    c_username = models.CharField(db_column='C_UserName', max_length=50)  # Field name made lowercase.
    c_user_password = models.CharField(db_column='C_User_password', max_length=50)  # Field name made lowercase.
    c_user_email = models.CharField(db_column='C_User_email', max_length=50)  # Field name made lowercase.
    c_user_sign = models.CharField(db_column='C_User_sign', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_user_sex = models.CharField(db_column='C_User_sex', max_length=2, blank=True, null=True)  # Field name made lowercase.
    c_joindate = models.DateTimeField(db_column='C_Joindate')  # Field name made lowercase.
    c_special_concern = models.CharField(db_column='C_Special_concern', max_length=50, blank=True, null=True)  # Field name made lowercase.
    def  xp1(self):
        return self.c_p_userid
    xp1.short_description="用户id"
    def  xp2(self):
        return self.c_username
    xp2.short_description="用户名"
    def  xp3(self):
        return self.c_user_password
    xp3.short_description="用户密码"
    def  xp4(self):
        return self.c_user_email
    xp4.short_description="邮件"
    def  xp5(self):
        return self.c_user_sign
    xp5.short_description="个性签名"
    def  xp6(self):
        return self.c_user_sex
    xp6.short_description="性别"
    def  xp7(self):
        return self.c_joindate
    xp7.short_description="注册时间时间"
    def  xp8(self):
        return self.c_special_concern
    xp8.short_description="主队"
    class Meta:
        db_table = 'User_T'
        verbose_name_plural = "用户副本"

class VMaininfoCom(models.Model):
    c_match_name = models.CharField(db_column='C_Match_name', primary_key=True,max_length=50)  # Field name made lowercase.
    c_teama = models.CharField(db_column='C_TeamA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_teamb = models.CharField(db_column='C_TeamB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_tformat = models.CharField(db_column='C_Tformat', max_length=10)  # Field name made lowercase.
    c_score = models.CharField(db_column='C_Score', max_length=20, blank=True, null=True)  # Field name made lowercase.
    c_time_field = models.DateTimeField(db_column='C_Time_')  # Field name made lowercase. Field renamed because it ended with '_'.
    c_remarks = models.CharField(db_column='C_Remarks', max_length=500, blank=True,null=True)  # Field name made lowercase.
    c_commentary = models.CharField(db_column='C_Commentary', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_hostplace = models.CharField(db_column='C_Hostplace', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'V_MainInfo_Com'

class VMaininfoPlayer(models.Model):
    c_team = models.CharField(db_column='C_Team', primary_key=True,max_length=50)  # Field name made lowercase.
    c_division = models.CharField(db_column='C_Division', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_game_id = models.CharField(db_column='C_Game_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_pname = models.CharField(db_column='C_Pname', max_length=50)  # Field name made lowercase.
    c_hero_1 = models.CharField(db_column='C_Hero_1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_hero_2 = models.CharField(db_column='C_Hero_2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_hero_3 = models.CharField(db_column='C_Hero_3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_pidentity = models.CharField(db_column='C_Pidentity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    c_position = models.CharField(db_column='C_Position', max_length=10, blank=True, null=True)  # Field name made lowercase.
    c_nation = models.CharField(db_column='C_Nation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_previous = models.CharField(db_column='C_Previous', max_length=50, blank=True,null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'V_MainInfo_Player'



class VMaininfoTeam(models.Model):
    c_team = models.CharField(db_column='C_Team',primary_key=True, max_length=50)  # Field name made lowercase.
    c_division = models.CharField(db_column='C_Division', max_length=50)  # Field name made lowercase.
    c_coach = models.CharField(db_column='C_Coach', max_length=50)  # Field name made lowercase.
    c_introduction = models.CharField(db_column='C_Introduction', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'V_MainInfo_Team'


class VUserCanChange(models.Model):
    c_username = models.CharField(db_column='C_UserName', primary_key=True,max_length=50)  # Field name made lowercase.
    c_user_password = models.CharField(db_column='C_User_password', max_length=50)  # Field name made lowercase.
    c_user_sign = models.CharField(db_column='C_User_sign', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_user_sex = models.CharField(db_column='C_User_sex', max_length=2, blank=True, null=True)  # Field name made lowercase.
    c_user_email = models.CharField(db_column='C_User_email', max_length=50)  # Field name made lowercase.
    c_special_concern = models.CharField(db_column='C_Special_concern', max_length=50, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'V_User_can_Change'

class Score(models.Model):
    c_team=models.CharField(TeamT,primary_key=True,max_length=50)
    c_victory=models.CharField(TeamScoreT,max_length=50)
    c_score=models.CharField(TeamScoreT,max_length=50)
    c_defeated=models.CharField(TeamScoreT,max_length=50)
    c_victorys=models.CharField(TeamScoreT,max_length=50)
    c_defeated_s=models.CharField(TeamScoreT,max_length=50)
