from rest_framework import permissions
from .models import *


class AddressPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_staff:
            return True
        return False


class ClientPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_staff:
            return True
        return False


class AdministratorPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if request.user.is_superuser:
                return True
            if (Administrator.objects.get(email=request.user.email).user.is_staff):
                return True
        except Administrator.DoesNotExist:
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


class BookPermission(permissions.BasePermission):

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