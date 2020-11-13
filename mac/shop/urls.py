from django.urls import path
from . import views

urlpatterns = [
    path("login",views.Handlelogin.as_view(),name='login'),
    path("signup",views.Handlesignup.as_view(),name='signup'),
    path("logout",views.Handlelogout.as_view(),name='logout'),
    path('dashboard',views.index,name="index"),
    path('encode',views.encode,name="encode"),
    path('decode',views.decode,name="decode")
 ]

