from django.urls import path
from .import views
from .views import signup_view, login_view, calculator_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('calculator/', calculator_view, name='calculator'),
]
