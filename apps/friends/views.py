from django.shortcuts import render, redirect
from ..manager.models import User

def index(request):

	user = request.session['user_id']
	context = {
		'users' : User.objects.all(),
		'friends': User.objects.filter(friend=user)

	}

	return render(request, 'friends/index.html', context)

def add(request, id):



	user_id = request.session['user_id']

	new_friend = User.objects.get(id=id)
	user = User.objects.get(id=user_id)
	new_friend.friend.add(user)
	new_friend.save()


	return redirect('friends:index')

def remove(request, id):


    user_id = request.session['user_id']

    my_friend = User.objects.get(id=id)
    user = User.objects.get(id=user_id)
    my_friend.friend.remove(user)
    my_friend.save()


    return redirect('friends:index')

def view(request, id):

    context= {
        'friends': User.objects.filter(id=id)
    }
    friend = User.objects.get(id=id)

    return render(request, 'friends/friendprofile.html', context)
