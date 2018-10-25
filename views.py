from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(request):
    user = User.objects.all()
    context = {
        'user' : user,
    }
    return render(request, "semi_users/index.html", context)

def create(request):
    return render(request, "semi_users/create.html")

def add(request):
    p = request.POST

    if request.method == 'POST':

        error = False
        if len(p['name']) < 1:
            messages.error(request, 'Name cannot be empty')
            error = True

        if len(p['email']) < 1:
            error = True
            messages.error(request, 'Email cannot be empty')

        if len(p['email']) > 1:
            try:
                check = User.objects.get(email=p['email'])
                error=True
                messages.error(request, "Already Registered")
                print('Already Registered')
                return redirect('/create')
            except:
                user = User.objects.create(name=p['name'], email=p['email']) 
                print(user.__dict__)
                return redirect('/create')

def edit(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user' : user
    }
    return render(request, "semi_users/edit.html", context)

def update(request, user_id):
    user = User.objects.get(id=user_id)
    user.name = request.POST['name']
    user.email = request.POST['email']
    user.save()
    return redirect('/edit/{}'.format(user_id))

def show(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user' : user
    }
    return render(request, "semi_users/show.html", context)

def delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/')


# Create your views here.
