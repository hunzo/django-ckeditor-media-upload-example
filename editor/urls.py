from django.urls import path
from . import views


urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("update/<int:pk>", views.UpdatePostView.as_view(), name="update"),
    path("<int:pk>/delete", views.DeletePostView.as_view(), name="delete")
]
