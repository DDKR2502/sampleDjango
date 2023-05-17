from . import views
from django.urls import path
urlpatterns = [
    path("learndj/", views.learn_jango),
    path('learnpy/', views.learn_py)
]
