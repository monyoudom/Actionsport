from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .form import  UserForm,PlaygroundForm
from .models import Playground


def index(request):
	return HttpResponse("<h1> Welcome to Sport Cambodia</h1>")
def resigster(request):

	form =UserForm(request.POST or None)
	if form.is_valid():

	 	user = form.save(commit = False)
	 	username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)
		return render(request,'Users/login.html')

	context = {
		"form": form,
	}

	return render(request,'Users/register.html',context)
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request,user)
				playground = Playground.objects.filter(user = request.user)

				return render(request,'Users/creat.html',{'playground':playground})
			else:
				return render(request,'Users/login.html',{'error_message':'Your account has been disabled'})
		else:
			return render (request,'Users/login.html',{'error_message':'Indvaile'})
	return render(request,'Users/login.html')
def playground(request):
	if not request.user.is_authenticated():
		return HttpResponse("<h1>Come Again</h1>")
	else:
		form = PlaygroundForm(request.POST)

		if form.is_valid():
			playground = form.save(commit= False)
			playground.user = request.user
			playground.save()
			return HttpResponse("<h1>Good Job </h1>")
		commit = {
			'form' : form

		}
	return render(request,'Users/playground.html')
def logouts(request):
	logout(request)
	form = UserForm(request.POST or None)
	context= {
	'form':form
	}
	return render(request,'Users/login.html',context)
