from django.urls import path
from firstapp  import views
  
urlpatterns = [
    path("", views.page1),
    path("page2/", views.page2),
    path("page3/", views.page3),
]