from . views import (
    api_detail_blog_view,
    api_update_blog_view,
    api_delete_blog_view,
    api_create_blog_view,
    
    
    register_api_view,
    ApiBlogListView,

    account_properties_view,
    account_update_view,
    )
from django.urls import path 
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'api'

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',api_detail_blog_view,name="detail"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/update',api_update_blog_view,name="update"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/delete',api_delete_blog_view,name="delete"),
    path('create',api_create_blog_view,name="create"),

    path('register',register_api_view,name='register'),
    path('login',obtain_auth_token,name="login"),

    path('list',ApiBlogListView.as_view(),name="list"),

    path('properties',account_properties_view,name="properties"),
    path('properties/update',account_update_view,name="properties"),

]