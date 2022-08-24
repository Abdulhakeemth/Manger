
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Userwait,Country,State
from django.contrib.auth import authenticate


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','country']



class StateSerializerplus(serializers.ModelSerializer):
    country = CountrySerializer()
    class Meta:
        model = State
        fields = ['id','country','state']      

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id','state']




class UserwaitSerializerplus(serializers.ModelSerializer):
    state=StateSerializerplus()
    class Meta:
        model = Userwait
        fields = ['id','state','username','firstname','lastname','gender','email','empimage','password'] 

class UserwaitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userwait
        fields = ['id','username','firstname','lastname','gender','email','empimage','password'] 




class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['username','first_name','last_name','password','is_staff','email']

    def create(self, validated_data):
        user =    user = User.objects.create_user(**validated_data)
        return user    

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['username','password']        
