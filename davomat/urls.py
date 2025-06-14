from django.urls import path
from . import views
from .views import home_page,davomat_page,xodimlar_page,dashboard_page,delete_employe,delete_davomat,update_employe
urlpatterns=[
    path('', home_page, name='home'),
    path('davomatlar/', davomat_page, name='davomat'),
    path('xodim/', xodimlar_page, name='xodimlar'),
    path('dashboardlar/', dashboard_page, name='dashboard'),
    path('delete/<int:id>/', delete_employe, name='delete'),
    path('deletedavomat/<int:id>/', delete_davomat, name='deleteD'),
    path('updateddavomat/<int:id>/', update_employe, name='updated'),
  path('signup/', views.SignupView.as_view(), name='sn'),
    path('login/', views.LoginView.as_view(), name='ln'),
    path('logout/', views.LogoutView.as_view(), name='lt'),




]



