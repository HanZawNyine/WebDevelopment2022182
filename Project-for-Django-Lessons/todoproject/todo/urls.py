from django.urls import path
from . import views

app_name= "todo"

urlpatterns = [
    path('',views.home,name="all_tasks"),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/delete/',views.remove,name="delete_tasks"),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/update/',views.update,name="update_tasks"),
]
