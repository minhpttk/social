from django.urls import path, include
from users.views.auth import RegisterView, LoginView
from users.views.user import CmsListUserView, CmsUserRoleUpdateView
from users.views.transaction import CmsUpdateUserBalanceView
from users.views.cms_auth import CmsLoginView
urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("cms/", include([
        path("users", CmsListUserView.as_view(), name = "cms_list_user" ),
        path('balances', CmsUpdateUserBalanceView.as_view(), name='update_user_balance'),
        path('user-roles', CmsUserRoleUpdateView.as_view(), name='user_role_update'),
        path('login', CmsLoginView.as_view(), name="cms_login")
    ]))
]
