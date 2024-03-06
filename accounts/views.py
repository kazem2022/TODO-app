from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

class LoginView(View):
    
    def get(self, request):
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "login.html", context=context)

    def post(self, request):
        if  not request.user.is_authenticated:
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/tasks')  # Redirect to the appropriate URL after successful login
            return HttpResponseRedirect('/')  # Redirect back to the login page if authentication fails
        else:
            return redirect("/tasks")
        
# @login_required       
class LogoutView(View):
    
    def get(self, request):
        logout(request)                  
        return redirect("/")
 
 