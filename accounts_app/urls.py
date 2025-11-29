from django.urls import path
from .views import login_view, logout_view, register_view
from .views import users_list_view, edit_user_view, delete_user_view
from .views import deactivate_user_view, activate_user_view, reset_password_view


app_name = "accounts_app"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("users/", users_list_view, name="users"),
    
]

urlpatterns += [
    path("users/edit/<int:user_id>/", edit_user_view, name="edit_user"),
    path("users/delete/<int:user_id>/", delete_user_view, name="delete_user"),
]

urlpatterns += [
    path("users/deactivate/<int:user_id>/", deactivate_user_view, name="deactivate_user"),
    path("users/activate/<int:user_id>/", activate_user_view, name="activate_user"),
    path("users/reset-password/<int:user_id>/", reset_password_view, name="reset_password"),
]
