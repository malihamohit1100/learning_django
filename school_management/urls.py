"""
URL configuration for school_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from product.views import product_view, product_list, product_update_view, ProductListView, ProductCreateView, ProductUpdateView, test_view
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import ResisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    path('home/', views.home),
    path('product/', ProductCreateView.as_view() , name='product'),
    path('product_list/', ProductListView.as_view(), name='ProductListView'),
    path('product/<int:pk>/', ProductUpdateView.as_view(), name='productUpdateView'),
    path('test_view/', test_view, name='test_view'),
    path('resister/', ResisterView.as_view() , name='resister'),
    path('login/', auth_views.LoginView.as_view() , name='login'),
    path('logout/', auth_views.LogoutView.as_view() , name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # Password reset request form
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(), 
         name='password_reset'),

    # Confirmation that reset email was sent
    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(), 
         name='password_reset_done'),

    # Link from email → form to enter new password
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(), 
         name='password_reset_confirm'),

    # Confirmation that password has been successfully reset
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(), 
         name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
