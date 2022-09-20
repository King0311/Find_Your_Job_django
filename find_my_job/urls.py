from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("homepage",views.homepage,name="homepage"),
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
    path("logout", views.logout, name="logout"),
    path("hr_seeker",views.hr_seeker,name="hr_seeker"),
    path("seeker",views.seeker,name="seeker"),
    path("jobs/<str:pk>",views.jobs,name="jobs"),
    path("giver/<str:fk>",views.giver,name="giver"),
]