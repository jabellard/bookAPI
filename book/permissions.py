from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsAdminOrObjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            print("IF------------------------------------")
            print(request.user)
            print(obj.owner)
            print("------------------------------------")
            return True
        else:
            print("------------------------------------")
            print(request.user)
            print(obj.owner)
            print("------------------------------------")
            return ( request.user.is_superuser or
            (request.user == obj.owner))
