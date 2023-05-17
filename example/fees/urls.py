from . import views
from django.urls import path
urlpatterns = [
    path("feesdj/", views.fees_django),
    path('feespy/', views.fees_py)
]