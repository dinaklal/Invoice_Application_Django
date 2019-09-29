from django.urls import path

from . import views


urlpatterns = [
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout'),
    path('add_site',views.add_site,name='add_site'),
    path('view_site',views.view_site,name='view_site'),
    path('process',views.process,name='process'),
    path('GeneratePdf',views.GeneratePdf,name='GeneratePdf'),
    
]
