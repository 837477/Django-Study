from django.urls import path
from django.contrib.auth import views as auth_views  # 쟝고 자체적으로 구현이 되어 있는 auth view
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
