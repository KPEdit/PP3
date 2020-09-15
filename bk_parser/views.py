from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms
from . import models

# Create your views here.

def index(request):
    return render(request, 'bk_parser/index.html')


def register(request):
    if request.method == 'POST':
        form = forms.BKUserRegisterForm(request.POST)
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2 and password1 is not None:
            if form.is_valid():
                user = form._meta.model.objects.create_user(
                    username=form.instance.username,
                    name=form.instance.name,
                    last_name=form.instance.last_name,
                    email=form.instance.email,
                    password=password1
                )
                if user is None:
                    return redirect(r'/admin')
                return redirect(r"/user/login", {'success_reg': True})

    else:
        form = forms.BKUserRegisterForm()

    return render(request, 'bk_parser/register.html', {'userform':form})


def login_view(request):
    templates = dict()
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            templates['good_login'] = False

    form = forms.BKUserLogForm()
    templates['userform'] = form
    return render(request, 'bk_parser/register.html', context=templates)


def logout_view(request):
    if request.user.is_authenticated:
        # models.BKUser.objects.add_to_balance(20.555, request.user.pk)
        models.BKUser.objects.sub_to_balance(40.00, request.user.pk)
        logout(request)
        return redirect('/user/register', {'unlog':True})
    return redirect('/user/register', {'unlog':False})


def statistics(request, ck=0):
    templates = dict()
    RAW_NUM = 30
    templates['statistics'] = models.SureBet.objects.order_by(
        'is_as', 'checked')[ck*RAW_NUM:(ck+1)*RAW_NUM]
    print(templates['statistics'][0].arbit_surbets.all())
    return render(request, 'bk_parser/statistics.html', context=templates)