from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = "Изменение чужого контента запрещено!"

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
