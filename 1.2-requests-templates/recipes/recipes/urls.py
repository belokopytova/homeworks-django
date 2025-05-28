from calculator.views import get_recipe

from django.urls import path

urlpatterns = [

    path('recipe/<name>/', get_recipe),

]
