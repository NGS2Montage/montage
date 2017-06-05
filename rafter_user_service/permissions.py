from rest_framework.permissions import BasePermission

class IsOwnerOrPost(BasePermission):
    """
    Custom permission to only allow owners to get.
    """
    message = "Application does not belong to user."

    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return True

        return request.user == obj.user
