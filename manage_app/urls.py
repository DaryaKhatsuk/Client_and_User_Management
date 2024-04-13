from django.urls import path
from .views import error_frame_view, homepage_view, login_view, logout_view, account_view, login_failed_view,\
    change_status, support_view, support_done_view

urlpatterns = [
    path('', homepage_view, name='homepage'),

    path('login/', login_view, name='login'),
    path('login_failed/', login_failed_view, name='login_failed'),
    path('logout/', logout_view, name='logout'),
    path('account/', account_view, name='account'),

    path('change_status/', change_status, name='change_status'),

    path('support/', support_view, name='support'),
    path('support/support_done/', support_done_view, name='support_done'),

    path('error_frame/', error_frame_view, name='error_frame'),
]
