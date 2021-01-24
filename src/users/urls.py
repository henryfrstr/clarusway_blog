# from django.urls import path
# from . import views
# from django.contrib.auth import views as auth_views
# # from .forms import EmailValidationOnForgotPassword


# urlpatterns = [
#     path('register/', views.register, name='register'),
#     path('profile/', views.profile, name='profile'),
#     path('logan/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
#     path('logot/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
#     path('password-reset/', auth_views.PasswordResetView.as_view(
#         template_name='users/password_reset.html', email_template_name='users/password_reset_email.html'), name='password_reset'),
#     # path('password-reset/', auth_views.PasswordResetView.as_view(
#     #     template_name='users/password_reset.html', form_class=EmailValidationOnForgotPassword), name='password_reset'),
#     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
#         template_name='users/password_reset_done.html'), name='password_reset_done'),
#     path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
#         template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
#     path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
#         template_name='users/password_reset_complete.html'), name='password_reset_complete'),
# ]


# # login/ [name='login']
# # logout/ [name='logout']
# # password_change/ [name='password_change']
# # password_change/done/ [name='password_change_done']
# # password_reset/ [name='password_reset']
# # password_reset/done/ [name='password_reset_done']
# # reset/<uidb64>/<token>/ [name='password_reset_confirm']
# # reset/done/ [name='password_reset_complete']
