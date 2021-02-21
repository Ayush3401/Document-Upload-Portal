
from django.urls import path
from main import views
from django.contrib.auth import views as auth

urlpatterns = [
    
    path('password_reset_request', auth.PasswordResetView.as_view(
        template_name='password/password_reset_form.html'), name='password_reset_request'),
    path('password_reset/done/', auth.PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth.PasswordResetConfirmView.as_view(
        template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth.PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html'), name='password_reset_complete'),

    path('upload/', views.uploadFile, name='upload_file'),
    path('fileview/', views.fileview, name='view_file'),

]
