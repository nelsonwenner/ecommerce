from rest_framework import serializers
from rest_framework import permissions
from .models import *

class ReadOnlyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

class IsOwner(permissions.BasePermission):
 
    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user.id