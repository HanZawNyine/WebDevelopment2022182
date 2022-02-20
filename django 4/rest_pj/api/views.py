from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from accounts.models import BlogPost
from django.db.models import Q
from rest_framework.authtoken.models import Token
from . serializers import BlogPostSerializer,RegisterSerializer,AccountPropertiesSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter,OrderingFilter

class ApiBlogListView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('title','body','author__username')

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def api_detail_blog_view(request, year, month, day, post):
    try:
        blog_post = BlogPost.objects.get(slug=post,    status='published',    publish__year=year,    publish__month=month,    publish__day=day)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)

@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def api_update_blog_view(request, year, month, day, post):
    try:
        blog_post = BlogPost.objects.get(slug=post,    status='published',    publish__year=year,    publish__month=month,    publish__day=day)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user = request.user
    if blog_post.author != user:
        return Response({"response":"You don't have permissions to edit that."})
    if request.method == "PUT":
        serializer = BlogPostSerializer(blog_post, data=request.data)
        data = {             
        }
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successfully"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def api_delete_blog_view(request, year, month, day, post):
    try:
        blog_post = BlogPost.objects.get(slug=post,    status='published',    publish__year=year,    publish__month=month,    publish__day=day)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if blog_post.author != user:
        return Response({"response":"You don't have permissions to delete that."})
    if request.method == "DELETE":
        operation = blog_post.delete() 
        data = {}
        if operation:            
            data["success"] = "delete successfully"
        else:
            data["failure"] = 'delete failed'
        return Response(data=data)

@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def api_create_blog_view(request):
   account = request.user
   blog_post = BlogPost(author=account)

   if request.method == "POST":
       serializer = BlogPostSerializer(blog_post,data=request.data)
       data = {}
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    #register
@api_view(['POST',])
def register_api_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully register user"
            data['email'] = account.email
            data['username']= account.username
            token= Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors    
        return Response(data)

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def account_properties_view(request):
    try:
        account = request.user
    except account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = AccountPropertiesSerializer(account)
        return Response(serializer.data )

@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def account_update_view(request):
    try:
        account = request.user
    except account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = AccountPropertiesSerializer(account,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Account Update Success"
            return Response(data=data)  
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST )