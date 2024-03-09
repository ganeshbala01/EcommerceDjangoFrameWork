from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already in use.')
            return redirect('/register')
        else:
            # Create a new user
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, password=password, email=email)
            user.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('/')
    else:
        return render(request, 'signup.html')
