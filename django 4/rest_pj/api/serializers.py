from rest_framework import serializers
from accounts.models import BlogPost
from django.contrib.auth.models import User

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title','slug','author','body','publish','status','created','updated']

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input-type':'password'},write_only=True)

    class Meta:
        model = User 
        fields = ['email','username','password','password2']
        extra_kwargs = {
            'password':{    
                'write_only':True
            }
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            print(password==password2)
            raise serializers.ValidationError({'password': 'Passwords must much'})
        
        user.set_password(password)
        user.save()
        return user

class AccountPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk','email','username']