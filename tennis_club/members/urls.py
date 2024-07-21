from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('admin/', admin.site.urls),
    path('members/testing', views.testing, name='testing'),
    path('members/testingtwo', views.testingtwo, name='testingtwo'),
    path('members/testingthree', views.testingthree, name='testingthree'),
]