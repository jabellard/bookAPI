from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAdminOrObjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            if hasattr(obj, 'owner'):
                return (request.user.is_superuser or
                        (request.user == obj.owner))
            else:
                return (request.user.is_superuser or
                        (request.user == obj))
