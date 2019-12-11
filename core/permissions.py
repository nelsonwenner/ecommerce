from rest_framework import serializers
from rest_framework import permissions
from .models import *


class ClientPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if Client.objects.filter(email=request.user.email).exists():
                return True
            try:
                if (Manager.objects.get(email=request.user.email).user.is_staff):
                    return True
            except Manager.DoesNotExist:
                return False
        except Client.DoesNotExist:
            return False


class AddressPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if Client.objects.filter(email=request.user.email).exists():
                return True
            try:
                if (Manager.objects.get(email=request.user.email).user.is_staff):
                    return True
            except Manager.DoesNotExist:
                return False
        except Client.DoesNotExist:
            return False


class ManagerPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if request.user.is_superuser:
                return True
            if (Manager.objects.get(email=request.user.email).user.is_staff):
                return True
        except Manager.DoesNotExist:
            return False


class BookPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            try:
                if (Manager.objects.get(email=request.user.email).user.is_staff):
                    return True
            except Manager.DoesNotExist:
                return False
        except Exception:
            return False # AnonymousUser


class StatusPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if (Manager.objects.get(email=request.user.email).user.is_staff):
                return True
        except Manager.DoesNotExist:
            return False


class GenrerPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if Client.objects.filter(email=request.user.email).exists():
                return False
            try:
                if (Manager.objects.get(email=request.user.email).user.is_staff):
                    return True
            except Manager.DoesNotExist:
                return False
        except Exception:
            return False


class AuthorPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if Client.objects.filter(email=request.user.email).exists():
                return False
            try:
                if (Manager.objects.get(email=request.user.email).user.is_staff):
                    return True
            except Manager.DoesNotExist:
                return False
        except Exception:
            return False


class WritePermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if Client.objects.filter(email=request.user.email).exists():
                return False
            try:
                if (Manager.objects.get(email=request.user.email).user.is_staff):
                    return True
            except Manager.DoesNotExist:
                return False
        except Exception:
            return False  
  

class OrderPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if Client.objects.filter(email=request.user.email).exists():
                return True
            try:
                if (Manager.objects.get(email=request.user.email).user.is_staff):
                    return True
            except Manager.DoesNotExist:
                return False
        except Client.DoesNotExist:
            return False 


class ItemOrderPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if Client.objects.filter(email=request.user.email).exists():
                return True
            try:
                if (Manager.objects.get(email=request.user.email).user.is_staff):
                    return True
            except Manager.DoesNotExist:
                return False
        except Client.DoesNotExist:
            return False


class CreditCardPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if Client.objects.filter(email=request.user.email).exists():
                return True
            try:
                if (Manager.objects.get(email=request.user.email).user.is_staff):
                    return True
            except Manager.DoesNotExist:
                return False
        except Client.DoesNotExist:
            return False
