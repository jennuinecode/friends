from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User



# Create your views here.
def index(request):
	return render(request, 'manager/index.html')

def register(request):
	if request.method == "POST":
		valid, response = User.objects.validate_registration(request.POST)
		if valid:
			messages.success(request, "Congrats, {}! You've successfully registered! Now Log In!".format(response.name))
			request.session['user_id'] = response.id
			return redirect('manager:index')
		else:
			for error in response:
				messages.error(request, error)

	return redirect('manager:index')

def login(request):
	if request.method == "POST":

		valid, response = User.objects.login_check(request.POST)
		if valid:
			request.session['user_id'] = response.id
			request.session['alias'] = response.alias
			request.session['name'] = response.name

			return redirect('friends:index')


		else:
			for error in response:
				messages.error(request, error)

	return redirect('manager:index')




def view(request,id):

	if request.method == "GET":
		friend = User.objects.get(id=id)
        context= {
            'friends': User.objects.filter(id=id)
        }

	return render(request, 'manager/friendprofile.html', context)

def logout(request):
    if request.method == "POST":
        if 'user_id' in request.session:
            del request.session['user_id']
            print "user has logged out!"
    return redirect('manager:index')
