from django.urls import path

from account import views

urlpatterns = [
    path("register/", views.register, name="register"),
    
    #Email doğrulama url leri
    path("email-verification/<str:uidb64>/<str:token>/", views.email_verification, name="email-verification"),
    path("email-verification-sent/", views.EmailVerificationSentView.as_view(), name="email-verification-sent"),
    path("email-verification-success/", views.EmailVerificationSuccessView.as_view(), name="email-verification-success"),
    path("email-verification-failed/", views.EmailVerificationFailedView.as_view(), name="email-verification-failed"),
    
    # login/logout url's
    path("my-login/", views.LoginView.as_view(), name="my-login"),
    path("user-logout/", views.UserLogoutView.as_view(), name="user-logout"),
    
    # dashboard/profile url's
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("profile-management/", views.ProfileManagementView.as_view(), name="profile-management"),
    path("delete-account/", views.DeleteAccountView.as_view(), name="delete-account"),
]