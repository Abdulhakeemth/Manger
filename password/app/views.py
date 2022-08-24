from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Userwait
from .serializers import UserwaitSerializerplus,SignupSerializer,LoginSerializer,CountrySerializer,StateSerializer,UserwaitSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# ==================For showing in admindashboard=====================
class Employeewaitlist(APIView):
    def get(self, request, format=None):
        employeesdetails = Userwait.objects.all()
        serializer = UserwaitSerializerplus(employeesdetails,many=True)
        return Response(serializer.data)

# =================For deleting after approving in admindashboard============
class EmployeeDetailEdit(APIView):
    def delete(self, request,pk, format=None):
        employee = Userwait.objects.get(id=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# =================For creating user in admindashboard==================
class Signupuser(APIView):
    def get(self, request, format=None):
        employeesdetails = User.objects.all()
        serializer = SignupSerializer(employeesdetails,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ==============For saving country,state & Employee====================
class Savecountry(APIView):
    def get(self, request, format=None):
        employeesdetails = User.objects.all()
        serializer = SignupSerializer(employeesdetails,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Savestate(APIView):
    def get(self, request, format=None):
        employeesdetails = User.objects.all()
        serializer = SignupSerializer(employeesdetails,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Checkuserwait(APIView):
    def get(self, request, format=None):
        employeesdetails = User.objects.all()
        serializer = SignupSerializer(employeesdetails,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserwaitSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Saveuserwait(APIView):
    def get(self, request, format=None):
        employeesdetails = User.objects.all()
        serializer = SignupSerializer(employeesdetails,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserwaitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class Loginuser(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            print(request.data['username'])
            print(request.data['password'])
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username,password=password)
            print(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
