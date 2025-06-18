from django.urls import path
from .views import TopUpOrderAPIView, Base,Login,Signup,Dashboard,Logout

urlpatterns = [
    path('', Base, name='Base'),
    path('login/', Login, name='login'),
    path('signup/', Signup, name='signup'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('api/topup/', TopUpOrderAPIView.as_view(), name='topup-api'),
    path('logout/', Logout,name = 'logout')
]
