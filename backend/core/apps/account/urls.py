from .api import UserCreateView, UserDetail, TokenObtainPairView, AddressCreateView
from rest_framework_simplejwt import views as jwt_views
from django.urls import path

app_name = 'account'

urlpatterns = [
  path('register', UserCreateView.as_view(), name=UserCreateView.name),
  path('<int:pk>', UserDetail.as_view(), name=UserDetail.name),
  path('address', AddressCreateView.as_view(), name=AddressCreateView.name),
  path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]