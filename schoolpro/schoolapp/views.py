from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def fun_home(request):
    return render(request, "index.html")


def fun_reg(request):
    if request.method == 'POST':
        usrname = request.POST['v_usrname']
        pass1 = request.POST['v_pass']
        cpass = request.POST['v_cpass']
        if pass1 == cpass:
            if not usrname:
                print("Enter username")
                return redirect('school:reg')
            elif User.objects.filter(username=usrname).exists():
                messages.info(request, "Username already exists")
                print("username taken")
                return redirect('school:reg')
            else:
                objUser = User.objects.create_user(username=usrname, password=pass1)
                objUser.save()
                print('user saved')
                return redirect('school:log')
        else:
            messages.info(request, "Password not matching")
            print("Password not matching")
            return redirect('school:reg')

    return render(request, 'register.html')


def fun_main(request):
    return render(request, "index2.html")


def fun_login(request):
    if request.method == 'POST':
        rusr = request.POST['v_usr']
        rpass = request.POST['v_pass']
        user = auth.authenticate(username=rusr, password=rpass)

        if user is not None:
            auth.login(request, user)
            return redirect('school:main')
        else:
            messages.info(request, "Invalid credentials")
            print("Invalid credentials")
            return redirect('school:log')
    return render(request, 'login.html')


def fun_logt(request):
    auth.logout(request)
    return redirect('/')


def fun_app(request):
    if request.method == 'POST':

        # met1,met2,met3
        selected_options = request.POST.getlist('met')
        print(selected_options)

        v_name = request.POST['v_name']
        v_dob = request.POST['v_dob']
        v_age = request.POST['v_age']
        v_gender = request.POST.get('v_gender')
        v_phone = request.POST['v_phone']
        v_mail = request.POST['v_mail']
        v_met = request.POST.getlist('met')

        if not v_name:
            messages.info(request, "Enter Name")
            return redirect('school:app')
        elif not v_dob:
            messages.info(request, "Select Date of Birth")
            return redirect('school:app')
        elif not v_gender:
            messages.info(request, "Select Gender")
            return redirect('school:app')
        elif not v_age:
            messages.info(request, "Enter Age")
            return redirect('school:app')
        elif not v_phone:
            messages.info(request, "Enter Phone Number")
            return redirect('school:app')
        elif not v_mail:
            messages.info(request, "Enter Mail Address")
            return redirect('school:app')
        elif len(v_met) == 0:
            messages.info(request, "Select at-least one material")
            return redirect('school:app')
        else:
            messages.info(request, "Your Order is Confirmed")
            return render(request, 'final.html')

    return render(request, 'application.html')
