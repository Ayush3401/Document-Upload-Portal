
from django.urls import path
from main import views
from django.contrib.auth import views as auth
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.firstpage, name="first_page"),
    path('password_reset_request', auth.PasswordResetView.as_view(
        template_name='password/password_reset_form.html'), name='password_reset_request'),
    path('password_reset/done/', auth.PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth.PasswordResetConfirmView.as_view(
        template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth.PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html'), name='password_reset_complete'),

    path('home/<int:folder_id>/upload/', views.uploadFile, name='upload_file'),
    path('home/', views.folder_view, name='home'),
    path('home/addFolder/<int:folder_id>/',
         views.create_folder, name='addFolder'),
    path('<int:folder_id>/files/', views.file_view, name='view_files'),
    path('<int:parent_id>/<int:folder_id>/files/newname/',
         views.renamefolder, name='renamefolder'),
    path('<int:parent_id>/files/<int:file_id>/newname/',
         views.renamefile, name='renamefile'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
