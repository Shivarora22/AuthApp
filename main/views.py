from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .forms import CustomerCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()

    # Ensure that render is always reached to return an HttpResponse
    return render(request, 'login.html', {'form': form})
    
#Signup View
def signup_view(request):
    if request.method== 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form= CustomerCreationForm()
    return render(request,'signup.html',{'form':form})

#Forgot Password View
def fpass_view(request):
    # Forgot password logic here
    return render(request, 'forgot_password.html')


#Change Password View
@login_required
def cpass_view(request):
    if request.method=='POST':
        form = PasswordChangeForm(user=request.user,data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,request.user)  #uses to re-authenticate
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'change_password.html',{'form':form})

#Dashboard View
def dash_view(request):
    # Ensure you're passing the request object as the first argument to render
    return render(request, 'dashboard.html', {'username': request.user.username})

#Profile Views
@login_required
def profile_view(request):
    return render(request,'profile.html',{
        'username': request.user.username,
        'email': request.user.email,
        'date_joined': request.user.date_joined,
        'last_login' : request.user.last_login,
    })

#Logout Views
def logout_view(request):
    logout(request)
    return redirect('login')