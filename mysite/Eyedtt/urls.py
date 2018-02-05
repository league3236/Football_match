from django.conf.urls import url
from django.contrib.auth.views import login,logout
from . import views 
from django.views.generic import TemplateView

urlpatterns = [
# url(r'^join/$',views.signup, name ='join'),
    url(r'^login',views.login),
	url(r'^myteam/(?P<t_num>\d+)/teaminfo_modify',views.teaminfo_modify),
	url(r'^myteam/(?P<t_num>\d+)/addplayer/',views.addplayer),
	url(r'^myteam/(?P<t_num>\d+)/$',views.myteam),
	url(r'^teamsimpleinfo/(?P<t_num>\d+)/(?P<another_t_num>\d+)/$', views.teamsimpleinfo),
	url(r'^teamsimpleinfo', views.teamsimpleinfo_nologin),
    url(r'^enrollmentteamlogo', views.enrollmentteamlogo),
    url(r'^myteam/', views.myteam),
    url(r'^teamlist/(?P<t_num>\d+/$)',views.teamlist),
	url(r'^teamlist',views.teamlist_nologin),
	url(r'^teaminfo_modify',views.teaminfo_modify),
    url(r'^groundlist/(?P<t_num>\d+)/$',views.groundlist),
	url(r'^groundlist/',views.groundlist_nologin),
    url(r'^detailoperandteam/(?P<t_num>\d+)/(?P<another_t_num>\d+)/$',views.detailoperandteam),
    url(r'^manorevaluation/(?P<t_num>\d+)/(?P<another_t_num>\d+)/$',views.manorevaluation),
    url(r'^matchingstate_modify',views.matchingstate_modify),
#    url(r'^myteam/(?P<t_num>\d+)/addplayer$',views.addplayer),
#    url(r'^matching',views.matching),
	url(r'^matching/(?P<t_num>\d+)/$',views.matching),
	url(r'^enrollmentmatching/(?P<t_num>\d+)/$',views.enrollmentmatching),
    url(r'^detailmatching/(?P<t_num>\d+)/(?P<m_num>\d+)/$',views.detailmatching),
#    url(r'^enrollmentmatching',views.enrollmentmatching),
    url(r'^main',views.main),
#    url(r'^enrollmentteam',views.enrollmentteam), 
	url(r'^signup/enrollmentteam/(?P<team_phonenum>\d+)(?P<team_password>\d+)/$',views.enrollmentteam, name='enrollmentteam'),
	url(r'^signup/', views.signup, name='signup'),
]
