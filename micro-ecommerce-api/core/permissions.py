from rest_framework import serializers
from rest_framework import permissions
from .models import *

class ReadOnlyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

class IsClientOwner(permissions.BasePermission):
 
    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user.id

class IsAddressOwnerDetail(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.customer_id == request.user.id

class IsCheckoutOwner(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.customer_id == request.user.id

class IsCheckoutItemOwner(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.checkout.customer_id == request.user.id
