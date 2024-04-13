# from django.contrib.auth.models import User
import json
from datetime import date

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from Client_and_User_Management.settings import SESSION
from .forms import LoginForm, SupportForm
from .management.commands.emails import support_email
from .management.commands.people_generation import generate_data
from .models import Client, User


def homepage_view(request):
    try:
        if len(User.objects.all()) > 0:
            if isinstance(request.session.get(SESSION, {}).get('id', {}), int):
                return redirect('account')
            else:
                return redirect('login')
        else:
            generate_data()
            return redirect(request.path_info)
    except Exception as ex:
        print(ex)
        return redirect('error_frame')


"""
login, logout
"""


def login_view(request):
    try:
        if isinstance(request.session.get(SESSION, {}).get('id', {}), int):
            return redirect('account')
        else:
            if request.method == "POST":
                user_form = LoginForm(data=request.POST)
                user = User.objects.filter(username=user_form.data.get('username'),
                                           password=user_form.data.get('password'),
                                           )
                if user.exists():
                    request.session[SESSION] = {
                        'id': User.objects.get(username=user_form.data.get('username'),
                                               password=user_form.data.get('password'),
                                               ).id,
                    }
                    return redirect('homepage')
                else:
                    return redirect('login_failed')
        context = {
            'form': LoginForm(),
        }
        return render(request, 'accounts/login.html', context)
    except Exception as ex:
        print(ex)
        return redirect('error_frame')


def login_failed_view(request):
    try:
        context = {
        }
        return render(request, 'accounts/login_failed.html', context)
    except Exception as ex:
        print(ex)
        return redirect('error_frame')


def account_view(request):
    # try:
        print(request.session.get(SESSION, {}).get('id', {}))
        user_id = request.session.get(SESSION, {}).get('id', {})
        print(user_id)
        user = User.objects.get(id=user_id)
        clients = Client.objects.filter(responsible_person=user.id)
        print(clients)

        context = {
            'user': user,
            'clients': clients,
        }
        print(context)
        return render(request, 'accounts/account.html', context)
    # except Exception as ex:
    #     print(ex)
    #     return redirect('error_frame')


def logout_view(request):
    request.session.pop(SESSION, {}).get('id', {})
    print(request.session.pop(SESSION, {}).get('id', {}))
    return redirect('homepage')


"""
Client
"""


def change_status(request):
    if request.method == 'GET':
        client_id = request.GET.get('client_id')
        status = request.GET.get('status')

        try:
            client = Client.objects.get(id=client_id)
            client.status = status
            client.save()

            return JsonResponse({'success': True})
        except Client.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Client does not exist'})


# def client_view(request, client_id):
#     try:
#         # print(client_id, user_id)
#         user_id = request.session.get(SESSION, {}).get('id', {})
#         user = User.objects.get(id=user_id)
#         client = Client.objects.get(id=client_id, responsible_person=user)
#         # if request.method == 'POST':
#         #     form = UpdateClientStatusForm(request.POST)
#         #     if form.is_valid():
#         #         new_status = form.cleaned_data['status']
#         #         client.status = new_status
#         #         client.save()
#         #     return redirect(request.path_info)
#         print(client)
#         context = {
#             'client': client,
#         }
#         print(context)
#         return render(request, 'clients/client.html', context)
#     except Exception as ex:
#         print(ex)
#         return redirect('error_frame')


"""
Support
"""


def support_view(request):
    try:
        if request.method == 'POST':
            support_form = SupportForm(data=request.POST)
            if support_form.is_valid():
                support_email(date.today(), support_form.data.get('email'), support_form.data.get('user_text'),
                              request.user, request.COOKIES, request.META)
                return redirect('support_done')
        context = {
            'form': SupportForm(),
        }
        return render(request, 'support/support.html', context)
    except Exception as ex:
        print(ex)
        return redirect('error_frame')


def support_done_view(request):
    try:
        context = {
        }
        return render(request, 'support/support_done.html', context)
    except Exception as ex:
        print(ex)
        return redirect('error_frame')


"""
Errors
"""


def error_frame_view(request):
    context = {
    }
    return render(request, 'errors/error_frame.html', context)
