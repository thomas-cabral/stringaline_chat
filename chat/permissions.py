from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only let creator of object modify/delete said object.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user