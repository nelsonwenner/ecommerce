from rest_framework import permissions

class IsOrderOwner(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    return obj.customer_id == request.user.id