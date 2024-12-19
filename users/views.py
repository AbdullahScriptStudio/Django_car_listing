from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.views import View
# Create your views here.

def login_page(request):
    if request.method =='POST':
        login_form = AuthenticationForm(request=request, data = request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            
            
            user = authenticate(username = username,  password = password)
            if user:
                login(request, user)
                messages.success(request, f'{username} welcome to our town')
                return redirect ('home')
                
    elif request.method == 'GET':
        login_form = AuthenticationForm()
    
    return render(request, 'views/login.html', {'login_form':login_form})




def register_page(request):
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            
            messages.success(request, f'You have been registered successfully.')
            
            return redirect('login')
    else:
        register_form = UserCreationForm()
    
    return render(request, 'views/register.html', {'register_form':register_form})


class Register(View):

    def get(self, request):
        register_form = UserCreationForm()
        return render(request, 'views/register.html', {'register_form':register_form})
    
    def post(self, request):
        
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            login(request, user)
            return redirect('home')
                
        else:
            register_form = UserCreationForm()
            messages.error(request, f'an error has occurred.')
            return render(request, 'view/register.html', {'register_form':register_form})
            