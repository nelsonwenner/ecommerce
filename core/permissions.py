from rest_framework import serializers
from rest_framework import permissions
from .models import *


class ClientPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        if request.method == "GET" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)
            is_client = Client.objects.filter(email=request.user.email).exists()

            if request.user.is_superuser:
                return True
            elif is_client:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False
        
        elif request.method == "POST":
            return True

        elif request.method == "PUT" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)
            is_client = Client.objects.filter(email=request.user.email).exists()

            if request.user.is_superuser:
                return True
            elif is_client:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False
        
        elif request.method == "PATCH" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)
            is_client = Client.objects.filter(email=request.user.email).exists()

            if request.user.is_superuser:
                return True
            elif is_client:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "DELETE" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "OPTIONS":
            return True

        elif request.method == "HEAD":
            return True


class AddressPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):

        if request.method == "GET" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)
            is_client = Client.objects.filter(email=request.user.email).exists()

            if request.user.is_superuser:
                return True
            elif is_client:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False
        
        elif request.method == "POST":
            return True

        elif request.method == "PUT" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)
            is_client = Client.objects.filter(email=request.user.email).exists()

            if request.user.is_superuser:
                return True
            elif is_client:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PATCH" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)
            is_client = Client.objects.filter(email=request.user.email).exists()

            if request.user.is_superuser:
                return True
            elif is_client:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "DELETE" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "OPTIONS":
            return True

        elif request.method == "HEAD":
            return True
        

class ManagerPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
    
        if request.method == "GET" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False
        
        elif request.method == "POST":
            if request.user.is_superuser:
                return True
        
        elif request.method == "PUT" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PATCH" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "DELETE" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "OPTIONS":
            return True

        elif request.method == "HEAD":
            return True


class BookPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
  
        if request.method == "GET":
            return True
        
        elif request.method == "POST" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PUT" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PATCH" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "DELETE" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "OPTIONS":
            return True

        elif request.method == "HEAD":
            return True


class StatusPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):

        if request.method == "GET":
            return True
        
        elif request.method == "POST" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PUT" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PATCH" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "DELETE" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "OPTIONS":
            return True

        elif request.method == "HEAD":
            return True


class GenrerPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):

        if request.method == "GET":
            return True
        
        elif request.method == "POST" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PUT" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PATCH" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "DELETE" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "OPTIONS":
            return True

        elif request.method == "HEAD":
            return True


class AuthorPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
     
        if request.method == "GET":
            return True
        
        elif request.method == "POST" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PUT" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PATCH" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "DELETE" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "OPTIONS":
            return True

        elif request.method == "HEAD":
            return True


class WritePermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
    
        if request.method == "GET":
            return True
        
        elif request.method == "POST" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)
            is_client = Client.objects.filter(email=request.user.email).exists()

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PUT" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PATCH" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "DELETE" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "OPTIONS":
            return True

        elif request.method == "HEAD":
            return True
  

class OrderPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
      
        if request.method == "GET" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)
            is_client = Client.objects.filter(email=request.user.email).exists()

            if request.user.is_superuser:
                return True
            elif is_client:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "POST" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)
            is_client = Client.objects.filter(email=request.user.email).exists()

            if request.user.is_superuser:
                return True
            elif is_client:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PUT" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PATCH" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "DELETE" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "OPTIONS":
            return True

        elif request.method == "HEAD":
            return True


class ItemOrderPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
       
        if request.method == "GET" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)
            is_client = Client.objects.filter(email=request.user.email).exists()

            if request.user.is_superuser:
                return True
            elif is_client:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "POST" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)
            is_client = Client.objects.filter(email=request.user.email).exists()

            if request.user.is_superuser:
                return True
            elif is_client:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PUT" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PATCH" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)
 
            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "DELETE" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "OPTIONS":
            return True

        elif request.method == "HEAD":
            return True

        
class CreditCardPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):

        if request.method == "GET" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)
            is_client = Client.objects.filter(email=request.user.email).exists()

            if request.user.is_superuser:
                return True
            elif is_client:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "POST" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)
            is_client = Client.objects.filter(email=request.user.email).exists()

            if request.user.is_superuser:
                return True
            elif is_client:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False
          
        elif request.method == "PUT" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)
            is_client = Client.objects.filter(email=request.user.email).exists()

            if is_client:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "PATCH" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)
            is_client = Client.objects.filter(email=request.user.email).exists()

            if request.user.is_superuser:
                return True
            elif is_client:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False
        
        elif request.method == "DELETE" and request.user.is_authenticated:
            is_manager = Manager.objects.filter(email=request.user.email)

            if request.user.is_superuser:
                return True
            elif is_manager and is_manager[0].user.is_staff:
                return True
            else:
                return False

        elif request.method == "OPTIONS":
            return True

        elif request.method == "HEAD":
            return True