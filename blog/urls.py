from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='blog'),

    #sets a path for id from views detail function
    path('<int:blog_id>/', views.details, name='details')

] 
