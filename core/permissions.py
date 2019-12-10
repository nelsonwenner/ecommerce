from rest_framework import serializers
from rest_framework import permissions
from .models import *


class ClientPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_staff:
            return True
        return False


class ManagerPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if (Manager.objects.get(email=request.user.email).user.is_staff):
                return True
        except Manager.DoesNotExist:
            return False


class BookPermission(permissions.BasePermission):
    
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


class StatusPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if Client.objects.filter(email=request.user.email).exists():
            return True
        try:
            if (Manager.objects.get(email=request.user.email).user.is_staff):
                return True
        except Manager.DoesNotExist:
            return False


class GenrerPermission(permissions.BasePermission):
    
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


class AddressPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_staff:
            return True
        return False


class SalePermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if (Employee.objects.get(email=request.user.email).user.is_staff):
                return True
        except Employee.DoesNotExist:
            return False


class ItemsalePermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if (Employee.objects.get(email=request.user.email).user.is_staff):
                return True
        except Employee.DoesNotExist:
            return False


class ReportPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        try:
            if request.user.is_superuser:
                return True
            if (Administrator.objects.get(email=request.user.email).user.is_staff):
                return True
        except Administrator.DoesNotExist:
            return False