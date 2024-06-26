from django.urls import path

from . import views


app_name = "accounts"
urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("signup/", views.CustomSignupView.as_view(), name="signup"),
    path("me/edit/", views.ProfileEditView.as_view(), name="profile_edit"),
    path("settings/", views.SettingView.as_view(), name="settings"),
    path("@<str:username>/follow/", views.AddFollowView.as_view(), name="follow"),
    path("@<str:username>/", views.ProfileView.as_view(), name="profile"),
        # path(
    #     "@<str:username>/followers/", views.FollowerListView.as_view(), name="followers"
    # ),
    path(
        "password-change/",
        views.CustomPasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password-change/done/",
        views.CustomPasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "password-reset/",
        views.CustomPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        views.CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset/confirm/<uidb64>/<token>/",
        views.CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        views.CustomPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
