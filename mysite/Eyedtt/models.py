# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ElectionsCandidate(models.Model):
    name = models.CharField(max_length=10)
    introduction = models.TextField()
    area = models.CharField(max_length=15)
    party_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'elections_candidate'


class Ground(models.Model):
    g_name = models.CharField(primary_key=True, max_length=50)
    g_place = models.CharField(max_length=20)
    g_address = models.CharField(max_length=255, blank=True, null=True)
    g_call = models.CharField(max_length=15, blank=True, null=True)
    g_url = models.CharField(max_length=255, blank=True, null=True)
	
    def __str__(self):
    	return self.g_name
    class Meta:
        managed = False
        db_table = 'ground'


class Matchmake(models.Model):
    m_num = models.IntegerField(primary_key=True)
    t_num = models.ForeignKey('Team', models.DO_NOTHING, db_column='t_num')
    m_stat = models.IntegerField()
    m_create_time = models.DateTimeField(blank=True, null=True)
    m_money = models.IntegerField(blank=True, null=True)
    g_name = models.ForeignKey(Ground, models.DO_NOTHING, db_column='g_name', blank=True, null=True)
    m_time = models.DateTimeField(blank=True, null=True)
    m_message = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matchmake'


class Matchwant(models.Model):
    m_num = models.ForeignKey(Matchmake, models.DO_NOTHING, db_column='m_num', primary_key=True)
    t_num = models.ForeignKey('Team', models.DO_NOTHING, db_column='t_num')
    w_create_time = models.DateTimeField(blank=True, null=True)
    w_result = models.IntegerField()
    w_cancel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'matchwant'
        unique_together = (('m_num', 't_num'),)


class Player(models.Model):
    p_num = models.IntegerField(primary_key=True)
    t_num = models.ForeignKey('Team', models.DO_NOTHING, db_column='t_num')
    p_name = models.CharField(max_length=10)
    p_age = models.IntegerField(blank=True, null=True)
    p_power = models.IntegerField(blank=True, null=True)
    p_position = models.CharField(max_length=10, blank=True, null=True)
    p_call = models.CharField(max_length=15, blank=True, null=True)
    p_pro = models.IntegerField(blank=True, null=True)
    p_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player'
        unique_together = (('p_num', 't_num'),)
'''
class Point(models.Model):
    my_num = models.ForeignKey('Team', models.DO_NOTHING, db_column='my_num', primary_key=True)
    op_num = models.ForeignKey('Team', models.DO_NOTHING, db_column='op_num')
    point = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'point'
        unique_together = (('my_num', 'op_num'),)
'''

class Season(models.Model):
    t_num = models.ForeignKey('Team', models.DO_NOTHING, db_column='t_num', primary_key=True)
    s_day = models.IntegerField()
    vii = models.IntegerField(blank=True, null=True)
    viii = models.IntegerField(blank=True, null=True)
    ix = models.IntegerField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    xi = models.IntegerField(blank=True, null=True)
    xii = models.IntegerField(blank=True, null=True)
    xiii = models.IntegerField(blank=True, null=True)
    xiv = models.IntegerField(blank=True, null=True)
    xv = models.IntegerField(blank=True, null=True)
    xvi = models.IntegerField(blank=True, null=True)
    xvii = models.IntegerField(blank=True, null=True)
    xviii = models.IntegerField(blank=True, null=True)
    ixx = models.IntegerField(blank=True, null=True)
    xx = models.IntegerField(blank=True, null=True)
    xxi = models.IntegerField(blank=True, null=True)
    xxii = models.IntegerField(blank=True, null=True)
    xxiii = models.IntegerField(blank=True, null=True)
    xxiv = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'season'
        unique_together = (('t_num', 's_day'),)


class Team(models.Model):
	t_num = models.IntegerField(primary_key=True)
# id = models.IntegerField(primary_key=True)
	t_name = models.CharField(max_length=10)
	t_picture = models.CharField(max_length=255, blank=True, null=True)
	t_leader = models.CharField(max_length=10)
	t_call = models.CharField(unique=True, max_length=15)
	t_pwd = models.IntegerField()
	t_place = models.CharField(max_length=20)
	t_time = models.CharField(max_length=20)
	t_power = models.IntegerField()
	t_point = models.FloatField(blank=True, null=True)
	t_age = models.FloatField(blank=True, null=True)
	t_delete = models.IntegerField()
	
	class Meta:
		managed = False
		db_table = 'team'
