from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import UserForm, LoginForm
from datetime import datetime

#from django.contrib.auth.forms import UserCreationForm
from .forms import *
id =0
def login(request):
	if request.method =="POST": 
#	form = UserForm(request.POST)
		phonenumber = request.POST.get('Phone_number_input')
		print(phonenumber)
		password = request.POST.get('password_input')
		print(password)
		try:
			team = Team.objects.get(t_call=phonenumber,t_pwd=password)
			print(team.t_call)
		except:
			return HttpResponse('비밀번호 혹은 아이디가 잘못되었습니다')
		if team is not None:
#			myteam(request,team)
#			return render (request,'Eyedtt/myteam.html',{'team':team})
			return HttpResponseRedirect("./myteam/{}/".format(team.t_num))
		else:
			return HttpResponse('로그인실패')
	else:
#		form = UserForm()
		return render(request,'Eyedtt/login.html')

def myteam(request,t_num):
	matchmakes = Matchmake.objects.filter(t_num=t_num)
	matchwants = Matchwant.objects.filter(t_num=t_num)
	matchings=[]
	for matchwant in matchwants:
		matcing=Matchmake.objects.get(m_num=matchwant.m_num)
		matchings.append(matching)
	try:
		team = Team.objects.get(t_num=t_num)
	except:
		return HttpResponseRedirect("../../login")
	try:
		players = Player.objects.filter(t_num=t_num).order_by('p_num')
	except:
		return render(request,"Eyedtt/myteam.html",{'team':team})
	if request.method =="POST":
		try:
			delect=request.POST.get('delect')
			print(delect)
			player = Player.objects.get(p_num=delect)
			player.delete()
		except:
			render(request,'Eyedtt/myteam.html',{'team':team,'players':players,'matchmakes':matchmakes,'matchings':matchings})
	else:
		#오름차순정렬
		return render(request,'Eyedtt/myteam.html',{'team':team,'players':players,'matchmakes':matchmakes,'matchings':matching})
	return render(request,'Eyedtt/myteam.html',{'team':team,'players':players,'matchmakes':matchmakes,'matchings':matching})

# return render(request, 'Eyedtt/myteam.html')
def signup(request):
	if request.method == 'POST':
		phonenumber = request.POST.get('Phone_number_input')
		if(phonenumber==""):
			return HttpResponse('번호를 입력하세요') 
		password = request.POST.get('password_input')
		if(password==""):
			return HttpResponse('비밀번호를 입력하세요')
		print(password)
		team_phonenum = phonenumber
		team_password = password
		
		redirect_to = reverse('enrollmentteam', kwargs={'team_phonenum':team_phonenum,'team_password':team_password})
		return HttpResponseRedirect(redirect_to)
		
	else:
		return render(request, 'Eyedtt/signup.html')

def enrollmentteam(request, team_phonenum, team_password):
	if request.method == 'POST':
		teams = Team.objects.all()
		teams_size = len(teams)

		newteam_phonenum = team_phonenum
		newteam_password = team_password
		newteam_name = request.POST.get('team_name')
		if(newteam_name == ""):
			return HttpResponse('팀이름을  입력하세요')
		newteam_leader = request.POST.get('team_leader')	
		if(newteam_leader == ""):
			return HttpResponse('이름을  입력하세요')
		newteam_place = request.POST.get('team_place')
		if(newteam_place == ""):
			return HttpResponse('주 활동지역을 고르세요')
		newteam_time = request.POST.get('team_time')
		if(newteam_time == ""):
			return HttpResponse('주 활동시간을 고르세요')
		newteam_power = request.POST.get('team_power')
		if(newteam_power == ""):
			return HttpResponse('팀 실력을 고르세요')

		if newteam_power == '상':
			newteam_power = 3
		elif newteam_power == '중':
			newteam_power = 2
		elif newteam_power == '하':
			newteam_power = 1
		
	
		for team in teams:
			if team.t_call == newteam_phonenum:
				return HttpResponse('이미 가입되어있는 번호입니다.')
		else:
			newteam = Team(t_num = teams_size+1, t_call=newteam_phonenum,
				t_pwd=newteam_password, t_name = newteam_name, t_leader=newteam_leader, t_place = newteam_place, t_time = newteam_time, t_power=newteam_power, t_delete=0)		
				
			newteam.save()
			return HttpResponse('팀이 등록되었습니다')
	else:
		return render(request, 'Eyedtt/enrollmentteam.html')

def teaminfo_modify(request,t_num):
	if request.method == "POST":
		team = Team.objects.get(t_num=t_num)
		team_name = request.POST.get('team_name')
		team_area = request.POST.get('team_area')
		team_time = request.POST.get('team_time')
		team_power = request.POST.get('team_power')
		team.t_name = team_name
		if team_name == "":
			return HttpResponse('팀이름을 입력해 주십시오.')
		team.t_place = team_area
		if team_area == "":
			return HttpResponse('활동지역을 입력해 주십시오.')
		team.t_time = team_time
		team.power = team_power
		team.save()
		return HttpResponse('수정되었습니다')
	else:
		return render(request, 'Eyedtt/teaminfo_modify.html')

def groundlist(request,t_num):
    return render(request, 'Eyedtt/groundlist.html',{'t_num':t_num})

def groundlist_nologin(request):
	return render(request, 'Eyedtt/groundlist_nologin.html')


def manorevaluation(request,t_num, another_t_num):
	if request.method == "POST":
		newpoint = request.POST.get('manner_input')
		

	else:
		team = Team.objects.get(t_num=t_num)
		another_team = Team.objects.get(t_num=another_t_num)
		return render(request, 'Eyedtt/manorevaluation.html',{'team':team,'another_team':another_team})

def matching(request, t_num):
	make_matchings = Matchmake.objects.filter(t_num = t_num)
	want_matchings = Matchwant.objects.filter(t_num = t_num)
	team = Team.objects.get(t_num = t_num)

#matchings = Matchmake.objects.filter(m_num = want_matchings.m_num)
	for make_matching in make_matchings:
		print('g_name: ',make_matching.g_name)



	matchings = []
	for want_matching in want_matchings:
		matching = {}
		matching = Matchmake.objects.get(m_num = want_matching.m_num)		
		matchings.append(matching)

	all_matchings = Matchmake.objects.all()
	
	
	

	context = {'make_matchings': make_matchings,
		'want_matchings': want_matchings, 'team':team, 'matchings':matchings,
	'all_matchings':all_matchings,'t_num':t_num}

	return render(request, 'Eyedtt/matching.html', context)

def enrollmentmatching(request, t_num):

	grounds = Ground.objects.all()
	context = {'grounds': grounds}

	if request.method == 'POST':
	
		matchings = Matchmake.objects.all()
		num = 0
		for matching in matchings:
			num += 1
		
#team = Team.objects.get(t_num = t_num)

		newmatching_mnum = num
		newmatching_tnum = t_num
		newmatching_message= request.POST.get('newmatching_message')
		if newmatching_message == "":
			return HttpResponse('메시지를 남겨주세요')
		newmatching_mtime= request.POST.get('newmatching_mtime')
		if newmatching_mtime == "":
			return HttpResponse('경기시간을 고르세요')
		newmatching_gname= request.POST.get('newmatching_gname')
		if newmatching_gname == "":
			return HttpResponse('경기장을 고르세요')
#print('g_name : ',newmatching_gname)
		newmatching_money= request.POST.get('newmatching_money')
		if newmatching_money == "":
			return HttpResponse('대관료를 명시하세요')
		newmatching_mstat= request.POST.get('newmatching_mstat')
#newmatching_create= datetime.datetime.now()
#		newmatching_create= 1
		
		ground = Ground.objects.get(g_name = newmatching_gname)
		team = Team.objects.get(t_num = t_num)
		if newmatching_mstat == '홈':
			newmatching_mstat = 1
		elif newmatching_mstat == '원정':
			newmatching_mstat = 2
		else:
			return HttpResponse('매칭 상태는 필수 입력사항입니다.')

		if newmatching_gname == "":
			matchmake = Matchmake(m_num = newmatching_mnum,t_num=team,m_message = newmatching_message,m_time = newmatching_mtime,m_money = newmatching_money, m_stat = newmatching_mstat)
			matchmake.save()
			return HttpResponse('매칭이 등록되었습니다.')
		else:
			matchmake = Matchmake(m_num = newmatching_mnum,t_num=team, m_message = newmatching_message,	m_time = newmatching_mtime, g_name = ground,m_money = newmatching_money, m_stat = newmatching_mstat)
			matchmake.save()
			return HttpResponse('매칭이 등록되었습니다.')

	else:
		return render(request, 'Eyedtt/enrollmentmatching.html', context)
	

def detailmatching(request,t_num, m_num):
	matchmake = Matchmake.objects.get(m_num=m_num)
	print(matchmake.g_name)
	team = Team.objects.get(t_num = t_num)
	ground = Ground.objects.get(g_name = matchmake.g_name)
	return render(request, 'Eyedtt/detailmatching.html',{'matchmake':matchmake,'t_num':t_num, 'ground':ground, 'team':team})


def matchingstate_modify(request):
    return render(request, 'Eyedtt/matchingstate_modify.html')

def main(request):
    return render(request, 'E.html')

def detailoperandteam(request,t_num,another_t_num):
	team=Team.objects.get(t_num=t_num)
	players=Player.objects.filter(t_num=another_t_num)
	another_team=Team.objects.get(t_num=another_t_num)
	matchmakes = Matchmake.objects.filter(t_num=another_t_num)
	matchwants = Matchwant.objects.filter(t_num=another_t_num)
	matchings=[]
	for matchwant in matchwants:
		matching=Matchmake.objects.get(m_num=matchwant.m_num)
		print("메세지:",matching.m_message)
		matchings.append(matching)
	
	return render(request, 'Eyedtt/detailoperandteam.html',{'team':team,'players':players,'another_team':another_team,'matchmakes':matchmakes,'matchings':matchings})

#def framepage(request):
#    return render(request, 'Eyedtt/framepage.html')

def addplayer(request,t_num):
	if request.method =='POST':
		player_tnum = t_num
		player_num = request.POST.get('player_num')
		if player_num == "" :
			return HttpResponse("선수 번호,이름,나이는 필수 입력사항입니다.")
		player_name = request.POST.get('player_name')
		if player_name == "" :
			return HttpResponse("선수 번호,이름,나이는 필수 입력사항입니다.")
		player_age = request.POST.get('player_age')
		if player_age == "" :
			return HttpResponse("선수 번호,이름,나이는 필수 입력사항입니다.")
		player_power = request.POST.get('player_power')
		player_position = request.POST.get('player_position')
		player_pro = request.POST.get('player_pro')
		player_call = request.POST.get('player_call')
		if player_pro == 'O':
			player_pro = 1
		else:
			player_pro = 0
	
		if player_power == '상':
			player_power = 3
		elif player_power == '중':
			player_power = 2
		elif player_power == '하':
			player_power = 1
		print(player_num)
		players=Player.objects.all()
		for player in players:
			print(player.p_num)
			if player.p_num == int(player_num):
				return HttpResponse('선수번호는 중복될수없습니다.')
		else:	
			player=Player(t_num=Team.objects.get(t_num=t_num),p_num=player_num,p_name=player_name,p_age=player_age,p_power=player_power,p_position=player_position,p_pro=player_pro,p_call=player_call,p_delete=0)
			player.save()
			return HttpResponse('선수가 추가되었습니다.')
	else:
		return render(request,'Eyedtt/addplayer.html')
def teamsimpleinfo(request,t_num,another_t_num):
	team=Team.objects.get(t_num=t_num)
	players=Player.objects.filter(t_num=another_t_num)
	another_team=Team.objects.get(t_num=another_t_num)
	return render(request, 'Eyedtt/teamsimpleinfo.html',{'team':team,'another_team':another_team,'players':players})

def teamsimpleinfo_nologin(request):

    return HttpResponse("세부정보를 조회하려면 로그인을 해주십시오.")

def enrollmentteamlogo(request):
    return render(request, 'Eyedtt/enrollmentteamlogo.html')

def teamlist_nologin(request):
	teams=Team.objects.all()
	return render(request,'Eyedtt/teamlist_nologin.html',{'teams':teams})

def teamlist(request,t_num):
	teams=Team.objects.all()
	return render(request, 'Eyedtt/teamlist.html',{'teams':teams,'t_num':t_num})

